#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<stdlib.h>
using namespace std;
char in[510][510];
int sum[510][510];
int sx[510][510];
int sy[510][510];
inline int gs(int a[510][510],int l,int r,int u,int d){
    return a[r][d]-a[l-1][d]-a[r][u-1]+a[l-1][u-1];
}
inline bool isb(int lx,int rx,int ly,int ry){
    int xx=0,yy=0;
    xx-=(rx-lx)*(in[lx][ly]-in[rx][ly]+in[lx][ry]-in[rx][ry]);
    yy-=(ry-ly)*(in[lx][ly]+in[rx][ly]-in[lx][ry]-in[rx][ry]);
    if((rx-lx+1)%2==0){
	int mx=(lx+rx)/2;
	int my=(ly+ry)/2;
	xx+=(2*mx+1)*gs(sum,lx,rx,ly,ry)-2*gs(sx,lx,rx,ly,ry);
	yy+=(2*my+1)*gs(sum,lx,rx,ly,ry)-2*gs(sy,lx,rx,ly,ry);
    }else{
	int mx=(lx+rx)/2;
	int my=(ly+ry)/2;
	xx+=2*mx*gs(sum,lx,rx,ly,ry)-2*gs(sx,lx,rx,ly,ry);
	yy+=2*my*gs(sum,lx,rx,ly,ry)-2*gs(sy,lx,rx,ly,ry);
    }
    return xx==0&&yy==0;
}
int main(){
    int tmt,cas=1;
    scanf("%d",&tmt);
    while(tmt--){
	int n,m,i,j,k;
	scanf("%d%d%*d",&n,&m);
	for(i=1;i<=n;i++){
	    scanf("%s",in[i]+1);
	    for(j=1;j<=m;j++)in[i][j]-='0';
	}
	memset(sum,0,sizeof(sum));
	memset(sx,0,sizeof(sx));
	memset(sy,0,sizeof(sy));
	for(i=1;i<=n;i++){
	    for(j=1;j<=m;j++){
		sum[i][j]=sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+in[i][j];
		sx[i][j]=sx[i-1][j]+sx[i][j-1]-sx[i-1][j-1]+in[i][j]*i;
		sy[i][j]=sy[i-1][j]+sy[i][j-1]-sy[i-1][j-1]+in[i][j]*j;
	    }
	}
	int ans=0;
	for(i=1;i<=n;i++){
	    for(j=1;j<=m;j++){
		for(k=1;;k++){
		    if(i-k<=0||i+k>n||j-k<=0||j+k>m)break;
		    if(isb(i-k,i+k,j-k,j+k))ans=max(ans,k*2+1);
		}
	    }
	}
	for(i=1;i<=n-1;i++){
	    for(j=1;j<=m-1;j++){
		for(k=2;;k++){
		    if(i-k+1<=0||i+k>n||j-k+1<=0||j+k>m)break;
		    if(isb(i-k+1,i+k,j-k+1,j+k))ans=max(ans,k*2);
		}
	    }
	}
	printf("Case #%d: ",cas++);
	if(ans==0)puts("IMPOSSIBLE");
	else printf("%d\n",ans);
    }
}
