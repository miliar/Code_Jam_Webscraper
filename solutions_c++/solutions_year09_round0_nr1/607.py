#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<iostream>

#include<cctype>
using namespace std;

char convert(char a)
{
	return a - 'a';
}

struct Trie
{
	Trie *node[26];
	char isWordEndHere;

	Trie()
	{
		fill( node, node+26, (Trie *)NULL);
		isWordEndHere = 0;
	}
};



void del( Trie *&n)
{
	for(int i =0;i<26;i++)
	{
		if( n->node[i] )
			del(n->node[i]);
	}

	delete n;
	n = NULL;
}


void addTrie( char *word , Trie *r)
{
	for(int i =0; word[i];  i++)
	{
		char c = convert(word[i]);
		if( r->node[c] == NULL )
		{
			r->node[c] = new Trie;
		}
		r = r->node[c];
	}
	r->isWordEndHere = 1;
}



char buf[6000];
int l , d , n;

string suspect;


int findIt( int curIdx , int curSize , Trie *curRoot)
{
	if( curSize == l )
	{
		return curRoot->isWordEndHere;
	}
	if( curRoot )
	{
		if( suspect.size() <= curIdx )
			return 0;
		if( suspect[curIdx] == '(' )
		{
			curIdx++;
			int ans = 0;
			int nextIdx = suspect.find( ")",curIdx );
			while(  suspect[curIdx] != ')'  )
			{
				if( curRoot->node [ convert(suspect[curIdx]) ] )
					ans += findIt(nextIdx+1,curSize+1,curRoot->node [ convert(suspect[curIdx]) ] );
				curIdx++;
			}
			return ans;

		}
		else //...?
		{
			if( curRoot->node [ convert(suspect[curIdx]) ] )
				return findIt(curIdx+1,curSize+1,curRoot->node [ convert(suspect[curIdx]) ] );

		}

	}


	return 0;
}



//

int main()
{
	int cur = 0;
	Trie *root = new Trie;
	int i;

	scanf("%d%d%d" , &l,&d,&n);
	gets(buf);
	for(i = 0 ; i< d;i++)
	{
		gets(buf);
		addTrie( buf , root );
	}

	int cases = 0;
	while( n-- )
	{
		getline(cin,suspect);
		printf("Case #%d: %d\n" , ++cases , findIt(0,0,root) );
	}



	del( root);
	return 0;
}
