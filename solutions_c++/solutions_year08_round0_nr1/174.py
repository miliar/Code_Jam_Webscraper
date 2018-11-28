#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int f[1205][215];
typedef struct
{
    char name[1010];
}Name;
Name q[105];
int ID[1100];
int n, m;

bool cmp( Name a, Name b )
{
    return (strcmp(a.name,b.name) < 0 ? true : false);
}

int Find( char name[] )
{
    int mid;
    int low = 0;
    int high = n-1;
    while( low <= high )
    {
        mid = (low+high)/2;
        int temp = strcmp(name, q[mid].name);
        if( temp == 0 )return mid;
        else if( temp > 0 )low = mid+1;
        else high = mid-1;
    }
    return mid;
}


int main()
{
    int kcase, t = 0;
    char name[110];
    freopen("A-large.in", "r", stdin );
    freopen("largeout.txt","w", stdout );
    scanf("%d", &kcase);
    while( kcase--){
        scanf("%d", &n);
        getchar();
        for(int i = 0; i < n; i++ ){
            gets(q[i].name);
        }
        sort(q,q+n,cmp);
        scanf("%d", &m );
        getchar();
        for( int i = 0; i < m; i++ ){
            gets(name);
            ID[i] = Find(name);
            //printf("%d ", ID[i]);
        }
        
        //if( n > 100 || m > 1000 )while(1);
        //printf("yes\n" );
        
        if( m==0)
        {
            printf( "Case #%d: 0\n", ++t );
            continue;
        }
        
        for(int i =0;i <m;i++){
            for(int j=0;j<n;j++)f[i][j]=-1;
        }
        for(int i=0;i<n; i++)f[0][i]=0;
        f[0][ID[0]]=-1;
        for( int i = 1; i < m; i++ )
        {
            for( int j = 0; j < n; j++ )if( f[i-1][j] >= 0 )
            {
                for( int k = 0; k < n; k++ )
                {
                    if( k == ID[i] )f[i][k]=-1;
                    else
                    {
                        if( k != j && ( f[i][k] < 0 || f[i][k] > f[i-1][j]+1 ) )f[i][k] = f[i-1][j]+1;
                        else if(k == j && ( f[i][k] < 0 || f[i][k] > f[i-1][j] ) )f[i][k] = f[i-1][j];
                    }
                }
            }
        }
        int ans = -1;
        for( int i = 0; i < n; i++ )
        {
            if( f[m-1][i] >= 0 && ( ans < 0 || ans > f[m-1][i] )) ans = f[m-1][i];
        }
        printf( "Case #%d: %d\n", ++t, ans );
    }
    return 0;
}
