#define _CRT_SECURE_NO_DEPRECATE
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <set>
#include <cmath>
#include <queue>
#include <sstream>
#include <iostream>
using namespace std;

//////////////////// Defines ////////////////////

#pragma comment(linker, "/STACK:67108864")

#define inf      2147483647
#define inf64    9223372036854775807
#define eps      1e-6
#define pi      3.14159265358
#define sqr(a) (a)*(a)
#define rall(a) a.rbegin(),a.rend()
#define all(a) a.begin(),a.end()
#define sz(a) (a).size()
#define mset(a,v) memset(a, v, sizeof(a))
#define pb push_back 
typedef long long ll;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;

#define ContinueIf(x) if ((x)) continue
#define ContinueUnless(x) if(!(x)) continue

#define BreakIf(x) if ((x)) break
#define BreakUnless(x) if(!(x)) break

#define ReturnUnless(x) if (!(x)) return
#define ReturnIf(x) if ((x)) return

#define ReturnUnless2(x, ret) if (!(x)) return ret
#define ReturnIf2(x, ret) if ((x)) return ret

//////////////////// Problem Code ////////////////////

struct Chicken
{
	int x, v;
	Chicken() {}
	Chicken(int _x, int _v) : x(_x), v(_v) {}

	bool operator < (const Chicken& c) const
	{
		return x < c.x;
	}
};

bool WillReach(Chicken c, ll time, ll B)
{
	return c.x + time * c.v >= B;
}

bool willIntersect(Chicken c1, Chicken c2, int B, int capTime)
{
	double d1 = B - c1.x;
	double d2 = B - c2.x;
	double time1 = d1 / c1.v;
	double time2 = d2 / c2.v;

	if (time1 < time2 + eps)
	{
		return !WillReach(c2, capTime, B);
	}
	return false;
}

int main()
{
	int k, T;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &T);
	for(k = 1 ; k <= T ; ++k)
	{
		int N, K, B, time;
		scanf("%d%d%d%d", &N, &K, &B, &time);
		int ans = 0;
		vector<Chicken> chicks(N);
		for (int i = 0 ; i < N ; ++i)
		{
			scanf("%d", &chicks[i].x);
		}

		for (int i = 0 ; i < N ; ++i)
		{
			scanf("%d", &chicks[i].v);
		}
		sort(all(chicks));

		vector<int> pickups;
		for (size_t i = 0 ; i < chicks.size() ; ++i)
		{
			ContinueUnless(WillReach(chicks[i], time, B));
			int curr = 0;
			for (size_t j = i + 1 ; j < chicks.size() ; ++j)
			{
				if (willIntersect(chicks[i], chicks[j], B, time))
				{
					++curr;
				}
			}
			pickups.push_back(curr);
		}
		sort(all(pickups));
		if (pickups.size() < K)
		{
			printf("Case #%d: IMPOSSIBLE\n", k);
		}
		else
		{
			for (int i = 0 ; i < K ; ++i)
			{
				ans += pickups[i];
			}
			printf("Case #%d: %d\n", k, ans);
		}
	}
	return 0;
}

