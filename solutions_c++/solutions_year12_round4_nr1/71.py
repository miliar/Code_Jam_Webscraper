#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <ctime>
#include <functional>
#define pb push_back
#define mp make_pair
#define LL long long
#define LD long double
#define INF 1000000000
#define INFll 1000000000000000000ll
#define Vi vector<int>
#define VI Vi::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Si set<int>
#define SI Si::iterator
using namespace std;

int n, d[11111], l[11111], tst, _, f[11111], p;

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> tst;
	while (tst--){
		bool flag = 1;
		cin >> n;
		for (int i = 0; i < n; i++)
			scanf("%d%d", &d[i], &l[i]);

		memset(f, 0, sizeof(f));
		f[0] = d[0] + d[0];
		for (int i = 1; i < n; i++)
			for (int j = 0; j < i; j++)
				if (f[j] >= d[i])
					f[i] = max(f[i], min(d[i] + l[i], d[i] + d[i] - d[j]));
		cin >> p;
		printf("Case #%d: %s\n", ++_, flag && *max_element(f, f + n) >= p ? "YES" : "NO");
	}
}
