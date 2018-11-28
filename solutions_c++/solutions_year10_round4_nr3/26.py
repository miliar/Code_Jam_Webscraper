#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

#define inf 100000000

int ixie(int a1, int a2, int b1, int b2){
	if(a2==b1)return -1;
	if(b2==a1)return -2;
	if(a2<b1)return 0;
	if(b2<a1)return 0;
	return 1;
}

struct R{
	int x1,x2,y1,y2;
	int gh;
	int m, r, b;
	int inte(R &k){
		int qx = ixie(x1,x2,k.x1,k.x2), qy = ixie(y1,y2,k.y1,k.y2);
		//printf(" qx=%d qy=%d\n", qx, qy);
		if(qx==0 || qy==0)return 0;
		if(qx==1 || qy==1)return 1;
		return (qx != qy);
	}
};

R r[2222];
char g[2222][2222];
char vi[2222];
int n;

int dfs(int k, int gh){
	vi[k]=1;
	r[k].gh = gh;
	for(int i=0; i<n; i++)if(g[k][i])if(!vi[i]){
		dfs(i, gh);
	}
	return 0;
}
		
int main(){
	int nn,ii,b,c,cnt;
	scanf("%d",&nn);
	for(ii =1;ii<=nn;ii++){
		scanf("%d",&n);
		for(int i=0 ; i<n; i++){
			scanf("%d%d%d%d", &r[i].x1, &r[i].y1, &r[i].x2, &r[i].y2);
			r[i].x2++;r[i].y2++;
			r[i].gh = i;
			r[i].m = inf;
			r[i].r=r[i].b=-inf;
		}
		memset(g,0,sizeof(g));
		memset(vi,0,sizeof(vi));
		for(int i=0; i<n; i++){
			for(int j=0; j<i; j++)if(r[i].inte(r[j])){
				g[i][j]=g[j][i]=1;
			}
		}
		for(int i=0; i<n; i++)if(!vi[i])dfs(i, i);
		
		for(int i=0; i<n; i++){
			int j=r[i].gh;
			r[j].m = min(r[j].m, r[i].x1+r[i].y1);
			r[j].r = max(r[j].r, r[i].x2);
			r[j].b = max(r[j].b, r[i].y2);
		}
		int ans = 0;
		for(int i=0; i<n; i++)if(r[i].gh == i){
			//printf(" m=%d r=%d b=%d\n", r[i].m, r[i].r, r[i].b);
			ans = max(ans, r[i].r+r[i].b-r[i].m-1);
		}
		printf("Case #%d: %d\n",ii,ans);
	}
	return 0;
}
