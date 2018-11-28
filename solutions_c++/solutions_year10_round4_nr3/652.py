#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int N=101;
int a[N][N],b[N][N];
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int i,j,k,n,t,tt=1,x1,x2,y1,y2;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		memset(a,0,sizeof(a));
		while(n--){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			if(x1>x2)swap(x1,x2);
			if(y1>y2)swap(y1,y2);
			for(i=x1;i<=x2;i++)
				for(j=y1;j<=y2;j++)
					a[i][j]=1;
		}
		for(k=0;;k++){
			for(i=1;i<N;i++){
				for(j=1;j<N;j++)
					if(a[i][j])break;
				if(j!=N)break;
			}
			if(i==N)break;
			memset(b,0,sizeof(b));
			for(i=1;i<N;i++)
				for(j=1;j<N;j++){
					b[i][j]=a[i][j];
					if(a[i-1][j]&&a[i][j-1])
						b[i][j]=1;
					if(!a[i-1][j]&&!a[i][j-1])
						b[i][j]=0;
				}
			memcpy(a,b,sizeof(b));
		}
		printf("Case #%d: %d\n",tt++,k);
	}
	return 0;
}
