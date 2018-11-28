#include <cstdio>
#include <queue>
#include <memory.h>
using namespace std;
int a[111][111];
int d[111][111];
int go(int x, int y){
	if(x<=0 || y<=0)
		return 0;
	if(x==1 && y==1)
		return 1;
	if(a[x][y]==-1)
		return 0;
	if(d[x][y]!=-1)
		return d[x][y];
	return d[x][y] = (go(x-1,y-2) + go(x-2,y-1))%10007;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tc=1; tc<=t; tc++){
		int n,m,r;
		memset(a,0,sizeof(a));
		scanf("%d %d %d\n",&n,&m,&r);
		for(int i=1; i<=r; i++){
			int t1,t2;
			scanf("%d %d\n",&t1,&t2);
			a[t1][t2]=-1;
		}
		memset(d,-1,sizeof(d));
		printf("Case #%d: %d\n",tc,go(n,m)%10007);
	}
	return 0;
}