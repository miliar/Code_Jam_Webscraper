#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <set>
#include <string>
using namespace std;

static const int MAXFEATURE = 16;
static const int MAXA = 111;
static const int MAXL = 111;
static const int MAXN = 111;

struct sTree
{
	double Weight;
	char Feature[ MAXFEATURE + 1 ];
	sTree *Left, *Right;
};

sTree *ReadTree()
{
	sTree *tree = new sTree;
	scanf( " (%lf", &tree->Weight );
	tree->Left = tree->Right = NULL;
	if( scanf( " %[a-zA-Z]", tree->Feature ) == 1 )
	{
		tree->Left = ReadTree();
		tree->Right = ReadTree();
	}
	else
		tree->Feature[ 0 ] = '\0';
	scanf( " )" );
	return tree;
}

void DeleteTree( sTree *tree )
{
	if( tree == NULL )
		return;
	DeleteTree( tree->Left );
	DeleteTree( tree->Right );
	delete tree;
}

int L, A, N;
sTree *Tree;
set< string > AnimalFeature[ MAXA ];
char Animal[ MAXA ];
double Result[ MAXA ];

void Read()
{
	int i;
	scanf( "%d", &L );
	Tree = ReadTree();
	scanf( "%d", &A );
	for( i = 0; i < A; ++i )
	{
		int n;
		scanf( "%s", &Animal[ i ] );
		scanf( "%d", &n );
		AnimalFeature[ i ].clear();
		while( n-- )
		{
			char feature[ MAXFEATURE ];
			scanf( "%s", feature );
			AnimalFeature[ i ].insert( feature );
		}
	}
}

void Work()
{
	int i;
	for( i = 0; i < A; ++i )
	{
		sTree *tree = Tree;
		double result = 1;
		while( tree != NULL )
		{
			result *= tree->Weight;
			if( AnimalFeature[ i ].find( tree->Feature ) != AnimalFeature[ i ].end() )
				tree = tree->Left;
			else
				tree = tree->Right;
		}
		Result[ i ] = result;
	}
	DeleteTree( Tree );
}

void Write( int t )
{
	int i;
	printf( "Case #%d:\n", t );
	for( i = 0; i < A; ++i )
	{
		printf( "%.9lf\n", Result[ i ] );
	}
}

int main()
{
	scanf( "%d", &N );
	for( int i = 0; i < N; ++i )
	{
		Read();
		Work();
		Write( i + 1 );
	}
	return 0;
}
