#include<iostream>
using namespace std;

const int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

int idx[200][200];

int N, M;
int h[200][200];
int fst[200*200];
char s[200][200], mark[200*200];

int find(int a) {
	return fst[a] == a ? a : (fst[a] = find(fst[a]));
}

int run() {
	int pop = 0;
	scanf("%d %d", &N, &M);
	for(int i=0;i<N;++i) {
		for(int j=0;j<M;++j) {
			scanf("%d", &h[i][j]);
			fst[pop] = pop;
			idx[i][j] = pop++;
		}
	}
	for(int i=0;i<N;++i) {
		for(int j=0;j<M;++j) {
			int cx=i, cy=j, x, y, tarh = 0x7fffffff;
			for(int d =0; d<4; ++d) {
				x = i+dir[d][0];
				y = j+dir[d][1];
				if(x >=0 && x < N && y >= 0 && y < M) {
					if(h[x][y] < tarh) {
						tarh = h[x][y];
						cx = x; cy = y;
					}
				}
			}
			if(tarh < h[i][j]) {
				fst[find(idx[i][j])] = find(idx[cx][cy]);
			}
		}
	}
	memset(mark,0,sizeof(mark));
	char cur = 'a' - 1;
	for(int i=0;i<N;++i) {
		for(int j=0;j<M;++j) {
			if(!mark[find(idx[i][j])]) {
				mark[find(idx[i][j])] = ++ cur;
			}
			s[i][j] = mark[find(idx[i][j])];
			
			putchar(s[i][j]);
			if(j == M-1) puts("");
			else putchar(' ');
		}
	}
	
}

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int test; scanf("%d", &test);
	for(int no=1;no<=test;++no) {
		printf("Case #%d:\n", no);
		run();
	}
}
