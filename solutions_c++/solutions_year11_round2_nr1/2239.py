#include<stdio.h>
#include<string.h>
int a[102][102];
int b[102][4];
char c[102];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large0.out","w",stdout);
	int t,n,i,j,cas=0;
	float w[102][3];
	scanf("%d",&t);
	while(t--)
	{
		cas++;
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		memset(c,0,sizeof(c)); 
		memset(w,0,sizeof(w));
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%s",c);
			//printf("%s",c);
			for(j=0;j<n;j++)
			if(c[j]=='1') 
			{
				a[i][j+1]=1;
				b[i][0]++;
				b[i][1]++;
			}
			else if(c[j]=='0') 
			{
				a[i][j+1]=0;
				b[i][0]++;
			}
			else a[i][j+1]=-1;
			w[i][0]=(float)b[i][1]/b[i][0];	
			//printf("%f ",w[i][0]);
		}	
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			{
				if(j==i || a[j][i]==-1)continue;
				//printf("%d %d \n",b[j][1],b[j][0]);
				if(a[j][i]==1) w[i][1]+=(float)(b[j][1]-1)/(b[j][0]-1);
				else if(a[j][i]==0) w[i][1]+=(float)b[j][1]/(b[j][0]-1);
			}
			w[i][1]/=(float)b[i][0];	
			//printf("%f \n",w[i][1]);		
		}
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			{
				if(j==i) continue;
				if(a[j][i]!=-1)	w[i][2]+=w[j][1];
			}
			w[i][2]/=(float)b[i][0];
			//printf("%f \n",w[i][2]);	
		}
		printf("Case #%d:\n",cas);
		for(i=1;i<=n;i++) 
		{
			//printf("%f %f %f\n",w[i][0],w[i][1],w[i][2]);	
			printf("%f\n",0.25*w[i][0]+0.5*w[i][1]+0.25*w[i][2]);
		}
	}
	return 0;	
}