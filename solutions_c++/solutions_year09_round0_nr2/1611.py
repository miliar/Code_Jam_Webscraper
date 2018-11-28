//B.cpp
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
const int dx[5] = {-1 , 0 , 0 , 1 , 0};
const int dy[5] = {0 , -1 , 1 , 0 , 0};
int T;
int h , w , d;
int a[10000];
int father[10000];
bool b[10000];
char c[10000];
char t;
int getfather(const int x)
{
	return x==father[x] ? father[x] : father[x] = getfather(father[x]);
}
int main()
{
	freopen("input.txt" , "r" , stdin);
	freopen("output.txt" , "w" , stdout);
	int cas = 0;
	for ( scanf("%d" , &T) ; T-- ; )
	{
		scanf("%d%d" , &h , &w);
		for ( int i=0 ; i<h ; ++i ) 
			for ( int j=0 ; j<w ; ++j )
			{
				scanf("%d" , &a[i*w+j]);
				father[i*w+j] = i * w + j;
			}
		for ( int i=0 ; i<h ; ++i ) 
			for ( int j=0 ; j<w ; ++j ) 
			{
				d = 4;
				for ( int k=0 ; k<4 ; ++k )
					if ( 0<=i+dx[k] && i+dx[k]<h
					&& 0<=j+dy[k] && j+dy[k]<w 
					&& a[(i+dx[k])*w+j+dy[k]] < a[(i+dx[d])*w+j+dy[d]] ) 
						d = k;
				father[i*w+j] = getfather((i+dx[d])*w+j+dy[d]);
			}
		for ( int i=0 ; i<h ; ++i ) 
			for ( int j=0 ; j<w ; ++j ) 
				father[i*w+j] = getfather(i*w+j);
		memset(b , 0 , sizeof(b));
		t = 'a';
		for ( int i=0 ; i<h ; ++i )
			for ( int j=0 ; j<w ; ++j ) 
			{
				if ( !b[father[i*w+j]] ) 
				{
					b[father[i*w+j]] = true;
					c[father[i*w+j]] = t;
					++t;
				}
				c[i*w+j] = c[father[i*w+j]];
			}
		printf("Case #%d:\n" , ++cas);
		for ( int i=0 ; i<h ; ++i ) 
		{
			putchar(c[i*w]);
			for ( int j=1 ; j<w ; ++j ) 
			{
				putchar(' ');
				putchar(c[i*w+j]);
			}
			putchar('\n');
		}
	}
	return 0;
}
