#include <iostream>
using namespace std;

int a[111][111],b[111][111];

int main()
{
	int t;
	freopen("in.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	scanf("%d",&t);
	for (int i=0;i<t;i++)
	{
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		int r;
		scanf("%d",&r);
		for (int j=0;j<r;j++)
		{
			int x1,x2,y1,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (int h=x1;h<=x2;h++)
				for (int g=y1;g<=y2;g++)
					a[h][g]=1;
		}
		int res=0;
		int ex=1;
		for (;ex;)
		{
			res++;
			ex=0;
			for (int g=1;g<=100;g++)
				for (int h=1;h<=100;h++)
					if (a[h][g])
					{
						if (!a[h-1][g]&&!a[h][g-1])
							b[h][g]=0;
						else
						{
							ex=1;
							b[h][g]=1;
						}
					}
					else
					{
						if (a[h-1][g]&&a[h][g-1])
						{
							b[h][g]=1;
							ex=1;
						}
					}
			for (int j=1;j<=100;j++)
				for (int h=1;h<=100;h++)
				{
					a[j][h]=b[j][h];
					b[j][h]=0;
				}
		}
		printf("Case #%d: %d\n",i+1,res);
	}
	return 0;
}