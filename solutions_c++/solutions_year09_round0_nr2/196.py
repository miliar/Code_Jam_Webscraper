#include<cstdio>
#include<cstring>
int map[100][100];
char s[100][100];
int H, W;
char cN;

int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

void calc(int x, int y){
	if (s[x][y]!='\0')
		return;
	int mina=4, minr=map[x][y];
	int i;
	int nx,ny;
	for (i=0;i<4;i++){
		nx=x+dir[i][0];
		ny=y+dir[i][1];
		if (nx>=0&&ny>=0&&nx<H&&ny<W)
			if (map[nx][ny]<minr){
				minr = map[nx][ny];
				mina = i;
			}
	}
	if (mina==4)
		s[x][y] = cN++;
	else {
		calc(x+dir[mina][0],y+dir[mina][1]);
		s[x][y] = s[x+dir[mina][0]][y+dir[mina][1]];
	}
}

int main(){
	int i,j;

	int T,t;

	scanf("%d",&T);
	for (t=1;t<=T;t++){
		scanf("%d%d", &H, &W);
		for (i=0;i<H;i++)
			for (j=0;j<W;j++)
				scanf("%d", &map[i][j]);
		memset(s, 0, sizeof(s));
		cN = 'a';
		for (i=0;i<H;i++)
			for (j=0;j<W;j++)
				calc(i, j);
		printf("Case #%d:\n", t);
		for (i=0;i<H;i++){
			printf("%c", s[i][0]);
			for (j=1;j<W;j++)
				printf(" %c",s[i][j]);
			printf("\n");
		}
	}

	return 0;
}
