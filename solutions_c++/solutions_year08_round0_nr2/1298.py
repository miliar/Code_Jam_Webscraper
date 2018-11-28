#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <vector>
#include <iostream>

#include <conio.h>
#include <stack>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <map>
#include <cmath>

using namespace std;

const int INF = 1000*1000*1000 + 10;
const double EPS = 1E-6;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef long long ll;
typedef vector<bool> vb;
typedef vector<ll> vll;
#define all(s) s.begin(), s.end()

#define forn(i, n) for (int i = 0; i < n; ++i)

struct shed
{
	int start, end;
	int ind;
	bool side;

	bool operator< (const shed & s)
	{
		return start < s.start;
	}
};

int main()
{
#ifdef _DEBUG
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		int t, n, m;
		cin >> t >> n >> m;
		vector<shed> a(n + m);
		
		for (int i = 0; i < n; ++i)
		{
			int hh, mm;
			scanf("%d:%d ", &hh, &mm);
			a[i].start= hh * 60 + mm;
			scanf("%d:%d", &hh, &mm);
			a[i].end= hh * 60 + mm;
			a[i].ind = i;
			a[i].side = true;
		}

		for (int i = 0; i < m; ++i)
		{
			int hh, mm;
			scanf("%d:%d ", &hh, &mm);
			a[n+i].start = hh * 60 + mm;
			scanf("%d:%d", &hh, &mm);
			a[n+i].end = hh * 60 + mm;
			a[n+i].ind = n + i;
			a[n+i].side = false;
		}

		int ans[2] = {0, 0};

		sort(all(a));

		vi used(n + m);
		for (int i = 0; i < n + m; ++i)
			if (!used[i])
			{
				ans[a[i].side]++;
				bool side = !a[i].side;
				int time = a[i].end + t;
				bool cool = true;
				for ( ; cool ; )
				{
					cool = false;
					for (int j = 0; j < n + m; ++j)
						if (!used[j] && a[j].side == side && a[j].start >= time)
						{
							used[j] = true;
							time = a[j].end + t;
							side ^= true;
							cool = true;
							break;
						}
				}
			}


		printf("Case #%d: %d %d\n", test, ans[1], ans[0]);
	}
}
