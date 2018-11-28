#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
using namespace std;
long long f[20][4000][20];
int pr[10][2000];
int M[2000],p;
long long dp(int i,int j,int k){
	if(f[i][j][k]!=-1)return f[i][j][k];
	if(i==p){
		if(M[j]>=k)return f[i][j][k]=0;
		else return f[i][j][k]=10000000000LL;
	}
	return f[i][j][k]=min(pr[i][j]+dp(i+1,2*j,k)+dp(i+1,2*j+1,k),dp(i+1,2*j,k+1)+dp(i+1,2*j+1,k+1));
}
int main(){
	int times;
	scanf("%d",&times);
	for(int tm=1;tm<=times;tm++){
		printf("Case #%d: ",tm);
		scanf("%d",&p);
		for(int i=0;i<(1<<p);i++){
			scanf("%d",&M[i]);
		}
		for(int i=p-1;i>=0;i--)
			for(int j=0;j<(1<<i);j++){
				scanf("%d",&pr[i][j]);
			}
		memset(f,-1,sizeof(f));
		cout<<dp(0,0,0)<<endl;
	}
	return 0;
}
