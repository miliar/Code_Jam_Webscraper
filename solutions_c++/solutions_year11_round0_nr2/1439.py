#include <cstdio>
#include <cstring>

const int N=110;

int n,m,tt,ca;
char a[N],ans[N];
char v[N][N];
bool vv[N][N];

int main()
{
	freopen( "B-large.in","r",stdin );
	freopen( "B-large.out","w",stdout );
	scanf( "%d",&tt );
	while ( tt-- )
	{
		for ( int i=0;i<26;i++ )
			for ( int j=0;j<26;j++ )
			{
				v[i][j]=0;
				vv[i][j]=0;
			}
		
		scanf( "%d",&n );
		for ( int i=1;i<=n;i++ )
		{
			scanf( "%s",a );
			v[a[0]-'A'][a[1]-'A']=v[a[1]-'A'][a[0]-'A']=a[2];
		}
		scanf( "%d",&n );
		for ( int i=1;i<=n;i++ )
		{
			scanf( "%s",a );
			vv[a[0]-'A'][a[1]-'A']=vv[a[1]-'A'][a[0]-'A']=1;		
		}
		scanf( "%d",&n );
		scanf( "%s",a );

		m=0;
		for ( int i=0;i<n;i++ )
		{
			ans[m++]=a[i];
			while ( m>1 && v[ans[m-2]-'A'][ans[m-1]-'A']!=0 )
			{
				ans[m-2]=v[ans[m-2]-'A'][ans[m-1]-'A'];
				m--;
			}
			for ( int j=m-2;j>=0;j-- )
				if ( vv[ans[j]-'A'][ans[m-1]-'A'] )
				{
					m=0;
					break;
				}
		}
		printf( "Case #%d: [",++ca );
		for ( int i=0;i<m;i++ )
		{
			if ( i!=0 ) printf( " " );
			printf( "%c",ans[i] );
			if ( i<m-1 ) printf( "," );
		}
		printf( "]\n" );
	
	}

	return 0;

}





