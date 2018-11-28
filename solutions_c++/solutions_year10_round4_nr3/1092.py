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

const int N = 105;
int d[N][N],a[N][N];

bool go_on(){
	int i,j,k = 0;
	for(i = 0;i<N;i++){
		for(j = 0;j<N;j++){
			if(d[i][j])k++;
		}
	}
	if(k==0)return false;
	for(i = 1;i<N;i++){
		for(j = 1;j<N;j++){
			a[i][j] = d[i][j];
			if(d[i][j]==1){
				if(!d[i-1][j] && !d[i][j-1]){
					a[i][j] = 0;
				}
			}else{
				if(d[i-1][j] && d[i][j-1]){
					a[i][j] = 1;
				}
			}
		}
	}
	for(i = 0;i<N;i++){
		for(j = 0;j<N;j++){
			d[i][j] = a[i][j];
		}
	}
	return true;
}
int n;
int main(){
	freopen("C-small-attempt0.in","r",stdin);freopen("out.txt","w",stdout);
    int i,j,k,t,nc = 0;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		memset(d,0,sizeof(d));
		for(i = 0;i<n;i++){
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(j = x1;j<=x2;j++){
				for(k = y1;k<=y2;k++){
					d[j][k] = 1;
				}
			}
		}
		int ans = 0;
		while(go_on())ans++;
		printf("Case #%d: %d\n",++nc,ans);
	}
    return 0;
}