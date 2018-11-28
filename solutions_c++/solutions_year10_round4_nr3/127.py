#include<stdio.h>       	
#include<memory.h>
#include<algorithm>
#include<stdlib.h>

int T;
int A[333][333],f[2][333][333],q1,q2,qx[333*333*333],qy[333*333*333],qd[333*333*333],n,x1,y1,x2,y2,ans,x,y,d,col;


int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		memset(f,0,sizeof(f));
		scanf("%d",&n);
		col=0;
		for(int i=0;i<n;i++){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(int ii=x1;ii<=x2;ii++)
			for(int jj=y1;jj<=y2;jj++){
				col+=f[0][ii][jj]==0;
				f[0][ii][jj]=f[1][ii][jj]=1;
			}
		}
		q1=q2=0;
		for(int ii=1;ii<=100;ii++)
			for(int jj=1;jj<=100;jj++) if((f[0][ii][jj] && !f[0][ii-1][jj] && !f[0][ii][jj-1]) || (!f[0][ii][jj] && f[0][ii-1][jj] && f[0][ii][jj-1])){
				qx[q1]=ii;
				qy[q1]=jj;
				qd[q1++]=0;
			}
		ans=1;
		while(q2<q1 && col){
			x=qx[q2];
			y=qy[q2];
			d=qd[q2++];
//			printf("%d %d %d\n",x,y,d);
			if(d!=ans){
				ans=d;
//				for(int i=1;i<=10;i++){
//				for(int j=1;j<=10;j++) putchar(f[d&1][i][j]+48);
//				puts("");
//				}
				memcpy(&f[1-(d&1)],&f[d&1],333*333*4);
			}
			if(f[1-(d&1)][x][y] && !f[d&1][x-1][y] && !f[d&1][x][y-1]){
				f[1-(d&1)][x][y]=0;
				col--;
					qx[q1]=x+1;
					qy[q1]=y;
					qd[q1++]=d+1;
					qx[q1]=x;
					qy[q1]=y+1;
					qd[q1++]=d+1;
			}else
			if(!f[1-(d&1)][x][y] && f[d&1][x-1][y] && f[d&1][x][y-1]){
				f[1-(d&1)][x][y]=1;
				col++;
					qx[q1]=x+1;
					qy[q1]=y;
					qd[q1++]=d+1;
					qx[q1]=x;
					qy[q1]=y+1;
					qd[q1++]=d+1;
			}
		}
		printf("Case #%d: %d\n",_,ans+1);
	}
	return 0;
}
