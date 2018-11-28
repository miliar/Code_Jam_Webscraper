#include <stdio.h>

int T;
int R;
bool a[101][101];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	int t;
	for (t=1;t<=T;t++)
	{
		scanf("%d",&R);
		int i;
		int cnt=0;
		int y,x;
		for (i=1;i<=R;i++)
		{
			int x1,y1,x2,y2;
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			if (y2>y) y=y2;
			if (x2>x) x=x2;
			int p,q;
			for (p=y1;p<=y2;p++)
				for (q=x1;q<=x2;q++)
				{
					if (!a[p][q]) cnt++;
					a[p][q]=1;
				}	
		}
		
		int r=0;
		while (cnt)
		{
			int j;
			for (i=y;i>=1;i--)
			{
				for (j=x;j>=1;j--)
				{
					if (a[i][j])
					{
						if ((i-1<1||a[i-1][j]==0)&&(j-1<1||a[i][j-1]==0))
						{
							cnt--;
							a[i][j]=0;
						}
					}
					else
					{
						if (i-1>=1&&a[i-1][j]==1&&j-1>=1&&a[i][j-1]==1)
						{
							cnt++;
							a[i][j]=1;
						}
					}
				}
			}
			r++;
		}
		
		printf("Case #%d: %d\n",t,r);
	}

	return 0;
}