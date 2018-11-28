#include <stdio.h>
#include <vector>

int resx,resy,d;

int map[500*500];

int totx;
int toty;
int totm;

int blade;
int bladex;
int bladey;

__forceinline void add(int x,int y,int m)
{
    totx += x*map[x+y*resx]*m;
	toty += y*map[x+y*resx]*m;
	totm += map[x+y*resx]*m;
};

void start(int yoffset,int xoffset)
{
	totx=0;
	toty=0;
	totm=0;

	bladex=xoffset;
	bladey=yoffset;
	for(int y=yoffset;y<blade+yoffset;y++)
	{
		int edge=0;
		if (y==yoffset || y==blade+yoffset-1) edge=1;
        for(int x=edge+xoffset;x<blade+xoffset-edge;x++)
		{
            add(x,y,1);                        
		};
	};
};

bool isCenter()
{
	return totx*2 == (bladex*2+blade-1)*totm && toty*2 == (bladey*2+blade-1)*totm;
};

int biggest=0;;

void check()
{
	for(int y=0;y<=resy-blade;y++)
	{
		for(int x=0;x<=resx-blade;x++)
		{
			start(y,x);
			if (isCenter())
			{
//				printf("%d %d: %d\n",x,y,blade);
				if (biggest<blade) 
				{
					biggest=blade;
					return;
				};
			};
		};
	};};

void main(void)
{
	FILE *f = fopen("B-small-attempt0.in","r");

	int T;
	fscanf(f,"%d\n",&T);

	for(int t=0;t<T;t++)
	{
		fscanf(f,"%d%d%d\n",&resy,&resx,&d);

		for(int y=0;y<resy;y++)
		{
            for(int x=0;x<resx;x++)
			{
				char i;
				fscanf(f,"%c",&i);
				map[y*resx+x] = (int)i-'0'+d;
			};
			fscanf(f,"\n");
		};


		biggest=0;
		for(blade=3;blade<=resx && blade<=resy;blade++)
		{
			check();
		
		};


		if (biggest==0)
		{
			printf("Case #%d: IMPOSSIBLE\n",t+1);
		}
		else
		{
			printf("Case #%d: %d\n",t+1,biggest);
		}
	};



};