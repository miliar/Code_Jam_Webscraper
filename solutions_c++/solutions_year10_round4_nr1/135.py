#include <stdio.h>
#include <memory.h>
#define max(a,b) (((a)>(b))?(a):(b))
char dat[203][203];
int n;
int lx[200*200], ly[200*200], lc;
int Abs(int x){
	if(x<0)return-x;
	return x;
}
bool cmp(int x,int y,int X,int Y){
	if( x<0 || x>=2*n || y<0 || y>=2*n || X<0 || X>=2*n || Y<0 || Y>=2*n ) return true;
	if( '0' <= dat[x][y] && dat[x][y] <= '9' && '0' <= dat[X][Y] && dat[X][Y] <= '9') return dat[x][y] == dat[X][Y];
	return true;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&n);
		memset(dat,0,sizeof(dat));
		gets(dat[0]);
		int i, j, k;
		lc = 0;
		for(i=0;i<n*2-1;i++){
			gets(dat[i]);
			for(j=0;j<n*2-1;j++){
				if('0' <= dat[i][j] && dat[i][j] <= '9'){
					lx[lc] = i; ly[lc] = j;
					lc ++;
				}
			}
		}
		int sol = -1, res;
		for(i=0;i<n*2-1;i++){
			for(j=0;j<2*n-1;j++){
				res = -1;
				for(k=0;k<lc;k++){
					if(!cmp(lx[k], ly[k], 2*i - lx[k], ly[k]) || !cmp(lx[k], ly[k], lx[k], 2*j - ly[k])) break;
					if(res == -1 || res < Abs(lx[k] - i)+Abs(ly[k] - j))
						res = Abs(lx[k]-i) + Abs(ly[k]-j);
				}
				if(k == lc){
					if(sol == -1 || sol > res) sol = res;
				}
			}
		}
		sol ++;
		printf("Case #%d: %d\n", t, sol*sol-n*n);
	}
	return 0;
}