// AlienLan.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include <vector>
#include <string>
#include <map>
#include <assert.h>

using namespace std;

#define MAX_WORD_LEN 15
#define MAX_BUF_LEN	1024

typedef struct _SolveTree
{
	map<char,_SolveTree *> data;
	_SolveTree *parent;
}SolveTree, STreeNode;
typedef map<char,_SolveTree *>::iterator TMapIter;
typedef map<char,_SolveTree *>::const_iterator TCMapIter;

SolveTree g_existTree;

void TreeInsert(char *buf)
{
	TMapIter it;
	SolveTree *pt = &g_existTree, *pt2;
	int i;
	for( i=0;buf[i];i++ )
	{
		if( pt->data.find(buf[i])==pt->data.end() )
		{
			pt2 = new STreeNode;
			pt->data[buf[i]] = pt2;
			pt2->parent = pt;
			pt = pt2;
		}
		else
		{
			pt = pt->data[buf[i]];
		}
	}
}

void AnalysisPattern( char *buf, vector<string> &pattern )
{
	int i,j,idx;
	idx = 0;
	for( i=0;buf[i] && buf[i]!='\n'; )
	{
		if( buf[i]=='(' )
		{
			for(j=i+1;buf[j]!=')';j++ )
				;
			pattern[idx++].assign( buf,i+1,j-i-1 );
			i = j+1;
		}
		else
			pattern[idx++].assign( buf,i++,1 );
	}
}

int CountMatch( vector<string> &pattern )
{
	static int idxArray[MAX_WORD_LEN+1];
	int i = 0;
	int ret = 0;
	const SolveTree *pt = &g_existTree;
	TCMapIter cit;

	for( idxArray[0]=0; i>=0; )
	{
		if( i==(int)pattern.size() )
		{
			ret ++;
			pt = pt->parent;
			i --;
		}
		else if( idxArray[i]<(int)pattern[i].size() )
		{
			if( (cit=pt->data.find(pattern[i][idxArray[i]]))!=pt->data.end() )
			{
				pt = cit->second;
				idxArray[i] ++;
				i ++;
				idxArray[i] = 0;
			}
			else
				idxArray[i] ++;
		}
		else
		{
			pt = pt->parent;
			i --;
		}
	}
	return ret;
}

void DestroySTreeImpl(SolveTree *p)
{
	for( TMapIter it=p->data.begin(); it!=p->data.end(); it++ )
	{
		DestroySTreeImpl( it->second );
	}
	delete p;
}

void DestroySTree()
{
	for( TMapIter it=g_existTree.data.begin(); it!=g_existTree.data.end(); it++ )
	{
		DestroySTreeImpl( it->second );
	}
}

void AlienLan()
{
	FILE *f = fopen( "in.txt", "r" );
	FILE *g = fopen( "out.txt", "w" );
	int l,d,n;
	int i;
	char buf[MAX_BUF_LEN];
	vector<string> pattern;

	assert( f && g );
	fgets( buf,MAX_BUF_LEN,f );
	sscanf( buf,"%d %d %d", &l,&d,&n );
	pattern.resize( l );

	for( i=0;i<d;i++ )
	{
		fgets( buf,MAX_BUF_LEN,f );
		buf[l] = 0;
		TreeInsert( buf );
	}

	for( i=0;i<n;i++ )
	{
		fgets( buf,MAX_BUF_LEN,f );
		AnalysisPattern( buf,pattern );
		fprintf( g,"Case #%d: %d\n", i+1, CountMatch( pattern ) );
	}
	fclose( f );

	DestroySTree();
}

int main()
{
	AlienLan();
	return 0;
}

