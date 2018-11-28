#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>
#define infile "a2.in"
#define outfile "a2.out"

const long maxheight = 10010;
const long dx[4]={-1,0,0,1};
const long dy[4]={0,-1,1,0};

struct Tpx{
	long x,y;
}*px[maxheight];

long map[150][150],sink[150][150],
	bh[100],ge[maxheight],m,n;
char result[150][150];

FILE *fin=fopen(infile,"r"),
	*fout=fopen(outfile,"w");

void init()
{	
}

void work()
{
	long w,i,j,k,x,y,qx,qy,sinknum,testnum,tx,ty;
	fscanf(fin,"%ld", &testnum);
	for (w=1; w<=testnum; ++w)
	{
		fscanf(fin,"%ld%ld",&m,&n);
		sinknum=0;
		for (i=0; i<maxheight; ++i)
			ge[i]=0;
		for (i=1; i<=m; ++i)
			for (j=1; j<=n; ++j)
			{
				fscanf(fin,"%ld",&map[i][j]);
				++ge[map[i][j]];
			}

		for (i=0; i<maxheight; ++i)
		{
			px[i]=new Tpx[ge[i]+1];
			ge[i]=0;
		}

		for (i=1; i<=m; ++i)
			for (j=1; j<=n; ++j)
			{
				k=map[i][j];
				++ge[k];
				px[k][ge[k]].x=i;
				px[k][ge[k]].y=j;
			}

		for (i=0; i<maxheight; ++i)
		{
			for (j=1; j<=ge[i]; ++j)
			{
				x=px[i][j].x;
				y=px[i][j].y;

				qx=qy=-1;
				for (k=0; k<4; ++k)
				{
					tx=x+dx[k];
					ty=y+dy[k];
					if ((tx>=1)&&(tx<=m)&&(ty>=1)&&(ty<=n))
						if ((qx==-1)||(map[tx][ty]<map[qx][qy]))
						{
							qx=tx;
							qy=ty;
						}
				}

				if ((qx>=1)&&(map[qx][qy]<map[x][y]))
				{
					sink[x][y]=sink[qx][qy];
				}
				else sink[x][y]=(++sinknum);
			}
		}

		for (i=1; i<=sinknum; ++i)
			bh[i]=-1;
		long now=0;
		for (i=1; i<=m; ++i)
			for (j=1; j<=n; ++j)
			{
				k=sink[i][j];
				if (bh[k]!=-1)
					result[i][j]=bh[k]+'a';
				else {
					bh[k]=(now++);
					result[i][j]=bh[k]+'a';
				}
			}

		fprintf(fout, "Case #%ld:\n",w);
		for (i=1; i<=m; ++i)
			for (j=1; j<=n; ++j)
			{
				fprintf(fout,"%c", result[i][j]);
				if (j==n)
					fprintf(fout,"\n");
				else fprintf(fout," ");
			}

		for (i=0; i<maxheight; ++i)
			delete px[i];

	}
	fclose(fin);
	fclose(fout);
}

void output()
{

}

int main()
{
	init();
	work();
	output();	
	return 0;
}