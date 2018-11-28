#include <stdio.h>
#include <string.h>
#include <vector>

using namespace std;


#define MAX_H 200
#define MAX_W 200

int H,W;
int kotak[MAX_H][MAX_W];
int no[MAX_H][MAX_W];
int gno[MAX_H][MAX_W];
bool isroot[MAX_H][MAX_W];
vector<int> child[MAX_H][MAX_W];

const int incy[] = {-1,0,0,1};
const int incx[] = {0,-1,1,0};

void addchild(int y, int x)
{
	int i;
	int mine=kotak[y][x];
	int theinc = -1;
	int ay=y,ax=x;
	for (i=0; i<4; i++)
	{
		int ny,nx;
		ny=y+incy[i];
		nx=x+incx[i];
		if (ny<0 || ny>=H || nx<0 || nx>=W)
			continue;
		if (kotak[ny][nx]<mine) {
			mine=kotak[ny][nx];
			if (i==0)
				theinc=3;
			else if (i==3)
				theinc=0;
			else if (i==1)
				theinc=2;
			else
				theinc=1;
			ay=ny;
			ax=nx;
		}
	}
	if (ax==x && ay==y)
		return;
	//printf("%d %d -> %d %d\n",y,x,ay,ax);
	child[ay][ax].push_back(theinc);
	isroot[y][x]=0;
}

void bfs(int y, int x,int theno)
{
//	printf("mark %d %d %d\n",y,x,theno);
	if (no[y][x]!=0)
		return;
	no[y][x]=theno;
	int i;
	for (i=0; i<child[y][x].size(); i++)
	{
		int n=child[y][x][i];
		int ny,nx;
		ny=y+incy[n];
		nx=x+incx[n];
		if (ny<0 || ny>=H || nx<0 || nx>=W)
			continue;
		bfs(ny,nx,theno);
	}
}

void gbfs(int y, int x, int gcol, int col)
{
	if (no[y][x]!=col)
		return;
	if (gno[y][x]!=0)
		return;
	gno[y][x]=gcol;
	int i;
	for (i=0; i<4; i++)
	{
		int ny,nx;
		ny=y+incy[i];
		nx=x+incx[i];
		if (ny<0 || ny>=H || nx<0 || nx>=W)
			continue;
		gbfs(ny,nx,gcol,col);
	}	
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,t;
	scanf("%d", &T);
	for (t=1; t<=T; t++)
	{
		int y,x;
		scanf("%d %d", &H, &W);
		for (y=0; y<H; y++)
		{
			for (x=0; x<W; x++)
			{
				scanf("%d", &kotak[y][x]);
				child[y][x].clear();
			}
		}
		memset(gno,0,sizeof(gno));
		memset(no,0,sizeof(no));
		memset(isroot,1,sizeof(isroot));
		int ncol=0;
		for (y=0; y<H; y++)
		{
			for (x=0; x<W; x++)
			{
				addchild(y,x);
			}
		}
		for (y=0; y<H; y++)
		{
			for (x=0; x<W; x++)
			{
				if (isroot[y][x])
					bfs(y,x,++ncol);
			}
		}
		int gcol=0;
		for (y=0; y<H; y++)
		{
			for (x=0; x<W; x++)
			{
				if (gno[y][x]==0)
					gbfs(y,x,++gcol,no[y][x]);
			}
		}
		printf("Case #%d:\n",t);
		for (y=0; y<H; y++)
		{
			for (x=0; x<W; x++)
			{
				if (x==0)
					printf("%c",gno[y][x]+'a'-1);
				else
					printf(" %c",gno[y][x]+'a'-1);
			}
			printf("\n");
		}
	}
	return 0;
}