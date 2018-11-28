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
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int tn = 0; tn < t; tn++)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		bool ok = true;
		for (int i = 0, p2 = 1; i < n; i++, p2 <<= 1)
		{
			if (!(p2 & k))
			{
				ok = false;
				break;
			}
		}
		printf("Case #%d: %s\n", tn + 1, ((ok)?"ON":"OFF"));
	}

	return 0;
}