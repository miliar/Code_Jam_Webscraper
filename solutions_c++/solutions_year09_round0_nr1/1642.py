#include <stdio.h>
#include <string.h>

typedef struct st_Trie
{
	struct st_Trie* next[26];
	bool isword;
} Trie;

typedef struct
{
	int len;
	int ch[28];
} Patt;

int search( const Trie* trie, const Patt word[] )
{
	int i;
	int num;

	if( word->len == 0 )
		{
		return trie->isword ? 1 : 0;
		}//end if

	num = 0;
	for( i = 0; i < word->len; ++i )
		{
		if( trie->next[word->ch[i]] != NULL )
			{
			num += search( trie->next[word->ch[i]], word+1 );
			}//end if
		}//end for

	return num;
}//end search

Trie trie[90000];
int tnum = 0;

char str[512];
Patt word[16];

int main()
{
	int l, d, n;
	Trie* t;
	int x;
	int i, j, w;

	freopen( "A-large.in", "r", stdin );
	freopen( "A.out", "w", stdout );

	scanf( "%d%d%d", &l, &d, &n );

	memset( trie, 0, sizeof( Trie ) );
	tnum = 1;

	for( x = 0; x < d; ++x )
		{
		scanf( "%s", str );
		for( t = trie, i = 0; str[i] != '\0'; ++i )
			{
			j = str[i]-'a';
			if( t->next[j] == NULL )
				{
				t->next[j] = &trie[tnum++];
				memset( t->next[j], 0, sizeof( Trie ) );
				}//end if
			t = t->next[j];
			}//end for
		t->isword = true;
		}//end for

	for( x = 1; x <= n; ++x )
		{
		scanf( "%s", str );
		for( w = i = 0; str[i] != '\0'; ++i, ++w )
			{
			if( str[i] == '(' )
				{
				for( j = 0, ++i; str[i] != ')'; ++i, ++j )
					{
					word[w].ch[j] = str[i] - 'a';
					}//end for
				word[w].len = j;
				}
			else{
				word[w].ch[0] = str[i] - 'a';
				word[w].len = 1;
				}//end if
			}//end for
		word[w].len = 0;
		printf( "Case #%d: %d\n", x, search( trie, word ) );
		}//end for

	return 0;
}