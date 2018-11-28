#include <stdio.h>
#include <string.h>
int T,N,K;
char map[51][51];
char ramap[51][51];

void gravity()
{
	int i,j,x;
	char ch;
	for(j=0;j<N;j++) {
		for(x=N-1,i=N-1;i>=0;i--) {
			if(ramap[i][j]!='.') {
				map[x--][j] = ramap[i][j];
			}
		}
		for(i=0;i<=x;i++) map[i][j] = '.';
	}
//	for(i=0;i<N;i++) puts(map[i]);
}

void rotate()
{
	int i,j;
	memset(ramap,0,sizeof(ramap));
	for(i=0;i<N;i++) 
		for(j=0;j<N;j++) {
			ramap[i][j] = map[N-1-j][i];
		}
	//for(i=0;i<N;i++) puts(ramap[i]);
}

int Rw,Bw;
int dx[] = {0,1,-1,1};
int dy[] = {1,0, 1,1};
int winpos(int i,int j)
{
	char ch = map[i][j];
//	printf("%d %d %c\n",i,j,ch);
	int x,cx,cy,cnt;
	for(x = 0;x < 4;x++) {
		cnt = 0;
		cx = j;
		cy = i;
		while(cx >=0 && cy>=0 && cx<N && cy<N && map[cy][cx]==ch && cnt<K) {
			cx += dx[x];
			cy += dy[x];
//			printf("(%d,%d=%c)",cy,cx,map[cy][cx]);
			cnt++;
		}
//		printf("%d\n",cnt);
		if(cnt>=K) return 1;
	}
	return 0;
}

int main(int argc, char *argv[])
{
	int Case,i,j;
	scanf("%d",&T);
	for(Case = 1;Case <= T; Case++) {
		scanf("%d%d",&N,&K);
		for(i=0;i<N;i++) {
			scanf("%s",map[i]);
		}
		rotate();
		gravity();
		Rw = Bw = 0;
		for(i=0;i<N;i++) {
			for(j=0;j<N;j++) {
				if(map[i][j]=='R' && !Rw) {
					if(winpos(i,j)) Rw = 1;
				} else if(map[i][j]=='B' && !Bw) {
					if(winpos(i,j)) Bw = 1;
				}
			}
		}
		printf("Case #%d: ",Case);
		if(Rw && Bw) puts("Both");
		else if(Rw) puts("Red");
		else if(Bw) puts("Blue");
		else puts("Neither");
	}
	return 0;
}
