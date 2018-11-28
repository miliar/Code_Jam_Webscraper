#include<stdio.h>
#include<memory.h>

const int LSZ=100, RSZ=100;

bool gp[LSZ][RSZ];
short que[RSZ], mr[RSZ], ml[LSZ], path[LSZ];
short inline match(short nl, short nr) {
	int answer=0;
	memset(ml, -1, sizeof(ml[0])*nl);
	memset(mr, -1, sizeof(mr[0])*nr);
	for(int i=0;i<nr;i++) {
		memset(path, -1, sizeof(path[0])*nl);
		que[0]=i;
		int tail=1, head=0;
		while(tail>head) {
			short cur=que[head++];
			for(int j=0;j<nl;j++) {
				//左侧j与右侧cur是否相连
				if(!gp[j][cur]) continue;

				if(path[j]>=0) continue;
				que[tail++]=ml[j]; path[j]=cur;
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

int price[100][25];
int solve() {
	int N, K;
	scanf("%d%d", &N, &K);
	for(int i=0;i<N;i++)
		for(int j=0;j<K;j++)
			scanf("%d", &price[i][j]);
	for(int i=0;i<N;i++)
		for(int j=0;j<N;j++) {
			if(j==i) continue;

			bool succ=true;
			for(int k=0;succ&&k<K;k++)
				if(price[i][k]>=price[j][k])
					succ=false;
			gp[i][j]=succ;
		}
	return N-match(N, N);
}

int main() {
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;c++)
		printf("Case #%d: %d\n", c, solve());
}