#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
#include <algorithm>
using namespace std;

#define MAX 512

int main()
{
	int L, D, N;
	scanf("%d %d %d", &L, &D, &N);

	char lang[5002][16];
	char word[1024];
	for ( int i=0 ; i<D ; ++i ) 
	{
		scanf("%s", lang[i]);
	}
	for ( int T=1 ; T<=N ; ++T )
	{
		scanf("%s", word);
		int len = strlen(word);
		char tmp[16] = {0, };
		bool table[D][28];
		memset(table, 0, sizeof(table));
		for ( int i=0, j=0 ; i<len ; ++i )
		{
			if ( islower(word[i]) )
			{
				tmp[j++] = word[i];
			}
			else 
			{
				tmp[j] = '*';
				while ( word[i] != ')' )
				{
					table[j][word[i]] = true;
					++i;
				}
				++j;
			}
		}

		int res = 0;
		if ( strlen(tmp)==L )
		{
			for ( int i=0 ; i<D ; ++i )
			{
				bool flag = true;
				for ( int j=0 ; j<L ; ++j )
				{
					if ( tmp[j] == '*' )
					{
						if ( !table[j][lang[i][j]] ) 
						{
							flag = false;
							break;
						}
					}
					else if (tmp[j] != lang[i][j] )
					{
						flag = false;
						break;
					}
				}
				if ( flag ) ++res;
			}
		}
		printf("Case #%d: %d\n", T, res);
	}
	return 0;
}

