#include<cstdio>
#include<queue>

using namespace std;

const int Dx[] = {0,-1,1,0};
const int Dy[] = {-1,0,0,1};

struct Node{
	int X,Y;
};

int N,M;
char Base;
char Map[105][105];
int Valu[105][105];

void Fill(int i,int j) {
	int Temp,Minm;
	Node p,q;
	p.Y = i,p.X = j;
	queue<Node> Q;
	Q.push(p);
	while(!Q.empty()) {
		p = Q.front();Q.pop();
		Temp = -1,Minm = Valu[p.Y][p.X];
		for(int k = 0 ; k < 4 ; k++) {
			q.X = p.X + Dx[k],q.Y = p.Y + Dy[k];
			if (q.X >= 0 && q.X < M && q.Y >= 0 && q.Y < N) {
				if (Valu[q.Y][q.X] < Minm) {
					Temp = k;
					Minm = Valu[q.Y][q.X];
				}
				if (Valu[q.Y][q.X] > Valu[p.Y][p.X] && Map[q.Y][q.X] == 0) {
					Q.push(q);
				}
			}
		}
		
		if (Temp != -1) {
			q.X = p.X + Dx[Temp],q.Y = p.Y + Dy[Temp];
			if (Map[p.Y][p.X] != 0) {
				Map[q.Y][q.X] = Map[p.Y][p.X];
				Q.push(q);
			}
			else {
				Map[p.Y][p.X] = Map[q.Y][q.X];
			}
		}
	}
	
}

int main() {
	freopen("B.txt","r",stdin);
	freopen("B.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	for(int t = 0 ; t < T ; t++) {
		memset(Map,0,sizeof(Map));
		Base = 'a';
		scanf("%d%d",&N,&M);
		for(int i = 0 ; i < N ; i++) {
			for(int j = 0 ; j < M ; j++) {
				scanf("%d",&Valu[i][j]);
			}
		}
		for(int i = 0 ; i < N ; i++) {
			for(int j = 0 ; j < M ; j++) {
				if (Map[i][j] == 0) {
					Map[i][j] = Base;
					Base++;
					Fill(i,j);
				}
			}
		}
		printf("Case #%d:\n",t + 1);
		for(int i = 0 ; i < N ; i++) {
			for(int j = 0 ; j < M ; j++) {
				printf("%c ",Map[i][j]);
			}
			printf("\n");
		}
	}
	
//	while(1);
	return 0;
}
