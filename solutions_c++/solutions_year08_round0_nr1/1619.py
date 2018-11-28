#include <cstdio>
#include <cstring>

using namespace std;

int dp[ 1111 ][ 111 ];
bool same[ 1111 ][ 111 ];
char names[ 111 ][ 111 ];
char query[ 1111 ][ 111 ];
char temp[ 111 ];
int s,q;

inline int mi(int a, int b)
{
    if(a<=b)return a;
    return b;
}

int main()
{
    freopen("savein.txt", "r",stdin);
    freopen("saveout.txt", "w",stdout);
    int i,j,k,a,t;

    gets(temp);

    sscanf(temp, "%d", &t);

    for(i = 1 ;i <= t ; i++)
    {
        int res = 0x3f3f3f3f;
        memset(dp, 0x3f, sizeof dp);
        memset(same, 0, sizeof same);
        gets(temp);
        sscanf(temp, "%d", &s );

        for( j = 0;j < s ; j ++)
            gets(names[j]);
        gets(temp);

        sscanf(temp,"%d", &q);

        for( j= 0;j < q; j++)
            gets(query[j]);

        if( q == 0 )
        {
            printf("Case #%d: 0\n", i );
            continue;
        }

        for( j = 0;j < q; j++)
         for( k = 0;k < s ; k++)
          same[j][k] = (strcmp(query[j],names[k]) == 0);

        for( j = 0;j < s ; j++)
         if( !same[ q-1 ][ j ] )
          dp[ q - 1 ][ j ] = 1;

        for( j = q-2;j >=0; j-- )
        {
         for( k = 0 ; k < s; k ++)
         {
            int next=-1, add = 0;
            if( same[j][k] ) continue;
            for( a = j+1 ; a < q ; a ++ )
            {
             if( same[a][k] )
             {
                next = a ;
                break;
             }
            }
            if( next != -1 )
            {
                add = 0x3f3f3f3f;
                for( a = 0; a < s; a++)
                 add = mi( add, dp[next][a] );
            }
            dp[j][k] = 1 + add;
         }
        }

        for( j = 0;j < s ;  j ++)
         res = mi(res , dp[0][j]);
        --res;
        printf("Case #%d: %d\n",i, res);
    }

    return 0;
}
