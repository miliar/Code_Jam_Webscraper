#include <iostream>
#include <cstdio>
using namespace std;

int dp[1000][1000],mat[1000][1000];

#define M 10007

int main(){
	int i,j,t,u,h,w,r,a,b;
	cin>>t;
	for (u=0; u<t; u++){
		cin>>h>>w>>r;
		for (i=0; i<h; i++){
			for (j=0; j<w; j++){
				dp[i][j]=mat[i][j]=0;
			}
		}
		for (i=0; i<r; i++){
			cin>>a>>b;
			mat[a-1][b-1]=1;
		}
		dp[0][0]=1;
		for (i=1; i<h; i++){
			for (j=1; j<w; j++){
				if (mat[i][j]==1)
					dp[i][j]=0;
				else{
					dp[i][j]=0;
					if (j>=2) dp[i][j]+=dp[i-1][j-2];
					if (i>=2) dp[i][j]+=dp[i-2][j-1];
					dp[i][j]%=M;
				}
			}
		}
		cout<<"Case #"<<(u+1)<<": "<<(dp[h-1][w-1]%M)<<endl;
	}
	return 0;
}
