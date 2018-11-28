#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
const int maxn=501;
int a[maxn][maxn];
int s[3][maxn][maxn];
char str[maxn+1];
int n,m;

void init(){
	int nouse;
	scanf("%d%d%d",&n,&m,&nouse);
	for (int i=0;i<n;i++){
		scanf("%s",str);
		for (int j=0;j<m;j++){
			a[i][j]=str[j]-'0';
		}
	}
	return;
}

void preprocess(){
	for (int k=0;k<3;k++){
		for (int i=0;i<=n;i++){
			for (int j=0;j<=m;j++){
				if ((i==0)||(j==0)){
					s[k][i][j]=0;
					continue;
				}
				s[k][i][j]=s[k][i-1][j]+s[k][i][j-1]-s[k][i-1][j-1];
				if (k==0){
					s[k][i][j]+=a[i-1][j-1];
					continue;
				}
				if (k==1){
					s[k][i][j]+=a[i-1][j-1]*(i-1);
					continue;
				}
				s[k][i][j]+=a[i-1][j-1]*(j-1);
			}
		}
	}
	return;
}

__int64 calcmass(int tp,int x1,int x2,int y1,int y2){
	return s[tp][x2][y2]-s[tp][x1][y2]-s[tp][x2][y1]+s[tp][x1][y1];
}

bool ok(int x,int y,int k){
	__int64 mass=calcmass(0,x,x+k,y,y+k)-a[x][y]-a[x+k-1][y]-a[x][y+k-1]-a[x+k-1][y+k-1];
	__int64 line=calcmass(1,x,x+k,y,y+k)-x*a[x][y]-(x+k-1)*a[x+k-1][y]-x*a[x][y+k-1]-(x+k-1)*a[x+k-1][y+k-1];
	__int64 column=calcmass(2,x,x+k,y,y+k)-y*a[x][y]-y*a[x+k-1][y]-(y+k-1)*a[x][y+k-1]-(y+k-1)*a[x+k-1][y+k-1];
	return ((line*2==mass*(2*x+k-1))&&(column*2==mass*(2*y+k-1)));
}

void calc(){
	preprocess();
	int ans=-1;
	for (int i=0;i<n;i++){
		for (int j=0;j<m;j++){
			for (int k=3;(k<=n-i)&&(k<=m-j);k++){
				if (ok(i,j,k)){
					ans=max(ans,k);
				}
			}
		}
	}
	if (ans==-1){
		puts("IMPOSSIBLE");
	} else {
		printf("%d\n",ans);
	}
	return;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d: ",i);
		calc();
	}
	return 0;
}
