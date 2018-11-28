#include <iostream>
#include <algorithm>
using namespace std;

struct point {
	char RT[ 30 ];
	int top;
}p[ 1000 ];

int hash[ 30 ];

struct trie {
	trie *next[26];
	int color;

	void Init() {
		memset( next, 0, sizeof( next ));
		color = 0;
	}
}*root;

char str[ 2000 ];
int l, d, n, top;

void Insert( char *str ) {
	int p = 0;

	trie* now = new trie;
	now->Init();

	now = root;
	while( str[p] ) {
		int c = str[p] - 'a';
		if( !now->next[c] ) {
			now->next[c] = new trie;
			now->next[c]->Init();
		}
		now = now->next[c];
		p ++;
	}
	now->color = 1;
}

int ans;

void dfs( int depth, trie *now ) {
	int i;

	if( depth == l ) {
		if( now->color ) {
			ans ++;
		}
		return ;
	}

	for( i = 0; i < p[ depth ].top; i++) {
		if( now->next[ p[ depth ].RT[i] ] ) {
			dfs( depth+1, now->next[ p[ depth ].RT[i] ] );
		}
	}
}

int main() {

	int i, j;

	freopen ( "A-large.in", "r", stdin );
	freopen ( "A-large.out", "w", stdout );
	while( scanf("%d %d %d", &l, &d, &n) != EOF ) {

		root= new trie;
		root->Init();

		while( d-- ) {
			scanf("%s", str);
			Insert( str );
		}

		int T = 1;
		while( n-- ) {

			top = 0;
			scanf("%s", str);
			for(i = 0; str[i]; i++) {
				if( str[i] == '(' ) {
					memset( hash, 0, sizeof( hash ) );
					for( j = i+1; ; j++) {
						if( str[j] == ')' )
							break;
						hash[ str[j] - 'a' ] = 1;
					}
					i = j;

					p[ top ].top = 0;
					for( j = 0; j < 26; j++) {
						if( hash[j] == 1 ) {
							p[ top ].RT[ p[ top ].top++ ] = j;
						}
					}
					top ++;

				}else {
					memset( hash, 0, sizeof( hash ) );
					hash[ str[i] - 'a' ] = 1;
					p[ top ].top = 0;
					for( j = 0; j < 26; j++) {
						if( hash[j] == 1 ) {
							p[ top ].RT[ p[ top ].top++ ] = j;
						}
					}
					top ++;
				}
			}
				
			ans = 0;
			if( top == l ) {
				dfs( 0, root );
			}
			printf("Case #%d: %d\n", T++, ans);
		}
	}

	return 0;
}

/*
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc
*/