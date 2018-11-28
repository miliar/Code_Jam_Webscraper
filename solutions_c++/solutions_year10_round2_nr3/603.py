#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<utility>
#include<cmath>
#include<string>
using namespace std;

#define llong long long 
const double pi = acos(-1.0);
const int maxInt = 0x7fffffff;
const int minInt = ~maxInt;

const int M = 100003;
const int N = 505;
int d[N][N],zh[N][N];

int main(){
	freopen("C-small-attempt2.in","r",stdin);freopen("out.txt","w",stdout);
    int i,j,k,t,nc = 0;
	scanf("%d",&t);
	memset(d,0,sizeof(d));
	d[2][1] = 1;
	for(i = 0;i<N;i++){
		zh[0][i] = 0;
		zh[i][0] = 1;
	}
	for(i = 1;i<N;i++){
		for(j = 1;j<N;j++){
			zh[i][j] = zh[i-1][j]+zh[i-1][j-1];
			zh[i][j] %= M;
		}
	}
	for(i = 3;i<N;i++){
		for(j = 1;j<i;j++){
			if(j==1)d[i][j] = 1;
			else{
				for(k = 1;k<j;k++){
					d[i][j] += d[j][k]*zh[i-j-1][j-k-1]%M;
				}
			}
		}
	}
	while(t--){
		int n;
		scanf("%d",&n);
		int ans = 0;
		for(i = 1;i<n;i++){
			ans = (ans+d[n][i])%M;
		}
		printf("Case #%d: %d\n",++nc,ans);
	}
    return 0;
}