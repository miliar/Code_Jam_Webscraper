#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int but;
char hall[10];

int main()
{
    char p;
    int aa, nn, n, i, B, O, ans, pt, t;
    scanf("%d",&nn);
    for ( aa = 1; aa <= nn; ++aa ) {
        scanf("%d",&n);
        B = 1; O = 1; ans = 0; p = 0, pt = 0;
        for ( i = 0; i < n; i++ ) {
            scanf("%s %d",hall,&but);
            if ( hall[0] == 'B' ) {
                t = max(B,but)-min(B,but);
                B = but;
            }
            if ( hall[0] == 'O') {
                t = max(O,but)-min(O,but);
                O = but;
            }
            if ( hall[0] == p ) {
                t++;
                pt += t;
            } else {
                if ( pt >= t ) t = 1;
                else t = t-pt+1;
                pt = t;
                p = hall[0];
            }
            ans += t;
        }
        printf("Case #%d: %d\n",aa,ans);
    }
    return 0;
}

