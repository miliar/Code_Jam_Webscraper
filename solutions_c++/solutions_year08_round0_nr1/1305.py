#include<iostream>
using namespace std;

int n,m,tc,x,i,j,k,sedikit;
string engine[105];
string queri[1005];
int dp[1005][105];
char st[1000000];

int main() {
	freopen("univ.out","w",stdout);
	freopen("univ.in","r",stdin);
	cin>>tc;
	for(x=1;x<=tc;x++) {
		cout<<"Case #"<<x<<": ";
		cin>>n;
		//cout<<"n: "<<n<<endl;
		getchar();
		for(i=0;i<n;i++) {
			gets(st);
			engine[i]=st;
		}
		cin>>m;
		getchar();
		for(i=0;i<m;i++) {
			gets(st);
			queri[i]=st;
		}
		if(m==0) {
			cout<<0<<endl;
			continue;
		}
		for(i=0;i<=m;i++) {
			for(j=0;j<=n;j++) dp[i][j]=1000000000;
		}
		for(i=0;i<n;i++) {
			if(engine[i]!=queri[0]) dp[0][i]=0;
		}
		for(i=1;i<m;i++) {
			for(j=0;j<n;j++) {
				if(engine[j]==queri[i]) {
					dp[i][j]=1000000000;
					continue;
				}
				dp[i][j]=dp[i-1][j];
				for(k=0;k<n;k++) {
					dp[i][j]=min(dp[i][j],1+dp[i-1][k]);
				}
			}
		}
		//cout<<"dp: "<<endl;
		//for(i=0;i<m;i++) {
			//for(j=0;j<n;j++) cout<<dp[i][j]<<" ";
			//cout<<endl;
		//}
		sedikit=1000000000;
		for(i=0;i<n;i++) sedikit=min(sedikit,dp[m-1][i]);
		cout<<sedikit<<endl;
	}
	fclose(stdout);
	fclose(stdin);
}
