#include <iostream>
#include <stdio.h>
#include <cstring>
#include <math.h>
using namespace std;

#define MaxN 110

struct button {
   int pos;
   int id;

   button() {}
   button( int _pos, int _id ) {
      pos = _pos;
      id = _id;
   }
};

int n,T;
button a[MaxN];
int nextO[MaxN];
int nextB[MaxN];

int pos,id;
char s[4];

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);

    scanf("%d",&T);
    for (int t = 0; t < T; ++t) {

        scanf("%d",&n);
        for (int i = 0; i < n; ++i) {
            scanf("%s %d",s,&pos);

            id = 0;
            if ( s[0] == 'B' ) id = 1;
            a[i] = button( pos, id );
        }

        int lastO, lastB;
        lastO = lastB = -1;
        for (int i = n-1; i >= 0; --i) {
            if ( a[i].id == 0 ) lastO = a[i].pos;
            else                lastB = a[i].pos;

            nextO[i] = lastO;
            nextB[i] = lastB;
        }

        int posO,posB;
        posO = posB = 1;
        int ret = 0; int time;
        for (int i = 0; i < n; ++i) {

            if ( a[i].id == 0 ) {

                time = abs( posO - a[i].pos ) + 1;
                posO = a[i].pos;

                if ( nextB[i] > -1 ) {
                    if ( nextB[i] > posB ) posB = min( nextB[i], posB+time );
                    else                   posB = max( nextB[i], posB-time );
                }

            }
            else {

                time = abs( posB - a[i].pos ) + 1;
                posB = a[i].pos;

                if ( nextO[i] > -1 ) {
                    if ( nextO[i] > posO ) posO = min( nextO[i], posO+time );
                    else                   posO = max( nextO[i], posO-time );
                }
            }

            ret += time;
        }

        printf("Case #%d: %d\n",t+1,ret);
    }

    return 0;
}
