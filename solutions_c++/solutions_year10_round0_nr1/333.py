#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <queue>
#include <bitset>
//#include <cmath>
#include <sstream>
#include <string>
#include <vector>

#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T x) {return x > 0 ? x : (-x); }
template<class T> T sqr(T x) {return x * x; }

bool a[100];

bitset<100 * 1000 * 1000 + 10> d[31];

void Solve0(int n, int k)
{
	cerr << n << "\n";
	memset(a, 0, sizeof(a));
	d[n][0] = 0;
	for (int i = 0; i < k; i++)
	{
		bool ok = false;
		for (int j = 0; j < n; j++)
		{
			a[j] = !a[j];
			if (a[j]) break;
			if (j == n - 1)
				ok = true;
		}
		d[n][i] = ok;
	}
}

void Solve()
{
	int n, k;
	cin >> n >> k;
	bool ok = d[n][k];
	printf("%s\n", ok ? "ON" : "OFF");
}

int main()
{

	for (int i = 1; i <= 30; i++)
		Solve0(i, 100 * 1000 * 1000);
	int nc;
	cin >> nc;
	for (int it = 0; it < nc; it++)
	{
		printf("Case #%d: ", it + 1);
		Solve();
	}
	return 0;
}
