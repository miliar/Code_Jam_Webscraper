#include <iostream>
#include <cstring>
#include <stdio.h>
using namespace std;

int T;
int A, B;

int s[15];
int ps;

int dosad[15];
int pdosad;

int Manjih( int broj, int A, int B )
{
    int BROJ = broj;

    ps = 0;
    while ( broj > 0 ) {
        s[ ps++ ] = broj % 10;
        broj /= 10;
    }
    reverse( s, s+ps );

    pdosad = 0;
    int ret = 0;
    int tmp;
    for (int i = ps-1; i >= 1; --i) {
        if ( s[i] == 0 || s[i] > s[0] ) continue;

        tmp = 0;
        for (int j = i; j < ps; ++j)
            tmp = tmp*10 + s[j];
        for (int j = 0; j < i; ++j)
            tmp = tmp*10 + s[j];

        if ( A <= tmp && tmp < BROJ ) {
            bool ima = false;
            for (int i = 0; i < pdosad; ++i)
                if ( dosad[i] == tmp ) {
                    ima = true;
                    break;
                }

            if ( !ima ) {
                ret++;
                dosad[ pdosad++ ] = tmp;
            }
        }
    }

    return ret;
}

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);

    scanf("%d",&T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d%d",&A,&B);

        int ret = 0;
        for (int i = A; i <= B; ++i) {
            ret += Manjih( i, A, B );
        }

        fprintf(stderr,"Case #%d\n",t);
        printf("Case #%d: %d\n",t,ret);
    }

    return 0;
}
