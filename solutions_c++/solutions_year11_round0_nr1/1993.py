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

int n,x;
char ch[20];

int ab(int x) { if (x<0) return -x; else return x; }

int main()
{
	freopen("a.out","w",stdout);
	int tes;
	scanf("%d",&tes);
	for (int ttt=1;ttt<=tes;ttt++)
	{
		scanf("%d",&n);
		int lpO=1,lpB=1,ltO=0,ltB=0,t=0;
		for (int i=1;i<=n;i++)
		{
			scanf("%s",ch);
			scanf("%d",&x);
			if (ch[0]=='O')
			{
				if (ab(x-lpO)+ltO>t) t=ab(x-lpO)+ltO;
				t++; lpO=x; ltO=t;
			}
			else
			{
				if (ab(x-lpB)+ltB>t) t=ab(x-lpB)+ltB;
				t++; lpB=x; ltB=t;
			}
		//	printf("%d\n",t);
		}
		printf("Case #%d: %d\n",ttt,t);
	}
	return 0;
}
