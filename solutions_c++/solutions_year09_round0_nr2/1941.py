#include <stdio.h>
#include <memory.h>
int q[10000],head,t;
int w,h;
int dat[103][103];
int edge[103][103][4];/* N,W,E,S */
int dir[4][2] = {-1,0, 0,-1, 0,1, 1,0};
int basins[27],bcnt;
int result[103][103];
int main(){
	int i,j;
	int T;
	int test;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&test);
	for(T=0;T<test;T++){
		memset(edge,0,sizeof(edge));
		bcnt =0;
		scanf("%d%d",&h,&w);
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				scanf("%d",&dat[i][j]);
			}
		}
		int k;
		head=t=0;
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				int minh = dat[i][j],mindir=-1;
				for(k=0;k<4;k++){
					if(i+dir[k][0] < 0 || i+dir[k][0] >= h){
						continue;
					}
					if(j+dir[k][1] < 0 || j+dir[k][1] >= w){
						continue;
					}
					if(minh > dat[i+dir[k][0]][j+dir[k][1]]){
						minh = dat[i+dir[k][0]][j+dir[k][1]];
						mindir = k;
					}
				}
				if(mindir == -1){
					q[t++] = i*128+j;
					basins[bcnt] = 0;
					result[i][j] = bcnt;
					bcnt ++;
				}else{
					edge[i+dir[mindir][0]][j+dir[mindir][1]][mindir] = 1;
				}
			}
		}
		for(head=0;head<t;head++){
			i = (q[head]>>7);
			j = (q[head]&127);
			for(k=0;k<4;k++){
				if(edge[i][j][k]){
					result[i-dir[k][0]][j-dir[k][1]] = result[i][j];
					q[t++] = ( ((i-dir[k][0])<<7) | (j-dir[k][1]) );
				}
			}
		}
		int chcnt='a';
		printf("Case #%d:\n",T+1);
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				if(basins[result[i][j]] == 0){
					basins[result[i][j]] = chcnt;
					chcnt++;
				}
				printf("%c ",(char)basins[result[i][j]]);
			}
			printf("\n");
		}
	}
	return 0;
}
