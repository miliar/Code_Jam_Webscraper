#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <ctime>
using namespace std;
#define pb push_back
#define INF 1000000000
#define L(s) (int)((s).end()-(s).begin())
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define C(a) memset((a),0,sizeof(a))
#define llint long long
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define VI vector<int>
#define ppb pop_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
#define x first
#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pi 3.1415926535897932384626433832795028841971
#define tt (ll+rr)/2
#define rnd() ((rand() << 16) ^ rand())

int main()
{
	freopen("input.in","rt",stdin); freopen("output.out","wt",stdout);
	
	int tc, TC;
	cin >> TC;
	rep(tc, TC)
	{
		cerr << tc << endl;
		int s[301][301];
		int n = 300;
		memset(s,0,sizeof(s));
		int r, x1, x2, y1, y2;
		scanf("%d", &r);
		rept(i, r)
		{
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int i = x1; i <= x2; i++)
				for (int j = y1; j <= y2; j++)
					s[i][j] = 1;
		}
		int T = 0;
		for (; ; T++)
		{
			bool fl = false;
			rept(i, n)
				rept(j, n)
					if (s[i][j] == 1) fl = true;
			if(!fl) break;

			rep(i, n)
				rep(j, n)
					if (s[i - 1][j] == 1 && s[i][j - 1] == 1)
						s[i][j] = 2;
			rep(i, n)
				rep(j, n)
					if (s[i - 1][j] == 0 && s[i][j - 1] == 0 && s[i][j] != 0)
						s[i][j] = 3;
			rept(i, n)
				s[i][0] = s[0][i] = 3;



			rept(i, n)
				rept(j, n)
				{
					if (s[i][j] == 2)
						s[i][j] = 1;
					if (s[i][j] == 3)
						s[i][j] = 0;
				}

	/*		rept(i, 10)
			{
				rept(j, 10)
					printf("%d ",s[i][j]);
				printf("\n");
			}
			puts("");*/
		}

		printf("Case #%d: ",tc);
		printf("%d\n", T);
	}
	
	return 0;
}






