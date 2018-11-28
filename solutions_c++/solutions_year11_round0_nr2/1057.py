#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;

#define MaxC 40
#define MaxD 30
#define MaxN 110
#define MaxChar 30

int T;
int c,d,n;

int next[MaxN];
int prev[MaxN];
char s[MaxN];

char combine[MaxChar][MaxChar];
bool opposed[MaxChar][MaxChar];

int main()
{
    freopen("test2.in","r",stdin);
    freopen("test2.out","w",stdout);

    scanf("%d",&T);
    for (int t = 0; t < T; ++t) {

        for (int i = 0; i < MaxChar; ++i)
            for (int j = 0; j < MaxChar; ++j) {
                combine[i][j] = 'a';
                opposed[i][j] = false;
            }
        for (int i = 0; i < MaxN; ++i) {
            next[i] = i+1;
            prev[i] = i-1;
        }


        scanf("%d",&c);
        for (int i = 0; i < c; ++i) {
            scanf("%s",s);

            int p1 = s[0] - 'A';
            int p2 = s[1] - 'A';

            combine[p1][p2] = combine[p2][p1] = s[2];
        }

        scanf("%d",&d);
        for (int i = 0; i < d; ++i) {
            scanf("%s",s);

            int p1 = s[0] - 'A';
            int p2 = s[1] - 'A';

            opposed[p1][p2] = opposed[p2][p1] = true;
        }

        scanf("%d",&n);
        scanf("%s",s);

        for (int i = 1; i < n; ++i) {
            int j = prev[i];

            while ( j > -1 ) {

                if ( prev[i] == j && combine[ s[i]-'A' ][ s[j]-'A' ] != 'a' ) {
                    s[i] = combine[ s[i]-'A' ][ s[j]-'A' ];
                    prev[i] = prev[j];
                    if ( prev[j] > -1 ) next[ prev[j] ] = i;
                }
                else {
                    if ( opposed[ s[i]-'A' ][ s[j]-'A' ] ) {
                        prev[ next[i] ] = -1;
                    }
                }

                j = prev[j];
            }

        }

        int p = n;
        while ( prev[p] > -1 ) {
            p = prev[p];
        }
        printf("Case #%d: [",t+1);
        if ( p < n ) {
            printf("%c",s[p]);

            p = next[p];
            while ( p < n ) {
                printf(", %c",s[p]);
                p = next[p];
            }
        }
        printf("]\n");
    }

    return 0;
}
