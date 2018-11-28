#include<iostream>
using namespace std;
const int maxn=50002;
const int maxk=16;

int sum,k,t,ca;
int cost[maxk][maxk],f[maxk][maxk][1<<maxk];
char s[maxn];
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&ca);
	for (int t=1;t<=ca;t++){
		scanf("%d",&k);
		scanf("%s",s);
		int n=strlen(s);
		int d=n/k;

		memset(cost,0,sizeof(cost));
		for (int i=0;i<k;i++)
			for (int j=0;j<k;j++)
				for (int a=0;a<d;a++)
					cost[i][j]+=s[a*k+i]!=s[a*k+j];

		memset(f,22,sizeof(f));
		for (int a=0;a<(1<<k);a++)
			for (int i=0;i<k;i++)
				for (int j=0;j<k;j++){
					if(i==j||a&(1<<i)||a&(1<<j))
						continue;
					if(a==0){
						f[i][j][a]=cost[i][j];
						continue;
					}
					for (int b=0;b<k;b++)
						if(a&(1<<b))
							if(f[i][j][a]>f[i][b][a-(1<<b)]+cost[b][j])
								f[i][j][a]=f[i][b][a-(1<<b)]+cost[b][j];
				}

		int ans=n;
		for (int i=0;i<k;i++)
			for (int j=0;j<k;j++){
				if(i==j)
					continue;
				sum=f[i][j][(1<<k)-1-(1<<i)-(1<<j)];
				for (int a=1;a<d;a++)
					sum+=s[a*k+i]!=s[(a-1)*k+j];
				if(sum<ans)
					ans=sum;
			}
		printf("Case #%d: %d\n",t,ans+1);
	}
	return 0;
}