#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <memory.h>
#include <cmath>
#include <cassert>

using namespace std;

#define fr(i,a,b) for(int i = (a); i <= (b); ++i)
#define fi(a) for(int i = (0); i < (a); ++i)
#define fj(a) for(int j = (0); j < (a); ++j)
#define fk(a) for(int k = (0); k < (a); ++k)

typedef long long ll;

int r, lim, n, a[1000];
ll ans;
int nxt[1000];
ll add[1000];

void preb()
{
	fi(n)
	{
		ll sum = 0;
		bool q = true;
		fj(n)
		{
			sum = sum + (ll)a[(i + j) % n];
			if (sum > lim)
			{
				nxt[i] = (i + j) % n;
				if (i == nxt[i])
					nxt[i] = (nxt[i] + 1) % n;
				add[i] = sum - (ll)a[(i + j) % n];
				q = false;
				break;
			}
		}
		if (q)
		{
			nxt[i] = i;
			add[i] = sum;
		}
	}
}

void make(int &ptr)
{
	ans += add[ptr];
	ptr = nxt[ptr];
}

void solve()
{
	scanf("%d%d%d", &r, &lim, &n);
	fi(n)
		scanf("%d", &a[i]);
	preb();

	ans = 0;
	int ptr = 0;
	fi(r)
		make(ptr);

	cout << ans << endl;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	fi(t)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return (0);
} 
