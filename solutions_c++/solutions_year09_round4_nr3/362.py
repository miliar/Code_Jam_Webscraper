#include <stdio.h>
int dat[16][25];
int map[16][16];
bool go[ 1<<16 ];
int gogo[ 1 << 16 ];
int wow[1<<16];
int wh;
int main(){
	freopen("inpug.txt","r",stdin);
	freopen("outpug.txt","w",stdout);
	int T, n ,m;
	scanf("%d",&T);
	while(T>0){
		T--;
		scanf("%d %d",&n, &m);
		int i, j, k;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				scanf("%d",&dat[i][j]);
			}
		}
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				map[i][j] = 0;
				if(i != j){
				for(k=0;k<m-1;k++){
					if((dat[i][k] >= dat[j][k] && dat[i][k+1] <= dat[j][k+1]) ||  (dat[i][k] <= dat[j][k] && dat[i][k+1] >= dat[j][k+1])){
						map[i][j] = 1;
					}
				}
				}
			}
		}
		for(i=0;i<(1<<n);i++){
			for(j=0;j<n;j++){
				if( (i & (1<<j) ) == 0) continue;
				for(k=0;k<n;k++){
					if( (i & (1<<k) ) == 0) continue;
					if(map[j][k] == 1) break;
				}
				if(k<n)break;
			}
			if(j<n) go[i] = false;
			else go[i] = true;
		}
		for(i=0;i<(1<<n);i++){
			if(go[i]){
				for(j=0;j<n;j++){
					if(( i & (1<<j) ) != 0){
						go[(i ^ (1<<j))] = false;
					}
				}
			}
		}
		wh = 0;
		for(i=0;i<(1<<n);i++){
			if(go[i]){
				wow[wh++] = i;
				gogo[i] = 1;
			}
			else gogo[i] = -1;
		}
		for(i=0;i<(1<<n);i++){
			if(go[i]){
				int next;
				for(j=0;j<wh;j++){
					next = i | wow[j];
					if(gogo[next] == -1 || gogo[next] > gogo[i] + 1){ 
						gogo[next] = gogo[i] + 1;
						go[next] = true;
					}
				}
			}
		}
		static int t=1;
		printf("Case #%d: %d\n",t++,gogo[ (1<<n) - 1 ] );
	}
	return 0;
}