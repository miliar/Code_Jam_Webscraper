#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN	=	100 + 10;
const int dx[]	=	{-1, 0, 0, 1};
const int dy[]	=	{0, -1, 1, 0};

int al[MAXN][MAXN];
int h,w;

int ff[MAXN*MAXN];
inline int no(int i,int j){return (i-1)*w + j-1;}

int f(int x){
	if(ff[x] == x)return x;
	return ff[x] = f(ff[x]);
}

void uni(int a,int b){
	ff[f(a)] = f(b);
}

char used[MAXN*MAXN];

void init(){
	memset(al, 67, sizeof(al));
	
	scanf("%d%d", &h, &w);
	for(int i=1; i<=h; ++i)
		for(int j=1; j<=w; ++j)
			scanf("%d", &al[i][j]);
}

void solve(){
	for(int i=0; i<MAXN*MAXN; ++i)
		ff[i] = i;
	
	for(int i=1; i<=h; ++i)
		for(int j=1; j<=w; ++j){
			int minp = 0;
			for(int t=1; t<4; ++t){
				if(al[i+dx[t]][j+dy[t]] < al[i+dx[minp]][j+dy[minp]])
					minp = t;
			}
			if(al[i+dx[minp]][j+dy[minp]] < al[i][j]){
				//printf("uni  %d %d %d %d %d %d\n", i, j, i+dx[minp], j+dy[minp], al[i][j],al[i+dx[minp]][j+dy[minp]]);
				uni(no(i,j), no(i+dx[minp],j+dy[minp]));
			}
		}
	
	memset(used, 0, sizeof(used));
	char count = 'a' - 1;
	for(int i=1; i<=h; ++i){
		for(int j=1; j<=w; ++j){
			//printf(" %d", f(no(i,j)));
			if(!used[f(no(i,j))]){
				used[f(no(i,j))] = ++count;
				
			}
		}
		//printf("\n");
	}
	
	for(int i=1; i<=h; ++i){
		printf("%c", used[f(no(i,1))]);
		for(int j=2; j<=w; ++j)
			printf(" %c", used[f(no(i,j))]);
		printf("\n");
	}
}

int main(){
	int t;
	scanf("%d", &t);
	for(int c=1; c<=t; ++c){
		init();
		printf("Case #%d:\n", c);
		solve();
	}
}
