#include<cstdio>
#include<algorithm>
using namespace std;

const int maxn = 108;
const int dh[4]={-1,0,0,1}, dw[4]={0,-1,1,0};

int		a[maxn][maxn], b[maxn][maxn];

int		h, w, lev;

inline  legel(int x, int y){
		return x>=0 && x<h && y>=0 && y<w;
}

int     find(int i, int j){
		if (b[i][j]) return b[i][j];
		int x, y, k, t = a[i][j], s = -1;
		for(k=0; k<4; k++){
			x = i + dh[k]; y = j + dw[k];
			if (legel(x,y) && t > a[x][y]){
				t = a[x][y]; s = k;
			}
		}
		if (s==-1) return b[i][j] = ++lev;
		else return b[i][j] = find(i+dh[s], j+dw[s]);
}

int		main(){
		int t, T, i, j;
		//freopen("input.txt","r",stdin);
		//freopen("output.txt","w",stdout);
		for(scanf("%d", &T), t=1; t<=T; t++){
			scanf("%d %d",&h, &w); 
			for(i=0; i<h; i++) for(j=0; j<w; j++){
				scanf("%d", &a[i][j]);
				b[i][j] = 0;
			}
			lev = 0;
			for(i=0; i<h; i++) for(j=0; j<w; j++) find(i,j);
			printf("Case #%d:\n", t);
			for(i=0; i<h; i++){
				for(j=0; j<w; j++){
					if (j==0) printf("%c", b[i][j]+'a'-1);
					else printf(" %c", b[i][j]+'a'-1);
				}
				printf("\n");
			}
		}
		return 0;
}
