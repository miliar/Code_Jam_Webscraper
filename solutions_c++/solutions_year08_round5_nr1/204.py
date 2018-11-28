#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define MAXN 300

int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};

int hx[2][4] = {0,0,1,1,0,1,1,0};
int hy[2][4] = {0,1,1,0,1,1,0,0};

bool mrk[MAXN][MAXN];

int n;
int x[MAXN*MAXN],y[MAXN*MAXN];

int rep;
char buf[MAXN];
int len;

int nx[MAXN][MAXN][4];
int ny[MAXN][MAXN][4];
bool pock[MAXN][MAXN][4];

long long ret;

long long mod(long long d){
	if(d < 0) return -d;
	return d;
}

void calc(int x,int y,int d){
	if(nx[x][y][d] >= 0){
		pock[x][y][d] = true;
		return ;
	}
	if(nx[x][y][d] <= -10) return ;
	
	if(mrk[x+hx[0][d]][y+hy[0][d]] && mrk[x+hx[1][d]][y+hy[1][d]]){
		pock[x][y][d] = true;
		//printf("%d %d %d\n",x,y,d);
		nx[x][y][d] = x;
		ny[x][y][d] = y;
		return ;
	}
	
	calc(x+dx[d],y+dy[d],d);
	nx[x][y][d] = nx[x+dx[d]][y+dy[d]][d];
	ny[x][y][d] = ny[x+dx[d]][y+dy[d]][d];
	pock[x][y][d] = pock[x+dx[d]][y+dy[d]][d]; 
	
}

int main(){
	
	int i,j,k,h;
	int t,lp;
	int dir,px,py;
	long long hlp;
	bool add;
	
	scanf("%d",&t);
	
	for(lp=1;lp<=t;lp++){
		
		for(i=0;i<MAXN;i++){
			for(j=0;j<MAXN;j++){
				mrk[i][j] = false;
				for(k=0;k<4;k++){
					nx[i][j][k] = -1;
					pock[i][j][k] = false;
				}
			}
		}
		
		for(i=0;i<MAXN;i++){
			/*
			nx[0][i][0] = -10;
			nx[MAXN-1][i][2] = -10;
			nx[i][0][3] = -10;
			nx[i][MAXN-1][1] = -10;
			*/
			for(k=0;k<4;k++){
				nx[0][i][k] = -10;
				nx[MAXN-1][i][k] = -10;
				nx[i][0][k] = -10;
				nx[i][MAXN-1][k] = -10;
			}
		}
		
		px = MAXN/2;
		py = MAXN/2;
		mrk[px][py] = true;
		dir = 1;
		x[0] = px;
		y[0] = py;
		n = 1;
		
		scanf("%d",&k);
		
		for(i=0;i<k;i++){
			scanf("%s %d",buf,&rep);
			for(j=0;j<rep;j++){
				len = strlen(buf);
				for(h=0;h<len;h++){
					if(buf[h] == 'F'){
						px += dx[dir];
						py += dy[dir];
						x[n] = px;
						y[n] = py;
						n++;
						mrk[px][py] = true;
					}
					else if(buf[h] == 'L'){
						dir--;
						if(dir < 0) dir = 3;
					}
					else{
						dir++;
						if(dir > 3) dir = 0;
					}
				}
			}
		}
		
		ret = 0;
		//printf("oi\n");
		for(i=0;i<MAXN;i++){
			for(j=0;j<MAXN;j++){
				for(k=0;k<4;k++){
					calc(i,j,k);
				}
				if((pock[i][j][0] && pock[i][j][2]) || (pock[i][j][1] && pock[i][j][3])) ret++;
			}
		}
		//printf("oi\n");
		
		hlp = 0;
		for(i=0;i<n-1;i++){
			hlp += x[i]*y[(i+1)%n] - x[(i+1)%n]*y[i];
		}
		hlp = mod(hlp)/2;
		//printf("%d %d\n",ret,hlp);
		ret -= hlp;
		/*
		printf("%d\n",hlp);
		for(i=0;i<n;i++){
			printf("%d %d\n",x[i],y[i]);
		}*/
		
		printf("Case #%d: %d\n",lp,ret);
		
	}
	
	return 0;
	
}