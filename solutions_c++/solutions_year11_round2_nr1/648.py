#include<stdio.h>
char _node[101][101];
double wp[105],owp[105],oowp[105],ans[105];
int main()
{
	int cas,n,i,j,k,cnt1,cnt,t;
	//freopen("Al.in","r",stdin);
	//freopen("2.txt","w",stdout);
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++)
	{
		printf("Case #%d:\n",ii);
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s",_node[i]);
		for(i=0;i<n;i++)
		{
			cnt1=cnt=0;
			for(j=0;j<n;j++)
				if(_node[i][j]!='.')
				{
					cnt++;
					if(_node[i][j]=='1')
						cnt1++;
					wp[i]=1.0*cnt1/cnt;
				}
		}
		for(i=0;i<n;i++)
		{
			t=0;
			owp[i]=0;
			for(j=0;j<n;j++)
				if(_node[i][j]!='.')
				{
					t++;
					cnt1=cnt=0;
					for(k=0;k<n;k++)
						if(k!=i&&_node[j][k]!='.')
						{
							cnt++;
							if(_node[j][k]=='1')
								cnt1++;
						}
					owp[i]+=1.0*cnt1/cnt;
				}
			owp[i]/=t;
		}
		for(i=0;i<n;i++)
		{
			oowp[i]=0;cnt=0;
			for(j=0;j<n;j++)
				if(_node[i][j]!='.')
				{
					oowp[i]+=owp[j];
					cnt++;
				}
			oowp[i]/=cnt;
		}
		for(i=0;i<n;i++)
		{
			ans[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
			printf("%.9lf\n",ans[i]);
		}
	}
	return 0;
}