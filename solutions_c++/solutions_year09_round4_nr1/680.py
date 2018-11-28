#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
using namespace std;

#define ALL(ar)       (ar).begin(),(ar).end()
#define SZ(a)         int((a).size())
#define MP(a,b)       make_pair(a,b)
#define INF           0x7f7f7f7f
typedef long long     LL;
typedef vector<int>   VI;
typedef pair<int,int> II;

int TC, N;

int main()
{
    freopen("in.in", "rt", stdin);
	freopen("out.out", "wt", stdout);

	scanf ("%d", &TC);
	for (int tc = 0; tc < TC; tc++)
	{
		scanf ("%d", &N);
		VI x;
		string s;
		for (int i = 0; i < N; i++) {
			cin >> s;
			int one = -1;
			for (int j = N-1; j >= 0; j--)
				if (s[j] == '1') {
					one = j;
					break;
				}
			x.push_back (one);
		}

		LL ans = 0;
		for (int i = 0; i < N; i++) {
			int k = 0;
			if (x[i] <= i) continue;
			for (int j = i+1; j < N; j++)
				if (x[j] <= i) {
					ans += j-i;
					int v = x[j];
					x.erase (x.begin()+j);
					x.insert (x.begin()+i, v);
					break;
				}
		}
		printf ("Case #%d: %I64d\n", tc+1, ans);
	}

	return 0;
}