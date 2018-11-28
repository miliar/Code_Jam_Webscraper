#include<iostream>
using namespace std;
char g[110][110],map[110][110];
int flagB,flagR,cn,n,k;
void solve()
{
	int cnt,num;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			if(map[i][j]!='.')
			{
				if(map[i][j]=='B' && flagB==0) 
				{
					cnt=1;num=1;
					while(map[i][j+cnt]=='B' && j+cnt<=n){	
						cnt++;num++;
						if(num>=k) flagB=1;
					}
					cnt=1;num=1;
					while(map[i+cnt][j]=='B' && i+cnt<=n){
						cnt++;num++;
						if(num>=k) flagB=1;
					}
					cnt=1;num=1;
					while(map[i-cnt][j+cnt]=='B' && i-cnt>=1 && j+cnt<=n){cnt++;num++;
						if(num>=k) flagB=1;
						
					}
					 cnt=1;num=1;
					while(map[i+cnt][j+cnt]=='B' && i+cnt<=n && j+cnt<=n){	cnt++;num++;
						if(num>=k) flagB=1;
					
					}
				} 
				else if(map[i][j]=='R' && flagR==0) 
				{
					 cnt=1;num=1;
					while(map[i][j+cnt]=='R' && j+cnt<=n){
						cnt++;num++;
						if(num>=k) flagR=1;
						
					}
					int cnt=1;num=1;
					while(map[i+cnt][j]=='R' && i+cnt<=n){
						cnt++;num++;
						if(num>=k) flagR=1;
						
					}
					cnt=1;num=1;
					while(map[i-cnt][j+cnt]=='R' && i-cnt>=1 && j+cnt<=n){cnt++;num++;
						if(num>=k) flagR=1;
						
					}
				    cnt=1;num=1;
					while(map[i+cnt][j+cnt]=='R' && i+cnt<=n && j+cnt<=n){	cnt++;num++;
						if(num>=k) flagR=1;
					
					}
				} 
			}
			cn++;
		if(flagR && flagB) printf("Case #%d: Both\n",cn);
		else if(flagR && !flagB) printf("Case #%d: Red\n",cn);
		else if(!flagR && flagB) printf("Case #%d: Blue\n",cn);
		else if(!flagR && !flagB) printf("Case #%d: Neither\n",cn);
		
}
int main()
{
	freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\A-large.out","w",stdout);
	int T,cn=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&n,&k);
		for(int i=1;i<=n;i++) 
		{
			for(int j=1;j<=n;j++)
				cin>>g[i][j];
		}
		for(int i=1;i<=n;i++)
			for(int j=n;j>=1;j--)
				for(int m=j-1;m>=1;m--)
					if(g[i][j]=='.' && g[i][m]!='.')
					{
						char ch;
						ch=g[i][j];g[i][j]=g[i][m];g[i][m]=ch;
					}
		/*for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=n;j++)
				cout<<g[i][j];
			cout<<endl;
		}*/
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				map[i][j]=g[n-j+1][i];
	/*	for(int i=1;i<=n;i++,printf("\n"))
			for(int j=1;j<=n;j++)
				printf("%c",map[i][j]);*/
		flagB=0,flagR=0;
		solve();
	}
	return 7;
}