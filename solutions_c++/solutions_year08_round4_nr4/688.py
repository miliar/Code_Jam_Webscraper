#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

#define MAX 50001

int m;
char tab[MAX];

int licz()
{
    int perm[16];
    int len = strlen( tab );

    for(int i=0;i<m;i++)
        perm[i] = i;

    int ret = 999999999;
    do {
        int x=0;
        int y=0;
        int res = 0;
        for(int i=0;i<len;i++) {
            int next = (x+1)%m;
            int y_next = y;
            if( next == 0 )
                y_next+=m;

            if( tab[perm[x]+y] != tab[perm[next]+y_next] )
                res++;
            x = next;
            y = y_next;
        }
//        printf("%d %d %d %d\n", res, perm[0], perm[1], perm[2] );
        if( res < ret ) {
            ret = res;
        }
    } while( next_permutation( perm, perm+m ) );

    return ret;
}

int wczytaj()
{
    scanf("%d", &m );
    scanf("%s", tab );
    return 0;
}

int main()
{
    int n;
    scanf("%d", &n );
    for( int i=1;i<=n;i++) {
        wczytaj();
        int ret = licz();
        printf("Case #%d: %d\n", i, ret );
    }
    return 0;
}
