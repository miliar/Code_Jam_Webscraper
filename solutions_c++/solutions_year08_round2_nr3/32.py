#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define VI vector<int>
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define all(v) v.begin(), v.end()

#define NMAX 1000005
#define DMAX 105

int f[NMAX];
bool used[NMAX];
int ans[NMAX];
int d[DMAX];
int n, k;

int next(int x)
{
	return x | (x + 1);
}

int prev(int x)
{
	return x & (x + 1);
}

int sum(int x)
{
	int ret = 0;
	while (x >= 0)
	{
		ret += f[x];
		x = prev(x) - 1;
	}
	return ret;
}

int sum(int l, int r)
{
	return sum(r) - sum(l - 1);
}

void update(int x, int val)
{
	while (x < k)
	{
		f[x] += val;
		x = next(x);
	}
}

int getFree(int l, int r)
{
	return r - l + 1 - sum(l, r);
}

int findKth(int start, int q)
{
	int l = start, r = k - 1;
	while (r - l > 2)
	{
		int mid = (l + r) / 2;
		if (getFree(start, mid) < q)
		{
			l = mid;
		}		
		else
		{
			r = mid;
		}
	}
	int ret = -1;
	for (int i = l; i <= r; i++)
	{
		if (getFree(start, i) == q)
		{
			ret = i;
			break;
		}		
	}
	while (used[ret]) --ret;
	return ret;
}

void solve(int tc)
{
	cerr << tc << endl;
	cin >> k >> n;
	forn(i, n) cin >> d[i];
	printf("Case #%d:", tc);

	forn(i, k)
	{
		f[i] = 0;
		used[i] = false;
	}

	int ptr = 0;
	for1(i, k)
	{
		int s = getFree(ptr, k - 1);
		int r = i;
		if (s >= r)
		{
			int id = findKth(ptr, r);
			update(id, 1);
			ans[id + 1] = i;
			used[id] = true;
			ptr = id;	
		}
		else
		{
			r -= s;
			ptr = 0;
			s = getFree(0, k - 1);
			r %= s;
			if (r == 0) r = s;
			int id = findKth(ptr, r);
			update(id, 1);
			ans[id + 1] = i;
			used[id] = true;
			ptr = id; 
		}
	}

	forn(i, n) printf(" %d", ans[d[i]]);
	printf("\n");
}

int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
	int tc;
	cin >> tc;
	forn(it, tc) solve(it + 1);
	return 0;
}
         	
