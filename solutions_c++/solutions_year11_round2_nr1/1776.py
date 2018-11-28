#include <iostream>
#include <stdio.h>
#include <memory.h>
#include <cmath>
using namespace std;

char s[110];
double wp[110],owp[110],oowp[110],ans[110];
int g[110][110];

int main()
{
	freopen("11.in","r",stdin);
	freopen("11.out","w",stdout);
	int t,i,da,ying,now,ren,n,j,cntren,nowren,cnt,kk,ca=0;
	double nwp,yyyy;
	scanf("%d",&t);
	while(t--)
	{
		++ca;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%s",&s[1]);
			da=0; ying=0;
			for(j=1;j<=n;j++)
			{
				if(s[j]=='1') { g[i][j]=1; da++; ying++;}
				else if(s[j]=='0')  { g[i][j]=0; da++; }
				else g[i][j]=-1;
			}
			wp[i]=(double)ying/(double)da;
		}
		for(now=1;now<=n;now++)    // 计算每个人的owp
		{
			ren=0; nwp=0.0;
			for(i=1;i<=n;i++)     
			{
				if(g[now][i]==-1) continue;
				ren++;
				da=0; ying=0;
				for(j=1;j<=n;j++)
				{
					if(j==now||g[i][j]==-1) continue;
					da++;
					if(g[i][j]==1) ying++;
				}
				nwp+=(double)ying/(double)da;
			}
			owp[now]=nwp/ren;
		}
//		for(i=1;i<=n;i++) printf("%.3lf ",wp[i]); printf("\n");
//		for(i=1;i<=n;i++) printf("%.3lf ",owp[i]); printf("\n");
		for(now=1;now<=n;now++)  // 每个人的oowp
		{
			nowren=0;   yyyy=0.0;
			for(cnt=1;cnt<=n;cnt++)
			{
				if(cnt==now) continue;
				//  求cnt不与now打的owp
				if(g[now][cnt]==-1) continue;    // maybe
				nowren++;
				yyyy+=owp[cnt];
			}
			oowp[now]=yyyy/(double)nowren;
			ans[now]=0.25*wp[now]+0.5*owp[now]+0.25*oowp[now];
		}
		printf("Case #%d:\n",ca);
		for(i=1;i<=n;i++)
			printf("%.12lf\n",ans[i]);
	}
	return 0;
}