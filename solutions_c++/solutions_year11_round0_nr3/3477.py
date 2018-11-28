#include <algorithm>
#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <memory.h>
#include <numeric>

#define REP(k, n) for(int k=0; k<(int)(n); ++ k)

using namespace std;

#define INFILE "C-large"

int go(vector<int> &x)
{
	return accumulate(x.begin(), x.end(), 0) - *min_element(x.begin(), x.end());
}

int main()
{
	freopen(INFILE".in", "r", stdin);
	freopen(INFILE".out", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int tt=1; tt<=T; ++ tt)
	{
		int n;
		scanf("%d", &n);
		vector<int> a;

		int XOR = 0;
		for(int q=0; q<n; ++q) {
			int x; scanf("%d", &x);
			a.push_back(x);
			XOR ^= x;
		}
		printf("Case #%d: ", tt);
		if(XOR != 0) printf("NO\n");
		else printf("%d\n", go(a));
	}
	return 0;
}