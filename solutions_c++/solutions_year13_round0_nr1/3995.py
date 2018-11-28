#include <iostream>
#include <math.h>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <limits.h>
#include <cstdio>

#include <utility>

#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;



void main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
	int tt;
	cin >> tt;

	int vt= 0 , ht = 0, vo = 0, ho = 0;
	bool dots = false;
	bool game = false;
	char f[4][4];

	for( int t= 0; t < tt; t++ )
	{
		vt = 0 ; ht = 0; vo = 0; ho = 0;
		dots = false;
		game = false;


		for( int i = 0; i < 4; i++ )
			for( int j = 0; j < 4; j++ )
			{
				cin >> f[i][j];
				if( f[i][j] == '.' )
					dots = true;
			}

		for( int i = 0; i < 4; i++ )
		{
			vt = 0 ; ht = 0; vo = 0; ho = 0;
			for( int j = 0; j < 4; j++ )
			{
				if( f[i][j] == 'X' || f[i][j] == 'T' ) ht++;
				if( f[i][j] == 'O' || f[i][j] == 'T' ) ho++;

				if( f[j][i] == 'X' || f[j][i] == 'T' ) vt++;
				if( f[j][i] == 'O' || f[j][i] == 'T' ) vo++;

			}
			
			if( ht == 4 || vt == 4 )
			{
				cout << "Case #"<< t+1 << ": " << "X won" << endl;
				game = true;
				break;
			}
			if( vo == 4 || ho == 4 )
			{
				cout << "Case #"<< t+1 << ": " << "O won" << endl;
				game = true;
				break;
			}

		}
		
		if( game )
			continue;

		int px = 0, po = 0, lx = 0, lo = 0;

		for( int i = 0; i < 4; i++  )
		{
			if( f[i][i] == 'X' || f[i][i] == 'T' ) px++;
			if( f[i][i] == 'O' || f[i][i] == 'T' ) po++;

			if( f[i][4-i-1] == 'X' || f[i][4-i-1] == 'T' ) lx++;
			if( f[i][4-i-1] == 'O' || f[i][4-i-1] == 'T' ) lo++;
		}

		if( px == 4 || lx == 4 )
		{
			cout << "Case #"<< t+1 << ": " << "X won" << endl;
			continue;
		}
		if( po == 4 || lo == 4 )
		{
			cout << "Case #"<< t+1 << ": " << "O won" << endl;
			continue;
		}

		if( dots )
		{
			cout << "Case #"<< t+1 << ": " << "Game has not completed" << endl;
			continue;
		}

		cout << "Case #"<< t+1 << ": " << "Draw" << endl;


	}

}

