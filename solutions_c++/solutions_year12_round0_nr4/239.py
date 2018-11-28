#include <cassert>
#include <cstdio>
#include <iostream>
#include <algorithm>


int W=0, H=0, D=0;
bool wall[32][32]={};
int px=0, py=0;


template <class T>
T gcd(T a, T b)
{
	while(b!=0)
	{
		T r=a%b;
		a=b;
		b=r;
	}
	return a;
}


size_t go(int x0, int y0, int dx, int dy)
{
	int mx=0<dx?1:-1;
	int my=0<dy?1:-1;
	dx=std::abs(dx);
	dy=std::abs(dy);
	int x=x0, y=y0;
	for(int t=1; (dx*dx+dy*dy)*t*t<=D*D; ++t)
	{
		int cx=0, cy=0;
		while(cx<dx || cy<dy)
		{
			int ax=dy*(2*cx+1);
			int ay=dx*(2*cy+1);
			bool cross_x=ax<=ay;
			bool cross_y=ay<=ax;
			if(cross_x)
				++cx;
			if(cross_y)
				++cy;
			if(cross_x && cross_y && !wall[y+my][x+mx])
			{
				x+=mx;
				y+=my;
			}
			else
			{
				if(cross_x)
					if(wall[y][x+mx])
						mx*=-1;
					else x+=mx;
				if(cross_y)
					if(wall[y+my][x])
						my*=-1;
					else y+=my;
			}
			if(wall[y][x])
				return 0;
		}
		if(x==x0 && y==y0)
			return 1;
	}
	return 0;
}


int main()
{
	size_t T=0;
	scanf("%zu\n", &T);
	for(size_t t=1; t<=T; ++t)
	{
		scanf("%d %d %d\n", &H, &W, &D);
		px=0; py=0;
		for(int y=0; y<H; ++y)
		{
			for(int x=0; x<W; ++x)
			{
				char c=0;
				scanf("%c", &c);
				assert(c=='.' || c=='#' || c=='X');
				assert(c=='#' || 0<x && x+1<W && 0<y && y+1<H);
				wall[y][x]= c=='#';
				if(c=='X')
				{
					assert(px==0 && py==0);
					px=x;
					py=y;
				}
			}
			scanf("\n");
		}
		assert(px!=0 && py!=0);

		size_t r=0;
		for(int dx=-D; dx<=D; ++dx)
			for(int dy=-D; dy<=D; ++dy)
				if((dx*dx+dy*dy)<=D*D && std::abs(gcd(dx, dy))==1)
					r+=go(px, py, dx, dy);
		printf("Case #%zu: %zu\n", t, r); 
	}
	return 0;
}

