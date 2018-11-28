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
	freopen("A-large2.in", "r", stdin);
	freopen("A-large2.out", "w+", stdout);
	int t;
	cin >> t;
	for(int l=1; l<=t; l++)
	{
		int n, p;
		int o=1, b=1;
		int to=0, tb=0, r;
		char col;
		scanf("%d", &n);
		FOR(i, 0, n)
		{
			scanf(" %c %d", &col, &p);
			if(col=='O')
			{
				r=abs(p-o)+1;
				o=p;
				to=max(to+r, tb+1);
			}
			else
			{
				r=abs(p-b)+1;
				b=p;
				tb=max(to+1, tb+r);
			}
		}
		printf("Case #%d: %d\n", l, max(to, tb));
	}
	return 0;freopen("input.in", "r", stdin);
}
