#include<memory.h>
#include<stdio.h>

const int SZ=7000;
bool gp[SZ][SZ];
short que[SZ],mr[SZ],ml[SZ],path[SZ];
short inline match(short nl, short nr) {
	short i,j,cur,tail,head,answer=0;
	memset(ml, -1, sizeof(ml[0])*nl);
	memset(mr, -1, sizeof(mr[0])*nr);
	for(i=0;i<nr;i++) {
		memset(path, -1, sizeof(path[0])*nl);
		que[0]=i; tail=0; head=0;
		while(tail<=head) {
			cur=que[tail++];
			for(j=0;j<nl;j++) {
				//左侧j与右侧cur是否相连
				if(!gp[j][cur]||path[j]>=0) continue;
				que[++head]=ml[j]; path[j]=cur;
				if(ml[j]<0) {
					short prev=1, right=j;
					while(prev>=0) {
						short &left=path[right];
						ml[right]=left;
						prev=mr[left];
						mr[left]=right;
						right=prev;
					}
					answer++;
					goto brkwle;
				}
			}
		}
brkwle:;
	}
    return answer;
}

int id[80][80];
char map[80][81];
int M, N;
void Test(int x, int y, int dx, int dy) {
	dx+=x; dy+=y;
	if(dx>=0 && dy>=0 && dx<M && dy<N && id[dx][dy]!=-1 && id[x][y]!=-1) {
		gp[id[x][y]][id[dx][dy]]=true;
		gp[id[dx][dy]][id[x][y]]=true;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for(int cas=1;cas<=T;cas++) {
		scanf("%d%d", &M, &N);
		for(int i=0;i<M;i++) scanf("%s", map[i]);
		memset(gp, 0, sizeof(gp));
		int ip=0;
		for(int i=0;i<M;i++) {
			for(int j=0;j<N;j++) {
				if(map[i][j]!='x') id[i][j]=ip++;
				else id[i][j]=-1;

				const int dir[][2]={{0, -1}, {-1, -1}, {-1, 1}};
				for(int k=0;k<3;k++) Test(i, j, dir[k][0], dir[k][1]);
			}
		}

		printf("Case #%d: %d\n", cas, ip-match(ip, ip)/2);
	}
	return 0;
}