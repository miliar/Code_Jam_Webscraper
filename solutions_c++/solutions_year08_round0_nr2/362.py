#include<stdio.h>

int Q,i,j,k,hh,mm;
int dep[3][200],arr[3][200],done[3][200];
int ks,T,N[3];
char time1[100],time2[200];
int temp,ok,nside;
int cnt,curtime,side,id;
int ans[3];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	scanf("%d",&Q);

	for(ks=1;ks<=Q;ks++)
	{
		scanf("%d",&T);
		scanf("%d%d",&N[0],&N[1]);

		for(j=0;j<2;j++)
		{
			for(i=1;i<=N[j];i++)
			{
				scanf("%s%s",time1,time2);
				sscanf(time1,"%2d:%2d",&hh,&mm);
				dep[j][i]=hh*60+mm;
				sscanf(time2,"%2d:%2d",&hh,&mm);
				arr[j][i]=hh*60+mm;
				done[j][i]=0;
			}

			for(i=1;i<=N[j];i++)
				for(k=i+1;k<=N[j];k++)
					if(dep[j][i]>dep[j][k] || (dep[j][i]==dep[j][k] && arr[j][i]>arr[j][k]))
					{
						temp=dep[j][i];
						dep[j][i]=dep[j][k];
						dep[j][k]=temp;
						temp=arr[j][i];
						arr[j][i]=arr[j][k];
						arr[j][k]=temp;
					}
		}

		ans[0]=ans[1]=0;
		cnt=0;
		while(cnt!=N[0]+N[1])
		{
			curtime=1000000000;
			for(j=0;j<2;j++)
				for(i=1;i<=N[j];i++)
					if(done[j][i]==0 && curtime > dep[j][i])
					{
						curtime=dep[j][i];
						id=i;
						side=j;
					}

			ans[side]++;
			cnt++;
			done[side][id]=1;
			curtime=arr[side][id];
			ok=1;
			while(ok)
			{
				ok=0;
				nside=1-side;
				for(i=1;i<=N[nside];i++)
					if(done[nside][i]==0 && dep[nside][i]>=curtime+T)
					{
						cnt++;
						ok=1;
						done[nside][i]=1;
						curtime=arr[nside][i];
						side=nside;
						break;
					}
			}
		}

		printf("Case #%d: %d %d\n",ks,ans[0],ans[1]);
	}

	return 0;
}