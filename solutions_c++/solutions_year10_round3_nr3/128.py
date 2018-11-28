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

const int N  = 600;
int m,n;
char str[20] = "0123456789ABCDEF",ts[N];
int val[N],grid[N][N],vis[N][N];
int vi[N],sz[N];

bool ok(int x,int y,int s){
	if(x+s>m || y+s>n)return false;
	int i,j,k;
	for(i = 0;i<s;i++){
		for(j = 0;j<s;j++){
			if(vis[x+i][y+j])return false;
			int sum = x+i+y+j;
			if((x+y+i+j)%2==(x+y)%2){
				if(grid[x][y]!=grid[x+i][y+j])return false;
			}else{
				if(grid[x][y]==grid[x+i][y+j])return false;
			}
		}
	}
	return true;
}

void out(int x,int y,int s){
	int i,j,k;
	for(i = 0;i<s;i++){
		for(j = 0;j<s;j++){
			vis[x+i][y+j] = 1;
		}
	}
}
int cut(int x){
	int i,j,k,ret = 0;
	for(i = 0;i<m;i++){
		for(j = 0;j<n;j++){
			if(ok(i,j,x)){
				ret ++;
				out(i,j,x);
			}
		}
	}
	return ret;
}
int main(){
	freopen("C-small-attempt0.in","r",stdin);freopen("out.txt","w",stdout);
    int i,j,k,t,nc = 0;
	for(i = 0;i<strlen(str);i++){
		val[str[i]] = i;
	}
	scanf("%d",&t);
	while(t--){
		scanf("%d%d",&m,&n);
		for(i = 0;i<m;i++){
			scanf("%s",ts);
			int l;
			for(l = 0;l<n/4;l++){
				int tmp = val[ts[l]];
				for(j = 0,k = l*4+3;j<4;j++,k--){
					if(tmp&(1<<j))grid[i][k] = 1;
					else grid[i][k] = 0;
				}
			}
		}
		int tmax = min(m,n);
		k = 0;
		memset(vis,0,sizeof(vis));
		for(i = tmax;i>=1;i--){
			int tmp = cut(i);
			if(tmp>0){
				sz[k] = i;
				vi[k++] = tmp;
			}
		}
		printf("Case #%d: %d\n",++nc,k);
		for(i = 0;i<k;i++){
			printf("%d %d\n",sz[i],vi[i]);
		}
	}
    return 0;
}