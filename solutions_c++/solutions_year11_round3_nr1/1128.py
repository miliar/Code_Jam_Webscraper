// gcc version 4.5.0 (tdm-1)
// g++ -I tr1 femidav.cpp -O2 -Wall -std=c++0x -o femidav.exe
// femidav < small-attempt0.in > small-attempt0.out
// femidav < large.in > large.out

#include <cstdio>
#include <iostream>
#include <string>

#define FOR(I, N) for( int I = 0, end_ = (N); I < end_; ++I )
int ri() { int r; scanf("%d", &r); return r; }
std::string const rs() { std::string r; std::cin >> r; return r; }

int main()
{
	FOR(i, ri())
	{
		int R = ri(), C = ri();
		char tiles[R][C];
		FOR(j, R)
		{
			std::string S = rs();
			FOR(k, C)
				tiles[j][k] = S[k];
		}

		bool impossible = false;
		for( int j = 0; !impossible && j < R; ++j )
			for( int k = 0; !impossible && k < C; ++k )
				if ( tiles[j][k] == '#' )
				{
					if ( j + 1 >= R || k + 1 >= C || tiles[j + 1][k] != '#' || tiles[j + 1][k + 1] != '#' || tiles[j][k + 1] != '#' )
						printf("Case #%d:\nImpossible\n", i + 1), impossible = true;
					else
					{
						tiles[j][k] = '/';
						tiles[j][k + 1] = '\\';
						tiles[j + 1][k] = '\\';
						tiles[j + 1][k + 1] = '/';
					}
				}

		if ( !impossible )
		{
			printf("Case #%d:\n", i + 1);
			FOR(j, R)
			{
				FOR(k, C)
					printf("%c", tiles[j][k]);
				printf("\n");
			}
		}
	}
}
