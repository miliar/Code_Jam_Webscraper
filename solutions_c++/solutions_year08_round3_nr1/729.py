#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <iterator>
#include <numeric>
#include <utility>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <fstream>
#include <string>
using namespace std;

#define FOR(n)		for(int _i=0, _n=n; _i<_n; _i++)

#define sqr(x)		((x)*(x))

int main()
{
	int N=0;
	scanf("%d", &N);

	for(int j=1; j<=N; j++)
	{
		int P, K, L;
		scanf("%d %d %d", &P, &K, &L);

		vector<int> v(L);
		for(int i=0; i<L; i++) scanf("%d", &v[i]);

		sort(v.begin(), v.end(), greater<int>());

		int R=0;
		for(int i=0; i<L; i++) R+=v[i]*(i/K+1);

		printf("Case #%d: %d\n", j, R);
	}

	return 1;
}
