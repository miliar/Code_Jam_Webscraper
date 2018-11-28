#include<iostream>
#include<algorithm>
#include<cstdio>
#include<string>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
int f[510][21],t1=1,tt,n;
string par,s;

int main(){
	freopen("cl.in","r",stdin);
	freopen("c.out","w",stdout);
	par="welcome to code jam";
	for(scanf("%d\n",&tt);t1<=tt;t1++){
		getline(cin,s);
		n=s.size();s+=' ';
		for(int i=n;i>=1;i--)s[i]=s[i-1];
		fo(i,0,19)f[0][i]=0;
		fo(i,1,n){
			f[i][0]=f[i-1][0]+(s[i]==par[0]);
			fo(j,1,18)
				f[i][j]=(f[i-1][j]+f[i-1][j-1]*(s[i]==par[j]))%10000;
		}
		int ans=f[n][18];
		printf("Case #%d: %d%d%d%d\n",t1,ans/1000,ans%1000/100,ans%100/10,ans%10);
	}
	return 0;
}
			
