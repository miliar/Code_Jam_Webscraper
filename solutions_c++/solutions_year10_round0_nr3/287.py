#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()
#define sz(a) a.size()

typedef pair<int, int> pii;
typedef long long lint;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int Size = 10000;
char buffer[Size];

const int inf = 0x0fffffff;
const int white = 0, gray = 1, black = 2;

const double eps = 10e-6;

lint Solve()
{
	int r, k, n;
	scanf("%d%d%d", &r, &k, &n);
	vi v(n);
	for(int i = 0; i < n; i++)
		scanf("%d", &v[i]);
	vi vvv = v;
	for(int i = 0; i < n; i++)
		v.insert(v.end(), all(vvv));
	vi bit(n);
	lint res = 0;
	int T = 0;
	int p = 0;
	for(int i = 0; i < n; i++)
	{
		if(bit[p % n])
			break;
		bit[p % n] = 1;
		T++;
		lint sum = 0;
		int l = 0;
		while(l < n && sum + v[p] <= k)
		{
			sum += v[p];
			res += v[p];
			p++;
			l++;
		}
	}
	int s = p % n;
	p = 0;
	lint d = res;
	res = 0;
	while(r && (p % n) != s)
	{
		int l = 0;
		lint sum = 0;
		while(l < n && sum + v[p] <= k)
		{
			sum += v[p];
			res += v[p];
			p++;
			l++;
		}
		T--;
		r--;
	}
	res = res + (d - res) * (r / T);
	r %= T;
	p = s;
	for(int i = 0; i < r; i++)
	{
		lint sum = 0;
		int l = 0;
		while(l < n && sum + v[p] <= k)
		{
			sum += v[p];
			res += v[p];
			p++;
			l++;
		}
	}
	return res;
}

lint solve()
{
	int r, k, n;
	scanf("%d%d%d", &r, &k, &n);
	vi v(n);
	for(int i = 0; i < n; i++)
		scanf("%d", &v[i]);
	vi vvv = v;
	for(int i = 0; i < n; i++)
		v.insert(v.end(), all(vvv));

	int p = 0;

	lint res = 0;
	for(int i = 0; i < r; i++)
	{
		lint sum = 0;
		int l = 0;
		while(l < n && sum + v[p] <= k)
		{
			sum += v[p];
			res += v[p];
			p++;
			if(p == n)
				p = 0;
			l++;
		}
	}
	return res;
}



int Solution(int nTest)
{
	lint res = Solve();
	printf("Case #%d: %lld\n", nTest + 1, res);

	return 1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 9999;
	scanf("%d", &n);
	while(i < n && Solution(i))
		i++;

	return 0;
}