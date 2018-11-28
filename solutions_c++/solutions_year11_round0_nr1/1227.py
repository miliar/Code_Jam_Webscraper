#include <iostream>
#include <string.h>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <algorithm>
#include <math.h>

using namespace std;

int orange[150],blue[150];

int main()
{
	int i,t,n,CurOr,CurBlue,kolOr,kolBlue,NextOr,NextBlue;
	char hlam;
	char a[150];
	freopen("a1.in","r",stdin);
	freopen("a1.out","w",stdout);
	scanf("%d",&t);
	for (int cnt=1;cnt<=t;cnt++)
	{
		kolOr=kolBlue=0;
		scanf("%d%c",&n,&hlam);
		for(i=0;i<n;i++)
		{
			scanf("%c",&a[i]);
			if (a[i]=='O')
				scanf("%d%c",&orange[kolOr++],&hlam);
			else
				scanf("%d%c",&blue[kolBlue++],&hlam);
		}
		NextOr=NextBlue=0;
		CurOr=CurBlue=1;
		i=0;
		int time=0;
		while (i<n)
		{
			if (a[i]=='O')
			{
				if (CurOr==orange[NextOr])
				{
					NextOr++;
					i++;
				}
				else
					if (CurOr>orange[NextOr]) CurOr--;
					else CurOr++;
				if (NextBlue<kolBlue && CurBlue!=blue[NextBlue])
					if (CurBlue>blue[NextBlue]) CurBlue--;
					else CurBlue++;
			}
			else
			{
				if (CurBlue==blue[NextBlue])
				{
					NextBlue++;
					i++;
				}
				else
					if (CurBlue>blue[NextBlue]) CurBlue--;
					else CurBlue++;
				if (NextOr<kolOr && CurOr!=orange[NextOr])
					if (CurOr>orange[NextOr]) CurOr--;
					else CurOr++;
			}
			time++;
		}
		printf("Case #%d: %d\n",cnt,time);
	}
	return 0;
}