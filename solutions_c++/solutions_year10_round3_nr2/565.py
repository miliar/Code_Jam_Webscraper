#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>

#define maxn 2000
#define maxC 1000000000

using namespace std;

int test,n,l,p,c;
int dp[maxn][maxn];
int cut[maxn][maxn];

void dynamic_programming(){
	int i,j,v,t1,t2;
	n=p;
	for (j=1;j<=n;j++)
		for (i=j;i>=1;i--)
			if (j<=i*c){
				dp[i][j]=0;
				cut[i][j]=i;
			}
		else{
			dp[i][j]=maxC;
			t1=min(cut[i+1][j],cut[i][j-1]);
			t2=max(cut[i+1][j],cut[i][j-1]);
			for (v=t1;v<=t2;v++)
				if (dp[i][j]>max(dp[i][v],dp[v][j])+1){
					dp[i][j]=max(dp[i][v],dp[v][j])+1;
					cut[i][j]=v;
				}
		}
}

int main(){
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>test;
	int i;
	for (i=1;i<=test;i++){
		cin>>l>>p>>c;
		dynamic_programming();
		cout<<"Case #"<<i<<": "<<dp[l][p]<<"\n";
	}
}
