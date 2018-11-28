#include<stdio.h>
int T, N;
struct SEQ{
	char d[3];
	int p;
}seq[105];

struct Q{
	int pos, x, y;
}q[2000000];

int vis[105][105][105];
int Head, Tail;
int c[3] = {-1,0,1};

int main()
{
	freopen("largeinput.txt", "r", stdin);
	freopen("largeoutput.txt", "w", stdout);
	scanf("%d",&T);
	int t = 0;
	int i, j, k, aa, bb;
	Q sta;
	while(T--)
	{
		++t;

		scanf("%d",&N);
		for(i=1;i<=N;i++) scanf("%s %d",seq[i].d,&seq[i].p);

		for(i=0;i<=N;i++)for(j=0;j<=100;j++)for(k=0;k<=100;k++) vis[i][j][k]=0;
		Head=Tail=0;

		q[Tail].pos = 0; q[Tail].x = 1; q[Tail++].y = 1;
		vis[0][1][1] = 1;
		while(Head != Tail)
		{
			sta = q[Head++];
			j = sta.x;
			k = sta.y;
			
			if(sta.pos == N){
				printf("Case #%d: %d\n",t, vis[sta.pos][j][k]-1);
				break;
			}
			for(aa=0;aa<=2;aa++){
				if(1 > j+c[aa] || j+c[aa] > 100) continue;
				for(bb=0;bb<=2;bb++){
					if(1 > k+c[bb] || k+c[bb] > 100) continue;
					if(vis[sta.pos][j+c[aa]][k+c[bb]]) continue;
					vis[sta.pos][j+c[aa]][k+c[bb]] = vis[sta.pos][j][k] + 1;
					q[Tail].pos = sta.pos;
					q[Tail].x = j+c[aa];
					q[Tail++].y = k+c[bb];
				}
			}
			
			if(seq[sta.pos+1].d[0] == 'O' && seq[sta.pos+1].p == j){
				for(bb=0;bb<=2;bb++){
					if(1 > k+c[bb] || k+c[bb] > 100) continue;
					if(vis[sta.pos+1][j][k+c[bb]]) continue;
					vis[sta.pos+1][j][k+c[bb]] = vis[sta.pos][j][k] + 1;
					q[Tail].pos = sta.pos+1;
					q[Tail].x = j;
					q[Tail++].y = k+c[bb];
				}
			}

			if(seq[sta.pos+1].d[0] == 'B' && seq[sta.pos+1].p == k){
				for(aa=0;aa<=2;aa++){
					if(1 > j+c[aa] || j+c[aa] > 100) continue;
					if(vis[sta.pos+1][j+c[aa]][k]) continue;
					vis[sta.pos+1][j+c[aa]][k] = vis[sta.pos][j][k] + 1;
					q[Tail].pos = sta.pos+1;
					q[Tail].x = j+c[aa];
					q[Tail++].y = k;
				}
			}
		}
	}
	return 0;
}