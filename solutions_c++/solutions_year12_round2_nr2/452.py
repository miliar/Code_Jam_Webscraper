#include<cstdio>
#include<algorithm>

using namespace std;
const int MAX = 13;
const int MHEIGHT = 1100;
const int INF = (1<<29);

bool flag;
int dy[] = {1, 0, -1, 0};
int dx[] = {0, 1, 0, -1};
int H, rows, columns, casos, d[MAX][MAX], u[MAX][MAX];
int m[MAX][MAX][MHEIGHT];

int inside(int y, int x){
	if(y<0 || x<0 || y >= rows || x >= columns) return 0;
	else return 1;
}

int ok(int y1, int x1, int y2, int x2, int w){
	if(!inside(y2, x2)) return 0;

	int piso1 = max(d[y1][x1], w);
	int piso2 = max(d[y2][x2], w);
	int teto1 = u[y1][x1];
	int teto2 = u[y2][x2];
	if(teto2-piso2 < 50) return 0; //casos 1 3
	if(teto2-piso1 < 50) return 0; //casos 2
	if(teto1-piso2 < 50) return 0; //casos 4
	return 1;
}

void f(int y, int x, int t){
	int ny, nx;

	m[y][x][t] = INF; //INF=processando
	if(y == rows-1 && x == columns-1){
		m[y][x][t] = 0;
		return ;
	}
	if(t-1 >= 0 && m[y][x][t-1] == -1) f(y, x, t-1);//wait
	if(t-1 >= 0) m[y][x][t] = 1+m[y][x][t-1];
	for(int i=0;i<4;i++){
		ny = y + dy[i];
		nx = x + dx[i];
		if(ok(y, x, ny, nx, t)){
			//if(flag) printf("OK at %d %d %d inside %d %d\n", ny, nx, t, rows, columns);
			if(m[ny][nx][t] == -1) f(ny, nx, t);
			if(t == H) m[y][x][t] = min(m[ny][nx][t], m[y][x][t]);
			if(t-d[y][x] >= 20) m[y][x][t] = min(10+m[ny][nx][max(0, t-10)], m[y][x][t]);
			else m[y][x][t] = min(100+m[ny][nx][max(0, t-100)], m[y][x][t]);
		}
	}
	//if(flag && t == H) printf("%d %d %d -> %d\n", y, x, t, m[y][x][t]);
	//if(t <= 200) printf("%d %d %d -> %d\n", y, x, t, m[y][x][t]);
}

int main(){
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
	flag = (inst==3)?true:false;
	scanf(" %d %d %d", &H, &rows, &columns);
	for(int i=0;i<rows;i++)
		for(int j=0;j<columns;j++)
			scanf(" %d", &u[i][j]);
	for(int i=0;i<rows;i++)
		for(int j=0;j<columns;j++)
			scanf(" %d", &d[i][j]);
	
	for(int i=0;i<MAX;i++)
		for(int j=0;j<MAX;j++)
			for(int k=0;k<MHEIGHT;k++)
				m[i][j][k] = -1;
	f(0, 0, H);
	/*if(inst == 1) */printf("Case #%d: %lf\n", inst, (double)m[0][0][H]/10.0);
	}
	return 0;
}

