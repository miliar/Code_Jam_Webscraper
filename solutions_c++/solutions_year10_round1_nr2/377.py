#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <queue>
#include <complex>
#include <queue>
#include <string.h>
#include <fstream>
using namespace std;

#define IT(c) typeof((c).begin())

#define FOR(i, a, b) for(int (i) =  int(a); i < int(b); ++i)
#define REP(x, n) FOR(x,0,n)
#define FORIT(c, i) for(IT(c) i = (c).begin(); i != (c).end(); ++i)

#define bound(num, lower, upper) (max(min((num),((upper)-1)),(lower)))
#define debug(x) cerr << #x << " = " << x << "\n"

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()


typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;

/*==================================================================================================================*/

int main()
{
int np; cin >> np;
for(int tp = 0; tp < np; tp++)
{
	int D,I,m,n; cin >> D >> I >> m >> n;
	vector<int> p(n, 0);
	for(int i = 0; i < n; i++)
		cin >> p[i];
	
	int dp[101][256];
	memset(dp, 0, sizeof(dp));

	const int big = 100000000;
	for(int i = 0; i < 101; i++) for(int k = 0; k < 256; k++) dp[i][k] = big;

	for(int k = 0; k < 256; k++)
	{
		int small = abs(p[0] - k);
		
		
		int base= 0;
		int i = 0;
		for(int l = 0; l  < 256; l++)
			{
				for(int me = 0; me < 256; me++)
				{
					if(abs(l - me) <= m)
					{
						base = 0 + abs(me - p[i]);
						if(m != 0)
						{
							int add = ceil(((double)(abs(me - k)/(double)m)))*I;
							small = min(base + add, small);
						}
						else if(me == k)
							small = min(small, base);

					
					}		
				}
			}



		//cout << k << " " << small << endl;

		if(D < small)
			small = D;
		dp[0][k] = small;
	}

	for(int i = 1; i < n; i++)
		for(int k = 0; k < 256; k++)
		{
			int small = big;
			small = min(small, D + dp[i-1][k]);
			
			int base = big;
			for(int l = 0; l  < 256; l++)
			{
				for(int me = 0; me < 256; me++)
				{
					if(abs(l - me) <= m)
					{
						base = dp[i-1][l] + abs(me - p[i]);
						if(m != 0)
						{
							int add = ceil(((double)(abs(me - k)/(double)m)))*I;
							small = min(base + add, small);
						}
						else if(me == k)
							small = min(small, base);
					}		
				}
			}

			//cout << k << " " << small << endl;
			
			dp[i][k] = small;
		}
	
	int answer = big;
	for(int k = 0; k < 256; k++)
	{
		answer = min(answer, dp[n-1][k]);
	}

	printf("Case #%d: %d\n", tp + 1, answer);

}
}

