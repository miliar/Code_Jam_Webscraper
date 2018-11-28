#include <iostream>
using namespace std;

#define MaxN 100

char s[MaxN+10];
int t;
int a[ 40 ];
int b[62];
bool nula;
long long ret;

int cif( char c )
{
    if ( c >= '0' && c <= '9' ) return (c - '0') + 26;
    return (c - 'a');
}

long long Prebaci(int a[], int s)
{
    int os = 0;
    for (int i = 0; i < s; i++)
      os = max( os, a[i] );
    os++;

    long long ret = 0;
    long long tr = 1;

    for (int i = s-1; i >= 0; i--) {
        ret += tr*a[i];
        tr *= os;
    }

    return ret;
}

long long Solve( char s[] )
{
    int ret = 0;
    int br = 0;
    memset(a, -1, sizeof(a));
    int len = strlen(s);

    b[0] = 1;
    a[ cif(s[0]) ] = 1;

    nula = false;
    br = 2;

    for (int i = 1; i < len; i++) {
        if ( a[ cif(s[i]) ] == -1 ) {
            if ( !nula ) {
                a[ cif(s[i]) ] = 0;
                b[ i ] = 0;
                nula = true;
            }
            else {
                a[ cif(s[i]) ] = br;
                b[i] = br;
                br++;
            }
        }
        else {
            b[i] = a[ cif(s[i]) ];
        }
    }

    return Prebaci(b,len);

}

int main()
{
    scanf("%d",&t);
    for (int T = 0; T < t; T++) {

        scanf("%s",s);

        printf("Case #%d: %lld\n",T+1,Solve(s));
    }

    return 0;

}
