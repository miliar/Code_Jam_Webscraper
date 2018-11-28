#include<cstdio>
#include<vector>
#include<deque>
#include<cmath>
#include<queue>
#include<set>
#include<cstring>
#include<string>

#define pb push_back
#define mp make_pair
#define ll long long

using namespace std;

int i , j , n , m , cases , t , A[500][500] , C[500][500];
char s[500];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&t);
	
	for( cases = 1 ; cases <= t ; ++cases ) { 
		
		printf("Case #%d:\n",cases);
		
		scanf("%d %d\n",&n,&m);
		
		memset( A , 0 , sizeof(A));
		memset( C , 0 , sizeof(C));
		
		bool ok = true;
		
		for( i = 1 ; i <= n ; ++i ) { 
			
			fgets( s , 100 , stdin);
			for( j = 0 ; j < m ; ++j ) 
				if ( s[j] == '.')
					A[i][j + 1] = 0;
				else
					A[i][j + 1] = 1;
		}
		
		for( i = 1 ; i <= n ; ++i ) 
			for( j = 1 ; j <= m ; ++j ) 
				if ( A[i][j] == 1 ) { 
					
					if ( i + 1 > n || j + 1 > m )
						ok = false;
					
					if ( A[i][j + 1] != 1 || A[i + 1][j] != 1 || A[i + 1][j + 1] != 1 )
						ok = false;
					
					C[i][j] = 1 , A[i][j] = 0;
					C[i][j + 1] = 2 , A[i][j + 1] = 0;
					C[i + 1][j] = 2 , A[i + 1][j] = 0;
					C[i + 1][j + 1] = 1 , A[i + 1][j + 1] = 0;
				}
		if ( !ok ) 
			printf("Impossible\n");
		else {
			for( i = 1 ; i <= n ; ++i ) {
				for( j = 1 ; j <= m ; ++j ) { 
					if ( C[i][j] == 1 ) 
						printf("/");
					else if ( C[i][j] == 2 )
						printf("\\");
					else if ( C[i][j] == 0 ) 
						printf(".");
				}
			printf("\n");
			}
		}
	}		
				
	
return 0;
}