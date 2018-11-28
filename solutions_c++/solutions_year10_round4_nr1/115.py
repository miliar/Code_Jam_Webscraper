#include<stdio.h>
#include<memory.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>

int T;


int n,ad,sz=0,a[411][411],x,y,ans=0,found=0;

bool tryeleg(int sz,int xx,int yy){
	int nx,ny,ss,col;
	for(int i=1;i<=sz;i++)
		for(int j=1;j<=sz;j++)if(i>xx && j>yy && a[i-xx][j-yy]!=-1){
			if(i>j) ss=sz-(i-j);else ss=sz-(j-i);
			if(i>j) col=j;else col=i;
			nx=i+ss-col-col+1;
			ny=j+ss-col-col+1;
			if((nx>xx && ny>yy && a[nx-xx][ny-yy]!=-1) && a[i-xx][j-yy]!=a[nx-xx][ny-yy])
				return 0;

			if(j>sz-i+1) ss=sz+sz+1-(i+j);else ss=(j+i)-1;
			if(j>sz-i+1) col=sz+j+1-(i+j);else col=j;
			nx=i-(ss-col-col+1);
			ny=j+ss-col-col+1;
			if((nx>xx && ny>yy && a[nx-xx][ny-yy]!=-1) && a[i-xx][j-yy]!=a[nx-xx][ny-yy])
				return 0;
		}
	return 1;
}

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		memset(a,-1,sizeof(a));
		scanf("%d",&n);
		ad=1;
		sz=0;
		for(int i=0;i<n+n-1;i++){
			sz+=ad;
			if(ad==1) x=1, y=n-i;else
				  x=i-n+2, y=1;

			for(int j=0;j<sz;j++){
				scanf("%d",&a[x][y]);
				x++;
				y++;
			}
			if(sz==n) ad=-1;
		}
		ans=0;
		found=0;
		int nn=n+n+n+n;
		for(int i=n;i<=nn && !found;i++)
			for(int xx=0;xx<=i-n && !found;xx++)
			for(int yy=0;yy<=i-n;yy++)
			if(tryeleg(i,xx,yy)){
				ans=i*i-n*n;
				found=1;
				break;
			}
		if(!found) puts("!!!");
		printf("Case #%d: %d\n",_,ans);
	}
	return 0;
}
