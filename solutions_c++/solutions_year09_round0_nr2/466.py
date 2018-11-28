#include <stdio.h>
char group[26], temp;
int n, m, map[100][100], num[100][100];
int ynum[10000][2], ch[100][100], head, bfs[10000];
bool flow[100][100];
class _LIST{
public:
	int who;
	_LIST *next;
} *list[ 10000 ];
void insert(int x,int y){
	_LIST *mk;
	mk = new _LIST;
	mk->next = list[x];
	list[x] = mk;
	list[x]->who = y;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i, j, k, nn;
	int T, tt;
	scanf("%d",&T);
	for(tt=1;tt<=T;tt++){
		if(tt == 62){
			tt=tt;
		}
		for(i=0;i<26;i++) group[i] = -1;
		scanf("%d %d",&n,&m);
		nn = 0;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				scanf("%d",&map[i][j]);
				num[i][j] = nn;
				ynum[nn][0] = i;
				ynum[nn][1] = j;
				ch[i][j] = -1;
				flow[i][j] = false;
				nn ++;
			}
		}
		int ni, nj, ti, tj, dir[4][2] = { {-1,0}, {0,-1}, {0,1}, {1,0} };
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				ni = nj = -1;
				for(k=0;k<4;k++){
					ti = i+dir[k][0]; tj = j+dir[k][1];
					if(0<=ti && ti<n && 0<=tj && tj<m){
						if(ni == -1 && nj == -1) {
							ni=ti;nj=tj;
						}
						else{
							if(map[ti][tj] < map[ni][nj]){
								ni = ti; nj = tj;
							}
						}
					}
				}
				if(ni != -1 && nj != -1){
					if(map[i][j] > map[ni][nj]){
						insert(num[ni][nj], num[i][j]);
						flow[i][j] = true;
					}
				}
			}
		}
		nn = 0;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(!flow[i][j]){
					bfs[0] = num[i][j];
					head = 1;
					for(k=0;k<head;k++){
						ch[ ynum[ bfs[k] ][0] ][ ynum[ bfs[k] ][1] ] = nn;
						_LIST *I;
						for(;list[bfs[k]]!=NULL;){
							bfs[head++] = list[bfs[k]]->who;
							I = list[bfs[k]];
							list[bfs[k]] = list[bfs[k]]->next;
							delete I;
						}
					}
					nn++;
				}
			}
		}
		temp = 'a';
		printf("Case #%d:\n",tt);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(group[ch[i][j]] == -1){
					group[ ch[i][j] ] = temp;
					temp ++;
				}
				if(j == m-1)	printf("%c\n",group[ch[i][j]]);
				else	printf("%c ",group[ch[i][j]]);
			}
		}
	}
	return 0;
}