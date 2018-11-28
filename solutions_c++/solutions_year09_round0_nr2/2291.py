#include<stdio.h>

FILE *fin=fopen("input.txt","r");
FILE *fout=fopen("output.txt","w");

int t,n,m;
int map[100][100];
int chk[100][100];
int qx[10000],qy[10000];
int mov[2][4] = {{-1,0,0,1},{0,-1,1,0}};

int dirc(int sx,int sy){
	int i,min = 99999999;
	int f;
	for(i=0;i<4;i++){
		if(sx+mov[0][i] >= 0 && sx+mov[0][i] < n && sy+mov[1][i] >=0 && sy+mov[1][i] < m && map[sx+mov[0][i]][sy+mov[1][i]] < min){
			min = map[sx+mov[0][i]][sy+mov[1][i]];
			f=i;
		}
	}
	if(min == 99999999 || min >= map[sx][sy]) return -1;
	else return f;
}

void basin(int x,int y,int co){
	int sx=x,sy=y,i;
	int tx,ty;
	int min;
	while(true){
		min = dirc(sx,sy);
		if(min == -1) break;
		sx = sx + mov[0][min];
		sy = sy + mov[1][min];
	}

	int head = 0, tail = 1;
	qx[head] = sx; qy[head] = sy;
	chk[sx][sy] = co;
	while(true){
		tx = qx[head]; ty = qy[head];
		for(i=0;i<4;i++){
			if(tx+mov[0][i] >= 0 && tx+mov[0][i] < n && ty+mov[1][i] >=0 && ty+mov[1][i] < m && chk[tx+mov[0][i]][ty+mov[1][i]]==0){
				min = dirc(tx+mov[0][i],ty+mov[1][i]);
				if(mov[0][i] + mov[0][min] == 0 && mov[1][i] + mov[1][min] == 0 && min != -1){
					qx[tail] = tx+mov[0][i];
					qy[tail] = ty+mov[1][i];
					chk[qx[tail]][qy[tail]]=co;
					tail++;
				}
			}
		}
		head++;
		if(head>=tail) break;
	}
}

void process(int t){
	int i,j,c=97;
	fprintf(fout,"Case #%d:\n",t);
	for(i=0;i<n;i++){
		for(j=0;j<m;j++){
			chk[i][j] = 0;
		}
	}
	for(i=0;i<n;i++){
		for(j=0;j<m;j++){
			if(chk[i][j] == 0){
				basin(i,j,c);
				c++;
			}
		}
	}
	for(i=0;i<n;i++){
		for(j=0;j<m;j++){
			fprintf(fout,"%c ",char(chk[i][j]));
		}
		fprintf(fout,"\n");
	}
}

int main(void){
	int i,j,k;
	fscanf(fin,"%d",&t);
	for(i=1;i<=t;i++){
		fscanf(fin,"%d%d",&n,&m);
		for(j=0;j<n;j++){
			for(k=0;k<m;k++){
				fscanf(fin,"%d",&map[j][k]);
			}
		}
		process(i);
	}
	fcloseall();
	return 0;
}