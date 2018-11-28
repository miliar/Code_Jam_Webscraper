#include<cstdio>

const int MOD = 1000003;

int a[10005],e[10005];

int find( int x )
{
	if( a[x]==0 ) return x;else
		return a[x] = find(a[x]);
}
char s[1000];

int R,C,n;

int getcor( int x,int y )
{
	x = ( x + 2*R -1 ) % R  + 1;
	y = ( y + 2*C -1 ) % C  + 1;
	return (x-1)*C + y;
}
int main()
{
	int T=0,TT;
	scanf("%d",&TT);
	int p1,p2;
	int ans;
	while(TT--)
	{
		printf("Case #%d: ",++T);
		scanf("%d%d",&R,&C);
		n = R*C;
		for( int i = 1;i<=n;i++ )
		{
			e[i] = -1;
			a[i] = 0;
		}

		gets(s);
		for( int i = 1;i<=R;i++ )
		{
			gets(s+1);
			for( int j = 1;j<=C;j++ )
			{
				if( s[j] == '-' )
				{
					p1 = getcor(i,j-1);p2 = getcor(i,j+1);
				}else
				if( s[j] == '|' )
				{
					p1 = getcor(i+1,j);p2 = getcor(i-1,j);
				}else
				if( s[j] == '/' )
				{
					p1 = getcor( i-1,j+1 );p2 = getcor( i+1,j-1 );
				}else
				if( s[j] == '\\' )
				{
					p1 = getcor( i-1,j-1 );p2 = getcor( i+1,j+1 );
				}

				p1 = find(p1);p2 = find(p2);
				if( p1!=p2 )
				{
					a[p1] = p2;
					e[p2] += e[p1];
				}
				e[p2] ++;
			}
		}

		ans = 1;
		for( int i = 1;i<=n;i++ ) if( a[i]==0 )
			if(e[i]!=0) ans =0;else ans = (ans*2)%MOD;
		printf("%d\n",ans);
	}
	return 0;
}
