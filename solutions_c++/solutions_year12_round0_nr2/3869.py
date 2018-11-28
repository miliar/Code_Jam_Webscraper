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
	int T = 0;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		int n, s, p;
		cin >> n >> s >> p;
		int min_s = max(p * 3 - 4, 1), min_ns = p * 3 - 2, res = 0;
		for (int j = 0; j < n; j++)
		{
			int k;
			cin >> k;
			if (k >= min_ns)
				res++;
			else if(k >= min_s && s > 0)
				res++, s--;
		}
		cout << res;
		cout << endl;
	}
	return 0;
}