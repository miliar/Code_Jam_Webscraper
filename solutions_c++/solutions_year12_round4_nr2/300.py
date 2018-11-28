#include<cstdio>
#include<cstring>
#include<algorithm>
#define maxn (1005)
using namespace std;

int test,N,W,L,cnt,x[maxn],y[maxn],r[maxn];

bool check(){
	bool ok=true;
	for (int i=0;i<N;i++)
		for (int j=i+1;j<N;j++){
			if (x[i]+r[i]<=x[j]-r[j] || x[i]-r[i]>=x[j]+r[j] || y[i]+r[i]<=y[j]-r[j] || y[i]-r[i]>=y[j]+r[j]) continue;
			int dx1,dy1,dx2,dy2;
			dx1=x[i]+r[i]-(x[j]-r[j]);
			dx2=x[j]+r[j]-(x[i]-r[i]);
			dy1=y[i]+r[i]-(y[j]-r[j]);
			dy2=y[j]+r[j]-(y[i]-r[i]);
			int r=rand()%8;
			if (x[j]+dx1<=W && r==0){
				x[j]+=dx1;
				//return false;
			}
			if (x[i]-dx1>=0 && r==1){
				x[i]-=dx1;
				//return false;
			}
			if (x[j]-dx2>=0 && r==2){
				x[j]-=dx2;
				//return false;
			}
			if (x[i]+dx2<=W && r==3){
				x[i]+=dx2;
				//return false;
			}
			if (y[j]+dy1<=L && r==4){
				y[j]+=dy1;
				//return false;
			}
			if (y[i]-dy1>=0 && r==5){
				y[i]-=dy1;
				//return false;
			}
			if (y[j]-dy2>=0 && r==6){
				y[j]-=dy2;
				//return false;
			}
			if (y[i]+dy2<=L && r==7){
				y[i]+=dy2;
				//return false;
			}
			//return false;
			ok=false;
		}
	if (!ok) return false;
	return true;
}
int main(){
	srand(time(NULL));
	freopen("i.txt","r",stdin);
	cnt=1;
	for (scanf("%d",&test);test--;cnt++){
		printf("Case #%d:",cnt);
		scanf("%d%d%d",&N,&W,&L);
		for (int i=0;i<N;i++) scanf("%d",&r[i]);
		for (int i=0;i<N;i++){
			x[i]=y[i]=0;
			if (i>0){
				x[i]=x[i-1]+r[i-1]+r[i];
				if (x[i]>W) x[i]=x[i]%W;
				y[i]=y[i-1]+r[i-1]+r[i];
				if (y[i]>L) y[i]=y[i]%L;
			}
		}
		while (!check());
		for (int i=0;i<N;i++) printf(" %d %d",x[i],y[i]);
		puts("");
	}
	return 0;
}
