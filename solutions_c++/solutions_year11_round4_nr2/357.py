#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int val[505][505];
char mp[505][505];
long long sum1[505][505];
long long sum2[505][505];
int R,C,D;

int fcmp(double a,double b)
{
	if(fabs(a-b)<1E-9) return 0;
	if(a>b) return 1;
	return -1;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("lowesy_B.out","w",stdout);
	int _,cases=1;
	scanf("%d",&_);
	int i,j,K,r,c;
	double s;
	while(_--)
	{
		scanf("%d%d%d",&R,&C,&D);
		for(i=0;i<R;i++)
			scanf("%s",mp[i]);
		if(R<3||C<3)
		{
			printf("Case #%d: IMPOSSIBLE\n",cases++);
			continue;
		}
		for(i=0;i<R;i++)
			for(j=0;j<C;j++)
				val[i][j]=mp[i][j]-'0'+D;
		for(i=0;i<R;i++)
		{
			sum1[i][0]=val[i][0];
			for(j=1;j<C;j++)
				sum1[i][j]=sum1[i][j-1]+val[i][j];
		}
		for(i=0;i<C;i++)
		{
			sum2[0][i]=val[0][i];
			for(j=1;j<R;j++)
				sum2[j][i]=sum2[j-1][i]+val[j][i];
		}
		int res=-1;
		for(K=min(R,C);K>=3&&res==-1;K--)
		{
			for(i=0;i+K<=R;i++)
			{
				for(j=0;j+K<=C;j++)
				{
					s=0.0;
					s+=(0.5-K/2.0)*(sum1[i][j+K-2]-sum1[i][j]);
					s+=(K-0.5-K/2.0)*(sum1[i+K-1][j+K-2]-sum1[i+K-1][j]);
					for(r=i+1;r<i+K-1;r++)
					{
						if(!j) s+=(r-i+0.5-K/2.0)*sum1[r][j+K-1];
						else s+=(r-i+0.5-K/2.0)*(sum1[r][j+K-1]-sum1[r][j-1]);
					}
					if(fcmp(s,0.0)!=0) continue;
					s=0.0;
					s+=(0.5-K/2.0)*(sum2[i+K-2][j]-sum2[i][j]);
					s+=(K-0.5-K/2.0)*(sum2[i+K-2][j+K-1]-sum2[i][j+K-1]);
					for(c=j+1;c<j+K-1;c++)
					{
						if(!i) s+=(c-j+0.5-K/2.0)*sum2[i+K-1][c];
						else s+=(c-j+0.5-K/2.0)*(sum2[i+K-1][c]-sum2[i-1][c]);
					}
					if(fcmp(s,0.0)==0) { res=K; break; }
				}
				if(res!=-1) break;
			}
		}
		printf("Case #%d: ",cases++);
		if(res==-1) puts("IMPOSSIBLE");
		else printf("%d\n",res);
	}
	return 0;
}