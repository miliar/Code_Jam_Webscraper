#include <stdio.h>
#include <algorithm>
#include <queue>
using namespace std;
#define N 100000
int l, d, n, cnt, size, val;
char str[N/10], tmp[N/10];
int mark[1000][26];
struct Node {
	int end, level;
	Node *next[26];
	void init( ){
		end = level = 0;
		memset( next, 0, sizeof(next) );
	}
}trie[N], *root = &trie[0], *que[N];

void init( ){
	root->init( );
	cnt = 0;
	size = 1;
	//memset( mark, 0, sizeof(mark) );
}

void insert( ){
	Node *p = root;
	int i = 0, index, l = 0;
	while ( str[i] ){
		index = str[i] - 'a';
		if ( p->next[index] == 0 ){
			p->next[index] = &trie[size++];
			p = p->next[index];
			p->init( );
			p->level = ++l;
		}
		else{
			p = p->next[index];
			l = p->level;
		}
		i++;
	}
	p->end = ++cnt;
}

void bfs( ){
	int head = 0, tail = 1, i;
	Node *p, *q;
	que[0] = root;
	while ( head < tail ){
		p = que[head++];
		for ( i = 0; i < 26; i++ )
			if ( p->next[i] ){
				q = p->next[i];
				que[tail++] = q;
				printf( "%d %d\n", i, q->level );
			}
	}
}

void dfs( Node *x, int y ){
	if ( x->level == y ){
		if ( x->end == 0 ) return;
		int i;
		for ( i = 1; i <= y; i++ ) if ( mark[i][tmp[i]-'a'] == 0 ) break;
		if ( i == y+1 ){
			val++;
		}
		return;
	}
	int i;
	for ( i = 0; i < 26; i++ ){
		if ( x->next[i] ){
			tmp[x->next[i]->level] = char(i+'a');
			dfs( x->next[i], y );
		}
	}
}

int main( ){
	int i, j, x, y;
	scanf( "%d%d%d", &l, &d, &n );
	//while ( scanf( "%d%d%d", &l, &d, &n ) != EOF ){
		init( );
		for ( i = 0; i < d; i++ ){
			scanf( "%s", str );
			insert( );
		}
		//bfs( );
		for ( i = 1; i <= n; i++ ){
			scanf( "%s", str );
			memset( mark, 0, sizeof(mark) );
			x = 0, y = 0;
			for ( j = 0; str[j]; j++ ){
				if ( str[j] == '(' ){
					x = 1;
					y++;
				}
				else if ( str[j] == ')' ){
					x = 0;
				}
				else {
					if ( x == 0 ){
						mark[++y][str[j]-'a'] = 1;
						x = 0;
					}
					else {
						mark[y][str[j]-'a'] = 1;
					}
				}
			}
			/*for ( x = 1; x <= l; x++ ){
				for ( y = 0; y < 26; y++ ) if ( mark[x][y] ) printf( "%d ", y );
				printf( "\n" );
			}*/
			val = 0;
			dfs( root, l );//Case #1: 2 Case #X: K
			printf( "Case #%d: %d\n", i, val );
		}
	//}
}
