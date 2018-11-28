#include <cstdio>
#include <cstring>

using namespace std;

int T, H, W;

int l[128][128];
int g[128][128];
char gN;
int mapping[50];

int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0, 1};

#define encode(x, y) ((y)*128 + (x))
#define decodex(z) ((z) % 128)
#define decodey(z) ((z) / 128)

int rek(int x, int y){
	if(g[y][x] <= 0)
		g[y][x] = rek(decodex(-g[y][x]), decodey(-g[y][x]));
	return g[y][x];
}

char get(int x, int y){
	int i = rek(x, y);
	return mapping[i] ? mapping[i] : (mapping[i] = gN++);
}

int main(){
	scanf("%d", &T);
	for(int tc=1; tc<=T; ++tc){
		gN = 1;
		memset(mapping, 0, sizeof(mapping));
		scanf("%d %d", &H, &W);
		for(int j=0; j<H; ++j)
			for(int i=0; i<W; ++i)
				scanf("%d", &l[j][i]);
		for(int j=0; j<H; ++j)
			for(int i=0; i<W; ++i){
				int mini = -1;
				for(int k=0; k<4; ++k)
					if(j+dy[k] >= 0 && j+dy[k] < H && i+dx[k] >= 0 && i+dx[k] < W && l[j][i] > l[j+dy[k]][i+dx[k]] && (mini == -1 || l[j+dy[k]][i+dx[k]] < l[decodey(mini)][decodex(mini)]))
						mini = encode(i+dx[k], j+dy[k]);
				g[j][i] = mini == -1 ? gN++ : -mini;
			}
		printf("Case #%d:\n", tc);
		gN = 'a';
		for(int j=0; j<H; ++j){
			for(int i=0; i<W; ++i){
				if(i) putchar(' ');
				printf("%c", get(i, j));
			}
			puts("");
		}
	}
}
