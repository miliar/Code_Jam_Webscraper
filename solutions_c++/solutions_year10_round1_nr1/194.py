#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

long t,k,n;
char c[61][61];
char d[61][61];
char e[61][61];
long f[61][61],g[61][61],q[61][61],p[61][61];

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	long h,i,j,l,ans;
	scanf("%ld",&t);
	for(h=1;h<=t;h++){
		memset(c,0,sizeof(c));
		memset(d,0,sizeof(d));
		memset(e,0,sizeof(e));
		memset(f,0,sizeof(f));
		memset(g,0,sizeof(g));
		memset(q,0,sizeof(q));
		memset(p,0,sizeof(p));
		scanf("%ld%ld",&n,&k);
		for(i=0;i<n;i++)
			scanf("%s",c[i]);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				d[j][n-i-1]	= c[i][j];
		for(j=0;j<n;j++){
			l=n;
			for(i=n-1;i>=0;i--){
				if(d[i][j]!='.')e[--l][j]=d[i][j];
			}
		}
		ans=0;
		for(i=0;i<n;i++)
			for(j=0;j<n;j++){
				if(i==0)f[i][j]=1;
				else f[i][j]=(e[i-1][j]==e[i][j]?f[i-1][j]+1:1);
				if(j==0)q[i][j]=1;
				else q[i][j]=(e[i][j-1]==e[i][j]?q[i][j-1]+1:1);
				if(i==0 || j==0)g[i][j]=1;
				else g[i][j]=(e[i-1][j-1]==e[i][j]?g[i-1][j-1]+1:1);
				if(f[i][j]>=k || q[i][j]>=k || g[i][j]>=k){
					if(e[i][j]=='R')ans|=1;
					else if(e[i][j]=='B') ans|=2;
				}
			}
		for(i=0;i<n;i++)
			for(j=n-1;j>=0;j--){
				if(j==n-1 || i==0)p[i][j]=1;
				else{
					p[i][j]=(e[i-1][j+1]==e[i][j]?p[i-1][j+1]+1:1);
					if(p[i][j]>=k){
						if(e[i][j]=='R')ans|=1;
						else if(e[i][j]=='B') ans|=2;
					}
				}
			}
		printf("Case #%ld: ",h);
		if(ans==0)printf("Neither\n");
		else if(ans==1)printf("Red\n");
		else if(ans==2)printf("Blue\n");
		else printf("Both\n");
	}
	return 0;
}
