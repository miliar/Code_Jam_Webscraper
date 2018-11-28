#define _CRT_SECURE_NO_DEPRECATE
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
#include <cstdio>
#include <memory>
using namespace std;
#define pb push_back
#define INF 1000000000
#define L(s) (int)((s).end()-(s).begin())
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define C(a) memset((a),0,sizeof(a))
#define ll long long
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
//#define tt (ll+rr)/2
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define rnd() ((rand() << 16) ^ rand())

#define sec(x, i, j) ((((i) < 0) || ((j) < 0))?0:(x[i][j]))

char s[555][555];
int a[555][555];
ll csn[555][555], csm[555][555];

pdd operator + (const pdd & a, const pdd & b)
{
	return pdd(a.x + b.x, a.y + b.y);
}
pdd operator * (double q, const pdd & a)
{
	return pdd(a.x * q, a.y * q);
}

struct mpoint
{
	double m;
	pdd pos;
	mpoint(double _m, pdd _pos) : m(_m), pos(_pos) {}
};

mpoint operator + (const mpoint & a, const mpoint & b)
{
	return mpoint(a.m + b.m, (a.m) / (a.m + b.m) * a.pos + (b.m) / (a.m + b.m) * b.pos);
}

mpoint mnew(int i, int j)
{
	return mpoint(a[i][j], mp(i, j));
}

int solve(int n, int m, int d)
{
	rept(i, n)
		rept(j, m)
			a[i][j] = s[i][j] - '0' + d;

	int res = 0;

	rept(i, n - 1)
		rept(j, m - 1)
		{
			mpoint cur = mpoint(0, mp(0, 0));
			for (int k = 3; k < min(n - i + 1, m - j + 1); k++)
			{
				mpoint A = mnew(i + k - 2, j);
				mpoint B = mnew(i, j + k - 2);
				mpoint C = mnew(i + k - 2, j + k - 2);
				cur = cur + A;
				cur = cur + B;
				cur = cur + C;
				rept(t, k)
				{
					if (t == 0 || t == k - 1) continue;
					mpoint X = mnew(i + t, j + k - 1);
					mpoint Y = mnew(i + k - 1, j + t);
					cur = cur + X;
					cur = cur + Y;
				}
				pdd mbe = mp(i + (k - 1) * 0.5, j + (k - 1) * 0.5); 
				
				if (abs(cur.pos.x - mbe.x) < 1e-7 && abs(cur.pos.y - mbe.y) < 1e-7)
				{
					res = max(res, k);
				}
			}
		}


	return res;
}


int main()
{
        #ifndef ONLINE_JUDGE 
        freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout); 
        #endif

		int TC;
		cin >> TC;
		rept(tc, TC)
		{
			int n, m, d;
			scanf("%d%d%d", &n, &m, &d);
			
			gets(s[0]);
			rept(i, n)
				gets(s[i]);

			int res = solve(n, m, d);

			if (res < 3)
			{
				printf("Case #%d: IMPOSSIBLE\n", tc + 1);
			}
			else
			{
				printf("Case #%d: %d\n", (tc + 1), res);
			}
		}

        
        return 0;
}