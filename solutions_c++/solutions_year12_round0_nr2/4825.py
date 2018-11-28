#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#define INF 100000000

using namespace std;

int n, s, p, p1, p2, ans, ans1;

void check(int x)
{
 	if (x>=p1) ans++;
	else
		if (x>=p2) ans1++;
}

int main(void)
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int curt=0; curt<t; curt++)
	{
		scanf("%d%d%d", &n, &s, &p);
		p1=(p-1)*2 + p;
		if (p==1) p2 = 1;
		else p2=(p-2)*2 + p;
		ans=0; ans1=0;
		for (int i=0; i<n; i++)
		{
			int x;
			scanf("%d", &x);
			check(x);
		}
		if (ans1<s) ans+=ans1;
		else ans+=s;
		printf("Case #%d: %d\n", curt+1, ans);
	}
}