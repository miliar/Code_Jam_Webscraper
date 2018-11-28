#include <cstdio>
#include <string>
using namespace std;

int n,m;
string a[100],b[1000];
int c[1000],k;
int dp[1000][100];

char buf[105];
string read() {
	char c;
	int poz=0;
	while(1) {
		c=getchar();
		if(c=='\n') {
			buf[poz]=0;
			return buf;
		}
		buf[poz++]=c;
	}
}

int main() {
	int t;
	scanf("%d",&t);
	for(int cnt=1; cnt<=t; ++cnt) {
		scanf("%d",&n);
		getchar();
		k=0;
		for(int i=0; i<n; ++i) a[i]=read();
		scanf("%d",&m);
		getchar();
		for(int i=0; i<m; ++i) b[i]=read();
		for(int i=0; i<m; ++i)
			for(int j=0; j<n; ++j)
				if(b[i]==a[j])
					c[k++]=j;
		m=k;
		for(int i=0; i<n; ++i)
			if(c[0]==i)
				dp[0][i]=1000000000;
			else
				dp[0][i]=0;
		for(int i=1; i<m; ++i)
			for(int j=0; j<n; ++j) {
				dp[i][j]=1000000000;
				if(c[i]==j) continue;
				dp[i][j]=min(dp[i][j],dp[i-1][j]);
				for(int k=0; k<n; ++k) dp[i][j]=min(dp[i][j],dp[i-1][k]+1);
			}
		int res=1000000000;
		for(int i=0; i<n; ++i) res=min(res,dp[m-1][i]);
		printf("Case #%d: %d\n",cnt,res);
	}
	return 0;
}
