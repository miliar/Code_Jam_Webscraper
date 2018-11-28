#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#pragma comment(linker, "/STACK:16777216")

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <stack>
#include <set>
#include <queue>
#include <numeric>
#include <algorithm>
#include <utility>
#include <bitset>
#include <cmath>
#include <sstream>

#define all(a) (a).begin(),(a).end()
#define sz(a) (int)(a).size()

using namespace std; 

typedef long long int64;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef vector<double> vd;
typedef vector< vd > vvd;
typedef vector< string > vs;
typedef pair< int, int > pii;
typedef vector< pii > vpii;




int main()
{

	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tc;
	scanf("%d", &tc);
	for (int tn = 0; tn < tc; tn++)
	{
		int r, k, n;
		scanf("%d%d%d", &r, &k, &n);
		vi g(n);
		for (int i = 0; i < n; i++)
			scanf("%d", &g[i]);
		vpii a(n);
		int s = 0, j = 0;
		for (int i = 0; i < n; i++)
		{
			//j = i;
			while (s + g[j] <= k)
			{
				s += g[j];
				j = (j + 1) % n;
				if (j == i) 
					break;
			}
			a[i] = pii(s, j);
			s -= g[i];
		}
		long long res = 0;
		int indx = 0;
		for (int i = 0; i < r; i++)
		{
			res += a[indx].first;
			indx = a[indx].second;
		}
		printf("Case #%d: %lld\n", tn + 1, res);
	}

	return 0;
}