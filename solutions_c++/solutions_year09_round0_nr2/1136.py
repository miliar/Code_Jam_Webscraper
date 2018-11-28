#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

const int dx[4] = {-1,0,0,1};
const int dy[4] = {0,-1,1,0};

char l[100][100];
int m[100][100];
int N,M;

inline bool inbounds(int x,int y) {
	return (x >= 0 && x < N && y  >= 0 && y < M);
}

inline bool poor(int x1,int y1,int x2,int y2) {
	int mn,mx,my;
	int i;
	
	mn = -1;
	for (i=0;i<4;++i)
		if (inbounds(x1 + dx[i],y1 + dy[i])) {
			if ((mn > m[x1 + dx[i]][y1 + dy[i]]) || (mn == -1)) {
				mn = m[x1 + dx[i]][y1 + dy[i]];
				mx = x1 + dx[i];
				my = y1 + dy[i];
			}
		}
	
	if (mn >= m[x1][y1]) return false;
	return (mx == x2) && (my == y2);
}

void flood_fill(int x,int y) {
	int i;
	for (i=0;i<4;++i) {
		if (inbounds(x + dx[i],y + dy[i])) {
			if ((poor(x,y,x+dx[i],y+dy[i]) || poor(x+dx[i],y+dy[i],x,y)) && (l[x+dx[i]][y+dy[i]] == 0)) {
				l[x + dx[i]][y + dy[i]] = l[x][y];
				flood_fill(x + dx[i],y + dy[i]);
			}
		}
	}
}

int main() {
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int T,t,i,j,k;
	
	k = 0;
	
	scanf("%d",&T);
	
	for (t=1;t<=T;++t) {
		scanf("%d%d",&N,&M);
		
		memset(m,0,sizeof(m));
		memset(l,0,sizeof(l));
		k = 0;
		
		for (i=0;i<N;++i)
			for (j=0;j<M;++j) { scanf("%d",&m[i][j]); l[i][j] = 0;}
		
		for (i=0;i<N;++i) 
			for (j=0;j<M;++j) {
				if (l[i][j] == 0) {
					l[i][j] = 'a' + k;
					flood_fill(i,j);
					++k;
				}
			}
			
		printf("Case #%d:\n",t);
		for (i=0;i<N;++i) {
			for (j=0;j<M;++j) printf("%c ",l[i][j]);
			printf("\n");
		}
	}
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}