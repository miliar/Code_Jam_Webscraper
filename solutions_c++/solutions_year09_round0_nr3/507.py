#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iomanip>

using namespace std;

#define mp make_pair
#define pb push_back
#define sz(c) (int)((c).size())
#define f first
#define s second

#define fin  "C.IN"
#define fout "C.OUT"

#define NMAX 512
#define MOD  10000

int T;
char buff[NMAX];
int dp[NMAX][20];

string s = "welcome to code jam";

int main()
{
	int i, j, k, t, cnt;

	ifstream f1(fin);
	ofstream f2(fout);
	
	f1 >> T;
	f1.get();

	for ( t = 1; t <= T; ++t)
	{
		f1.getline(buff,sizeof(buff));
		
		cnt = 0;
		memset(dp,0,sizeof(dp));

		for ( i = 0; i < strlen(buff); ++i )
		{
			for ( j = 0; j < sz(s); ++j )
				if ( s[j] == buff[i] )
				{
					if ( j == 0 )
						dp[i][0] = 1;
					else
					for ( k = 0; k < i; ++k )
						if ( buff[k] == s[ j - 1 ] )
							dp[ i ][ j ] = (dp[ i ][ j ] + dp[ k ][ j - 1 ]) % MOD;
				}

			if ( dp[ i ][ sz(s) - 1 ] )
				cnt = (cnt + dp[ i ][ sz(s) - 1 ]) % MOD;
		}

		f2 << "Case #" << t << ": " << setfill('0') << setw(4) << cnt << endl;
	}

	return 0;
}