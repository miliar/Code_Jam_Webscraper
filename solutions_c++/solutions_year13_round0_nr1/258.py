#include <cstdio>
typedef unsigned int uint;

uint const N=4;
char A[N][N+1];

bool check(int x,int y,int dx,int dy,char p)
{
	uint c=0;
	for(uint i=0; i<N; ++i,x+=dx,y+=dy)
		c+=A[y][x]=='T' || A[y][x]==p;
	return c==N;
}

bool check(char p)
{
	for(uint i=0; i<N; ++i)
		if(check(0,i,1,0,p) || check(i,0,0,1,p))
			return 1;
	return check(0,0,1,1,p) || check(0,N-1,1,-1,p);
}

int main()
{
	uint T=0;
	scanf("%u\n", &T);
	for(uint t=1; t<=T; ++t)
	{
		for(uint i=0; i<N; ++i)
			scanf("%s",A[i]);
		if(check('X'))
			printf("Case #%u: X won\n",t); 
		else if(check('O'))
			printf("Case #%u: O won\n",t); 
		else
		{
			uint dots=0;
			for(uint y=0; y<N; ++y)
				for(uint x=0; x<N; ++x)
					dots+=A[y][x]=='.';
			if(dots)
				printf("Case #%u: Game has not completed\n",t); 
			else printf("Case #%u: Draw\n",t); 
		}
	}
	return 0;
}

