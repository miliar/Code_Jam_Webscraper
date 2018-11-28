#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#define task "file"
#define N 100

using namespace std;
int test;
int Mod=10007;
int t[N][N];
int d[N][N];
int mark[N][N];
int h,w,k;
int a,b;


int fuck(int x,int y){
	if (x<0 || y<0) return 0;
	if (t[x][y]) return 0;
	if (mark[x][y]) return d[x][y];
	mark[x][y]=1;
	int res=0;
	res=(res+fuck(x-2,y-1))%Mod;
	res=(res+fuck(x-1,y-2))%Mod;
	d[x][y]=res;
	return res;
}

int main(void){
	freopen(task".in","r",stdin);
	freopen(task".out","w",stdout);
	scanf("%i",&test);
	for (int zzz=1;zzz<=test;zzz++){
		printf("Case #%i: ",zzz);
		scanf("%i %i %i",&h,&w,&k);
		memset(d,0,sizeof(d));
		memset(t,0,sizeof(t));
		memset(mark,0,sizeof(mark));
		mark[0][0]=1;
		d[0][0]=1;
		for (int i=0;i<k;i++){
			scanf("%i %i",&a,&b);
			t[a-1][b-1]=1;
		}
		h--;
		w--;
		int ans=fuck(h,w);
		printf("%i\n",ans);

	}


	return 0;
}
