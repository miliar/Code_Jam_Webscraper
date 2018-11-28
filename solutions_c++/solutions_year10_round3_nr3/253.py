#include<stdio.h>
#include<string.h>
#include<math.h>
int board[1000][1000];
char line[1000];
int sizes[1000];

int main() {
	int i,j,T,N,M, num,l,a,b,s,can,cnt,m,ma,mb;
	freopen("google2.in","r",stdin);
	freopen("google2.out","w",stdout);
	scanf("%d", &T);
	for(i=0;i<T;i++){
		scanf("%d %d", &N, &M);
		for(j=0;j<N;j++) {
			scanf("%s",line);
			for(l=0;l<M/4;l++) {
				if(line[l]<='9') num = line[l]-'0';
				else num = line[l]-'A'+10;
				board[j][4*l+0] = (num>>3)&1;
				board[j][4*l+1] = (num>>2)&1;
				board[j][4*l+2] = (num>>1)&1;
				board[j][4*l+3] = (num>>0)&1;		
			}
		}
		for(j=0;j<N;j++) {
			for(l=0;l<M;l++) {
				if((l+j)%2 == board[j][l])board[j][l] = 1;
				else board[j][l] = 0;
			}
		}
		for(j=1;j<=N;j++) sizes[j] = 0;
		while(1) {
			m = 0;
			ma = 0;
			mb = 0;
			for(a=0;a<N;a++){
				for(b=0;b<M;b++){
					can = 1;
					for(s=1;s<=N && a+s<=N && b+s<=M;s++){
						for(j=a;j<a+s;j++){
							for(l=b;l<b+s;l++){
								if(board[j][l] == -1) can = 0;
								if(board[j][l] != board[a][b])can=0;
								if(can == 0)break;
							}
							if(can == 0)break;
						}
						if(can == 0)break;
					}
					s--;
					if(s > m) {
						m = s;
						ma = a;
						mb = b;
					}
				}
			}
			sizes[m]++;
			if(m == 0) break;
			for(j=ma;j<ma+m;j++){
				for(l=mb;l<mb+m;l++){
					board[j][l]=-1;
				}
			}
		}
		cnt=0;
		for(j=1;j<=N;j++) if(sizes[j]>0) cnt++;
		printf("Case #%d: %d\n", i+1, cnt);
		for(j=N;j>0;j--) {
			if(sizes[j]==0) continue;
			printf("%d %d\n", j, sizes[j]);
		}
	}
	
	return 0;	
}
