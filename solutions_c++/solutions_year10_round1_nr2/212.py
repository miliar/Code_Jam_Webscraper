#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;


const int oo=(int)1e9;
void opens(){
	freopen("Bsmall.in","r",stdin);
	freopen("Bsmall.out","w",stdout);
}

void openb(){
	freopen("Blarge.in","r",stdin);
	freopen("Blarge.out","w",stdout);
}
int t,xx,D,I,M,n,a[101],f[101][300],need[300][300],ans;

int dp(int x,int y){
	if (x==n) return 0;
	if (y!=-1 && f[x][y]!=-1) return f[x][y];
	int res=oo;
	if (y==-1 || abs(y-a[x])<=M){
		res=min(res,dp(x+1,a[x]));
	}
	else{
		if (res>need[y][a[x]]){
			res=min(res,dp(x+1,a[x])+need[y][a[x]]);
		}
	}
	if (res>D){
		res=min(res,dp(x+1,y)+D);
	}
	for (int i=1;i<=a[x];i++){
		if (i>=res) continue;
		if (y==-1 || abs(y-(a[x]-i))<=M){
			res=min(res,dp(x+1,a[x]-i)+i);
		}
		else {
			if (need[y][a[x]-i]+i>=res) continue;
			res=min(res,dp(x+1,a[x]-i)+i+need[y][a[x]-i]);
		}
	}
	for (int i=1;i<=255-a[x];i++){
		if (i>=res) continue;
		if (y==-1 || abs(y-(a[x]+i))<=M){
			res=min(res,dp(x+1,a[x]+i)+i);
		}
		else {
			if (need[y][a[x]+i]+i>=res) continue;
			res=min(res,dp(x+1,a[x]+i)+i+need[y][a[x]+i]);
		}
	}
	return f[x][y]=res;
}

int main(){
	//opens();
	openb();
	scanf("%d",&t);
	xx=1;
	while (t--){
		scanf("%d%d%d%d",&D,&I,&M,&n);
		for (int i=0;i<n;i++){
			scanf("%d",&a[i]);
		}
		for (int i=0;i<=255;i++){
			need[i][i]=0;
			for (int j=i+1;j<=255;j++){
				if (M==0){
					need[i][j]=need[j][i]=oo;
					continue;
				}
				need[i][j]=need[j][i]=0;
				int now=i;
				while (1){
					if (now+M<j){
						now+=M;
						need[i][j]+=I;
						need[j][i]+=I;
					}
					else break;
				}
			}
		}
		memset(f,-1,sizeof(f));
		ans=dp(0,-1);
		printf("Case #%d: %d\n",xx++,ans);
	}
	return 0;
}
