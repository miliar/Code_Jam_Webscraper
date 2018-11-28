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
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pi 3.1415926535897932384626433832795028841971
//#define tt (ll+rr)/2
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define rnd() ((rand() << 16) ^ rand())

inline double wp(const vector<string> & s, const vector<bool> & used, int num)
{
	double res = 0.0, cnt = 0.0;
	rept(i, L(s))
		if (!used[i])
			if (s[num][i] != '.')
			{
				res += s[num][i] - '0';
				cnt++;
			}
	return res / cnt;
}

inline double owp(const vector<string> & s, vector<bool> used, int num)
{
	used[num] = true;
	double res = 0, cnt = 0;
	int n = L(s);
	rept(j, n)
		if (j != num)
			if (s[j][num] != '.')
			{
				res += wp(s, used, j);
				cnt++;
			}
	return res / cnt;
}

inline double oowp(const vector<string> & s, vector<bool> used, int num)
{
	double res = 0.0, cnt = 0.0;

	rept(i, L(s))
		if (s[num][i] != '.')
		{
			res += owp(s, used, i);
			cnt++;
		}

	return res / cnt;
}


int main()
{
	#ifndef ONLINE_JUDGE 
	freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout); 
	#endif
	
	int TC;
	cin >> TC;
	rep(tc, TC)
	{
		int n;
		cin >> n;
		vector<string> s(n, "");

		rept(i, n)
			cin >> s[i];

		
		printf("Case #%d:\n", tc);
		rept(i, n)
		{
			cerr << i << endl;
			vector<bool> used(n, false);
			double w = wp(s, used, i);
			double ow = owp(s, used, i);
			double oow = oowp(s, used, i);

			double res = 0.25 * w + 0.5 * ow + 0.25 * oow;

			printf("%.9lf\n", res);
		}


	}
	
	return 0;
}
