#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>

#define FOR(i, s, e) for(int i=s; i<e; i++)
#define INP(arr) for(int i=0; i<arr.size(); i++) cin >> arr[i];

using namespace std;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w+", stdout);
	int t, n;
	int cmin, s, flag, x;
	cin >> t;
	for(int l=1; l<=t; l++)
	{
		cin >> n;
		cin >> cmin;
		s=cmin;
		flag=cmin;
		for(int i=1; i<n; i++)
		{
			cin >> x;
			s+=x;
			if(x<cmin) cmin=x;
			flag^=x;
		}
		printf("Case #%d: ", l);
		if(flag) printf("NO\n", flag);
		else printf("%d\n", s-cmin);
	}
	return 0;
}
