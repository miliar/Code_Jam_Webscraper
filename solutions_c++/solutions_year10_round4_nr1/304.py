#include <iostream>
using namespace std;
int i,j,n,m,curcase = 1 , testcase ,minsize,k,tmp,S,q,p;
char G[300][300];
bool check_cell(int x,int y,int xx, int yy)
{
	int ret = 0;
	if ((G[x][y]=='?')||(G[x][y]==' ')) return true;
	int xxx = 2*xx-x,yyy = 2*yy-y;
	if ((xxx<1)||(yyy<1)||(xxx>=300)||(yyy>=300)) ret++; else 
	if ((G[xxx][yyy]=='?')||(G[xxx][yyy]==' ')) ret++; else 
	if (G[xxx][yyy]==G[x][y]) ret++;
	xxx = 2*xx-x,yyy = y;
	if ((xxx<1)||(yyy<1)||(xxx>=300)||(yyy>=300)) ret++; else
	if ((G[xxx][yyy]=='?')||(G[xxx][yyy]==' ')) ret++; else 
	if (G[xxx][yyy]==G[x][y]) ret++;
	xxx = x,yyy = 2*yy-y;
	if ((xxx<1)||(yyy<1)||(xxx>=300)||(yyy>=300)) ret++; else
	if ((G[xxx][yyy]=='?')||(G[xxx][yyy]==' ')) ret++; else
	if (G[xxx][yyy]==G[x][y]) ret++;
	if (ret==3) return true ; else return false;
}
bool check(int q,int p)
{
	int i,j;
	for ( i = 1 ; i < 2*n ; i++ )
			for ( j = 1 ; j < 2*n ; j++ )
				if (check_cell(i,j,q,p)==false) return false;
	return true;
}
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	for ( scanf("%d\n",&testcase) ; curcase <= testcase ; curcase++ )
	{
		scanf("%d",&n);
		scanf("%c",&G[0][0]);
		for ( i = 0 ; i < 300 ; i++ )
			for ( j = 0 ; j < 300 ; j++ )
				G[i][j] = '?';
		minsize = 1000000;
		for ( i = 1 ; i < 2*n ; i++ )
		{
			if ( i <= n )
			{
				for ( j = 1 ; j <= n+i-1 ; j++ )
					scanf("%c",&G[i][j]);
			} else
			{
				for ( j = 1 ; j <= n+2*n-i-1 ; j++ )
					scanf("%c",&G[i][j]);
			}
			scanf("%c",&G[0][0]);
			G[0][0] = '?';
		}
		for ( i = 1 ; i < 2*n ; i++ )
			for ( j = 1 ; j < 2*n ; j++ )
				if (check(i,j))
				{				
					q=i-1;
					p=j-1;
					S=max(abs(q-p),abs(q+p+2-2*n));
					if (!(n%2))
						if(!(S%2)) tmp = (n/2+S/2)*2;
							else tmp = 2*(n/2+S/2)+1;
					else 
						if (!(S%2)) tmp = 2*(n/2+S/2)+1;
							else tmp = 2*(n/2+S/2+1);
					minsize = min(minsize,tmp);
				}
		printf("Case #%d: %d\n",curcase,minsize*minsize-n*n);
	}
}
