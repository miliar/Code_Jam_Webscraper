#include <stdio.h>
#include <string.h>

#define float double

float tree[100000];
char fea[100000][30];
char fea_list[102][30];
bool opt[100000];

void search( int , float & );
int n;

int main()
{
	int T,k,L,pos,i,u,N,j,root;
	char ch;
	float wei;
	char str[30];
	char ani[30];
	
	scanf("%d",&T);

	for( k = 1 ; k <= T ; ++k )
	{
		scanf("%d",&L);
		while(getchar()!='\n');
		pos = 1;
		memset( tree , 0 , sizeof( tree ) );
		memset( opt , 0 , sizeof( opt ) );
		for( i = 1 ; i <= L ; ++i )
		{
			do
			{
				do
				{
					ch = getchar();
				}while( ch != '(' && ch != ')' );
				if( ch == '(' )
				{
					scanf("%lf",&wei);
					if( pos == 1 && tree[pos] == 0 )
						tree[pos] = wei;
					else
					{
						if( tree[2 * pos] == 0 )
							pos = 2 * pos;
						else
							pos = 2 * pos + 1;
						tree[pos] = wei;
					}
					ch = getchar();
					if( ch == ')' )
					{
						pos = pos / 2;
						break;
					}
					if( ch == '\n' )
						break;
					u = 0;
					while( 1 )
					{
						ch = getchar();
						while( ch >= 'a' && ch <= 'z' )
						{
							str[u] = ch;
							u++;
							ch = getchar();
						}
						if( ch == ' ' || ch == ')' || ch == '\n' )
							break;
					}
					str[u] = '\0';
					if( u > 0 )
					{
						strcpy( fea[pos] , str );
						opt[pos] = true;
					}
					if( ch == ')' )
					{
						pos = pos / 2;
						break;
					}
					if( ch == '\n' )
						break;
				}
				else
				{
					pos = pos / 2;
					break;
				}
			}while(1);
			if( ch != '\n' )
				while( getchar() != '\n' );
		}
		printf("Case #%d:\n",k);
		scanf("%d",&N);
		for( i = 1 ; i <= N ; ++i )
		{
			scanf("%s%d",ani,&n);
			for( j = 0 ; j < n ; ++j )
			{
				scanf("%s",fea_list[j]);
			}
			float sum = 1;
			float pp=1;

			search( 1 , pp );
			printf("%7lf\n",pp);
		}
	}
}

bool check( int root )
{
	int i;
	for( i = 0 ; i < n ; ++i )
	{
		if( strcmp( fea_list[i] , fea[root] ) == 0 )
			return true;
	}
	return false;
}

void search( int root , float &pp )
{
	if( tree[root] == 0 )
		return ;
	pp = pp * tree[root];

	if( opt[root] == false )
	{
		search( 2 * root , pp );
	}
	else
	{
		if( check( root ) )
			search( 2 * root , pp );
		else
			search( 2 * root + 1 , pp );
	}
}
