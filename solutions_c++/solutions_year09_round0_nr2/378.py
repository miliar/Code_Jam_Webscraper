#include<stdio.h>


int T, W, H;
int dat[101][101];
int graph[101][101][4];
int check[101][101];
int mapping[10000];
int r, cnt;



int getmin(int x, int y)
{
	int min = dat[x][y];
	int mx, my;
	int ret = -1;

	if(x-1 >= 0) if( min > dat[x-1][y])
	{
		ret = 0;
		min = dat[x-1][y];
	}
	if(y-1 >= 0) if( min > dat[x][y-1])
	{
		ret = 1;
		min = dat[x][y-1];
	}
	if(y+1 < W) if( min > dat[x][y+1])
	{
		ret = 2;
		min = dat[x][y+1];
	}
	if(x+1 < H) if( min > dat[x+1][y])
	{
		ret = 3;
		min = dat[x+1][y];
	}
	
	return ret;
}
void solve()
{
	int i,j,ret,k,l, r;


	for(i=0;i<H;i++) for(j=0;j<W;j++) check[i][j] = i*W+j;
	for(i=0;i<H;i++) for(j=0;j<W;j++) for(k=0;k<4;k++) graph[i][j][k] = 0;

	for(i=0;i<H;i++) for(j=0;j<W;j++)
	{
		ret = getmin(i,j);
		if(ret == -1) continue;
		graph[i][j][ret] = 1;

		if(ret == 0) graph[i-1][j][3] = 1;
		if(ret == 1) graph[i][j-1][2] = 1;
		if(ret == 2) graph[i][j+1][1] = 1;
		if(ret == 3) graph[i+1][j][0] = 1;
	}

	for(i=0;i<W*H;i++)
	{
		for(j=0;j<H;j++)
		{
			for(k=0;k<W;k++)
			{
				if(graph[j][k][0] == 1 && check[j-1][k] > check[j][k]) check[j-1][k] = check[j][k];
				if(graph[j][k][1] == 1 && check[j][k-1] > check[j][k]) check[j][k-1] = check[j][k];
				if(graph[j][k][2] == 1 && check[j][k+1] > check[j][k]) check[j][k+1] = check[j][k];
				if(graph[j][k][3] == 1 && check[j+1][k] > check[j][k]) check[j+1][k] = check[j][k];
			}
		}
	}

	for(i=0;i<10000;i++) mapping[i] = 0;
	r = 'a';
	for(i=0;i<H;i++)
	{
		for(j=0;j<W;j++)
		{
			if(mapping[ check[i][j] ] == 0) {mapping[ check[i][j] ] = r; check[i][j] = r; r++;}
			else
			{
				check[i][j] = mapping[ check[i][j] ];
			}
		}
	}

}

int main()
{
	int i,j,k;
	FILE *fp, *fp1;
	fp = fopen("B.in","r");
	fp1= fopen("B.out","w");
	fscanf(fp,"%d",&T);

	for(i=0;i<T;i++)
	{
		fscanf(fp,"%d %d",&H,&W);

		for(j=0;j<H;j++) for(k=0;k<W;k++) fscanf(fp, "%d",&dat[j][k]);

		solve();
		fprintf(fp1,"Case #%d:\n",i+1);
		for(j=0;j<H;j++) 
		{
			for(k=0;k<W;k++) fprintf(fp1,"%c ",check[j][k]);
			fprintf(fp1,"\n");
		}
	}
}