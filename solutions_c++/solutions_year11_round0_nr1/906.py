#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input2.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T, tt;
	scanf("%d", &T);
	for (tt=0; tt<T; ++tt)
	{
		int n, i;
		scanf("%d ", &n);
		int t1=0, t2=0;
		int p1=1, p2=1;
		int curt=0;
		for (i=0; i<n; ++i)
		{
			char c;
			int x;
			scanf("%c %d ", &c, &x);
			if (c=='O')
			{
				t1=max(t1+abs(x-p1), curt)+1;
				curt=t1;
				p1=x;
			}
			else
			{
				t2=max(t2+abs(x-p2), curt)+1;
				curt=t2;
				p2=x;
			}
		}
		printf("Case #%d: ", tt+1);
		printf("%d\n", curt);
	}
	return 0;
}