#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int alt[110][110];
//char table[110][110];
int grp[10010];
char mapping[10010];

int find(int a)
{
	if ( grp[a] < 0 ) return a;
	grp[a] = find(grp[a]);
	return grp[a];
}

void join(int a, int b)
{
	a = find(a);
	b = find(b);
	if ( a == b ) return;
	grp[a] = b;
}

int main()
{
	int aa, nn, h, w, i, j, m, a, b;
	char c;
	scanf("%d",&nn);
	
	for ( aa = 1; aa <= nn; aa++ )
	{
		scanf("%d %d",&h,&w);
		memset(grp,-1,sizeof(grp));
		memset(mapping,0,sizeof(mapping));
		
		for ( i = 0; i < 110; i++ )
		{
			alt[i][0] = alt[0][i] = 20000;
			alt[i][w+1] = alt[h+1][i] = 20000;
		}
		
		for ( i = 1; i <= h; i++ )
		{
			for ( j = 1; j <= w; j++ )
			{
				scanf("%d",&alt[i][j]);
			} 
		}
		
		for ( i = 1, a = 0; i <= h; i++ )
		{
			for ( j = 1; j <= w; j++, a++ )
			{
				m = alt[i-1][j];
				/*
				m = min(m,alt[i+1][j]);
				m = min(m,alt[i][j-1]);
				m = min(m,alt[i][j+1]);
				*/
				if ( m > alt[i+1][j]) m = alt[i+1][j];
				if ( m > alt[i][j-1]) m = alt[i][j-1];
				if ( m > alt[i][j+1]) m = alt[i][j+1];
				
				if ( m >= alt[i][j] ) continue;				
				
				if ( m == alt[i-1][j] ) b = (i-2)*w + (j-1);
				else if ( m == alt[i][j-1] ) b = (i-1)*w + (j-2);
				else if ( m == alt[i][j+1] ) b = (i-1)*w + (j);
				else if ( m == alt[i+1][j] ) b = (i)*w + (j-1);
				
				//printf("%d,%d ",m,b);
				join(a,b);
			}
			//puts("");
		}
		
		printf("Case #%d:\n",aa);

		for ( i = 1, a = 0, c = 'a'; i <= h; i++ )
		{
			b = find(a);
			if ( mapping[b] == 0 ) mapping[b] = c++;
			printf("%c",mapping[b]);
			//printf("%d",grp[a]);
			a++;
			
			for ( j = 2; j <= w; j++, a++ )
			{
				b = find(a);
				if ( mapping[b] == 0 ) mapping[b] = c++;
				printf(" %c",mapping[b]);
				//printf(" %d",grp[a]);
			}
			puts("");
		}
	}
	return 0;
}
