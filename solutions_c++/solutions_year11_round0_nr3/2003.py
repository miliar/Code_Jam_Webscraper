#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
using namespace std;

int a[2000],tes,n;


int main()
{
	freopen("c.out","w",stdout);
	scanf("%d",&tes);
	for (int ttt=1;ttt<=tes;ttt++)
	{
		scanf("%d",&n);
		for (int i=0;i<n;i++) scanf("%d",&a[i]);
		int x=0;
		for (int i=0;i<n;i++) { x=(x^a[i]); }
		printf("Case #%d: ",ttt);
		if (x) { printf("NO\n"); continue; }
		else
		{
			int mi=a[0],tt=0;
			for (int i=0;i<n;i++) { if (a[i]<mi) mi=a[i]; tt+=a[i]; }
			printf("%d\n",tt-mi);
		}
	}
}
