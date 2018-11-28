#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
using namespace std;
#define MAX 400
bool is[MAX][MAX];
int main()
{
	int cs,r,x1,x2,y1,y2,dd,i,j,ans,cnt;
	scanf("%d",&cs);
	for(dd=1;dd<=cs;dd++)
	{
		memset(is,0,sizeof(is));
		scanf("%d",&r);
		while(r--)
		{
			scanf("%d%d",&x1,&y1);
			scanf("%d%d",&x2,&y2);
			for(i=x1;i<=x2;i++)
				for(j=y1;j<=y2;j++)
					is[i][j]=true;
		}
		for(ans=0;;ans++)
		{
			for(cnt=0,i=MAX-1;i>0;i--)
				for(j=MAX-1;j>0;j--)
				{
					if(is[i][j])
						cnt++;
					if(is[i-1][j]&&is[i][j-1])
						is[i][j]=true;
					else if(!is[i-1][j]&&!is[i][j-1])
						is[i][j]=false;
				}
			if(cnt==0)
				break;
		}
		printf("Case #%d: %d\n",dd,ans);
	}
}