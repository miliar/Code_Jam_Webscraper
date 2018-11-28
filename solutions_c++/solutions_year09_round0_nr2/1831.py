#include <cstdio>
#include <string.h>
#include <stdlib.h>

using namespace std;

#define max(x,a) ((x)>(a)?(x):(a))
#define min(x,a) ((x)<(a)?(x):(a))

int Bas[200][200];
int W,H,dx,dy;
int _dx[5]={0,-1,1,0,0};
int _dy[5]={-1,0,0,1,0};

void SetDir(int x,int y)
{
	int h[4],d=4;
	int a=Bas[y][x];
	h[0]=(y>0?Bas[y-1][x]:3e4);
	h[1]=(x>0?Bas[y][x-1]:3e4);
	h[2]=(x+1<W?Bas[y][x+1]:3e4); 
	h[3]=(y+1<H?Bas[y+1][x]:3e4);
	for(int i=0;i<4;i++)
	{
		if(h[i]<a)
		{
			a=h[i];
			d=i;
		}
	}
	dx=_dx[d];
	dy=_dy[d];
}

char Sink[100][100];

void NameSinks()
{
	char c=1;
	for(int i=0;i<H;i++)
	{
		for(int j=0;j<W;j++)
		{
			Sink[i][j]=0;
			SetDir(j,i);
			if(dx==0 && dy==0)
			{
				Sink[i][j]=c;
				c++;
			}
		}
	}
}

void Cell(int _x,int _y)
{
	int x=_x,y=_y;
	SetDir(x,y);
	while(dx!=0 || dy!=0)
	{
		x+=dx;y+=dy;
		if(Sink[y][x]) break;
		SetDir(x,y);
	}
	char c=Sink[y][x];
	x=_x,y=_y;
	SetDir(x,y);
	while(dx!=0 || dy!=0)
	{
		Sink[y][x]=c;
		x+=dx;y+=dy;
		if(Sink[y][x]) break;
		SetDir(x,y);
	}
}

char Voc[30];

void cVoc()
{
	int i,j,k;
		for(k=0;k<30;k++)
		{	
			Voc[k]=0;
		}
	char c='a';
	for(int i=0;i<H;i++)
	{
		for(int j=0;j<W;j++)
		{
			//if(Sink[i][j]>30) continue;
			if(Voc[Sink[i][j]]==0)
			{
				Voc[Sink[i][j]]=c++;
			}
			Sink[i][j]=Voc[Sink[i][j]];
		}
	}
}

int main()
{
	long i,j,k,T;

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	char S[10000];
	scanf("%d",&T);

	
	char *l;
	for(i=0;i<T;i++)
	{
		scanf("%d%d",&H,&W);

		for(j=0;j<H;j++)
			for(k=0;k<W;k++)
				scanf("%d",&Bas[j][k]);

		NameSinks();

		for(int k=0;k<H;k++)
		{
			for(int j=0;j<W;j++)
			{
				if(Sink[k][j]==0) Cell(j,k);
			}
		}

		cVoc();
		printf("Case #%d:\n",i+1);
		for(k=0;k<H;k++)
		{
			for(j=0;j<W;j++)
			{
				printf("%c ",Sink[k][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
