#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
char cell[2][500][500];
int mx,my;
int solve()
{
	int ans=0,k=0;
	while(1)
	{
		char flag=0;
		for(int i=0;i<=mx;i++)
			for(int j=0;j<=my;j++)
			{
				if(cell[k][i][j]==0)
				{
					if(j-1>=0 && i-1>=0 && cell[k][i][j-1] && cell[k][i-1][j]){
						cell[!k][i][j]=1;
						flag=1;
					}
					else
						cell[!k][i][j]=0;
				}else
				{
					if((j-1<0 || (j-1>=0 && cell[k][i][j-1]==0)) && (i-1<0 || (i-1>=0 && cell[k][i-1][j]==0)))
						cell[!k][i][j]=0;
					else{
						cell[!k][i][j]=1;flag=1;
					}
				}
			}
		ans++;k=!k;
		if(!flag) break;
	}
	return ans;
}
int main()
{
	int c;
	scanf("%d",&c);
	for(int cas=1;cas<=c;cas++)
	{
		int r;
		scanf("%d",&r);
		memset(cell[0],0,sizeof(cell[0]));
		int i,j,k;
		mx=my=-1;
		for(i=1;i<=r;i++)
		{
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			if(x2>mx) mx=x2;
			if(y2>my) my=y2;
			for(j=x1;j<=x2;j++)
				for(k=y1;k<=y2;k++)
					cell[0][j][k]=1;
		}
		int ans=solve();
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}

