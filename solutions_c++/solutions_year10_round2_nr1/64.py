#include <cstdio>
#include <iostream>
#include <memory.h>
#include <vector>
#include <ctime>
#include <string>
#include <algorithm>
#include <cstring>
#include <utility>
#include <map>
#include <set>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
#define pb push_back
typedef pair<int,int> pii;
typedef long long ll;

struct node{
	vector<pii> to;
//	int key;
};

map<string,int> mm;
int n, m, knode;
node trie[100010];
char s[1010];
int kd;

inline int getid( string& s )
{
	if ( mm.find( s ) == mm.end() ) mm[s] = kd++;
	return mm[s];
}

void go( int& cnode, string& s )
{
	int x = getid( s );
	forn( i, trie[cnode].to.size() )
		if ( trie[cnode].to[i].first == x )
		{
			cnode = trie[cnode].to[i].second;
			return;
		}
		
	int z = knode++;
	trie[z].to.clear();
	trie[cnode].to.pb( pii( x, z ) );
	cnode = z;
}

void add( char* s )
{
	int k = strlen( s );
	k--;
	s[k] = '/';
	string cur = "";
	int cnode = 0;
	for ( int i=1; i<=k; i++ )
		if ( s[i] == '/' )
		{
			go( cnode, cur );
			cur = "";
		}
		else cur += s[i];
}

int main()
{
	int t;
	scanf( "%d", &t );
	for ( int q=1; q<=t; q++ )
	{
		scanf( "%d %d", &n, &m );
		mm.clear();
		gets( s );
		knode = 1;
		kd = 0;
		trie[0].to.clear();
		forn( i,n )
		{
			gets( s );
			add( s );
		}
		int c = knode;
		//printf( "-> %d\n", c );
		forn( i,m )
		{
			gets( s );
			add( s );			
		}
		printf( "Case #%d: %d\n", q, knode - c );
	}
	return 0;
}
