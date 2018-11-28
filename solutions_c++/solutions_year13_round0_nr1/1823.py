#include <stdio.h>


char m[4][5];

int win(char cc)
{
	int i,j;
	int ret;
	for ( i=0;i<4;++i )
	{
		ret = 1;
		for ( j=0;j<4 && ret;++j )
		{
			if ( m[i][j] != cc && m[i][j] != 'T' )
				ret = 0;
		}
		if ( ret ) return ret;
	}
	for ( i=0;i<4;++i )
	{
		ret = 1;
		for ( j=0;j<4 && ret;++j )
		{
			if ( m[j][i] != cc && m[j][i] != 'T' )
				ret = 0;
		}
		if ( ret ) return ret;
	}
	ret = 1;
	for ( i=0;i<4&&ret;++i )
		if ( m[i][i] != cc && m[i][i] != 'T' )
			ret = 0;
	if ( ret ) return ret;
	ret = 1;
	for ( i=0;i<4&&ret;++i )
		if ( m[i][3-i] != cc && m[i][3-i] != 'T' )
			ret = 0;
	return ret;
}
int isend()
{
	int i,j;
	for ( i=0;i<4;++i )
		for ( j=0;j<4;++j )
			if ( m[i][j] == '.' )
				return false;
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,st;
	int i,j;
	scanf("%d",&st);
	for ( t=1;t<=st;++t )
	{
		for ( i=0;i<4;++i )
		{
			scanf("%s",m[i]);
		}
		if ( win('X') )
		{
			printf("Case #%d: X won\n",t);
		}
		else if ( win('O') )
		{
			printf("Case #%d: O won\n",t);
		}
		else if ( isend() )
		{
			printf("Case #%d: Draw\n",t);
		}
		else
		{
			printf("Case #%d: Game has not completed\n",t);
		}
	}
}
