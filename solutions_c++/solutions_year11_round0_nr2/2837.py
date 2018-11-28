#include <vector>
#include <iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<string.h>
#include<queue>
#include <set>
#include<map>
#include<string>
#include<stdexcept>
#include<errno.h>

using namespace std;
template <class T> void show(T a, int n) { for (int i = 0; i < n; ++i) cout << a[i] << ' '; cout << endl; }
template <class T> void show(T a, int r, int l) { for (int i = 0; i < r; ++i) show(a[i], l); cout << endl; }
#define max(a, b) (a > b?a:b)
#define min(a, b) (a < b?a:b)

#define ms(a, v)    memset(a, v, sizeof(a))
#define pb push_back
#define mp make_pair
#define pii pair<int, int>

typedef long long LL;

const int N = 128 * 2;
const int M = 5000;
const int oo = 10000 * 10000 * 10;


char com[500][500];
bool opos[500][500];
char buf[128];
int n;

char ans[128];
int an;

void solve()
{
    int i, j, k;
    an = 0;
    ans[an++] = '$';
//    printf("n:%d\n", n);
    for(i = 0; i < n;++i)
    {
        ans[an++] = buf[i];
       
//        for(i = 0; i < an;++i)
//            putchar(ans[i]);
//        putchar(10);
        
        char c;
        if( c = com[ ans[an - 2] ][ ans[an - 1] ] )
        {
//            printf("c:%c\n", c);
            an -= 2;
            ans[an++] = c;
        }
        else
        {
            for(j = 1; j < an - 1;++j)
                if( opos[ ans[j] ][ ans[an - 1] ] )
                {
                    an = 1;
                    break;
                }
        }
    }
  
}

int main()
{
        freopen("in", "r", stdin);
        freopen("out","w",stdout); 
    int i, j, cas = 0;
    
    scanf("%d", &cas);
    for(int cc = 0; cc < cas;++cc)
    {
        ms(com, 0);
        ms(opos, 0);
        int c;
        scanf("%d", &c);
        while(c--)
        {
            scanf("%s", buf);
            com[ buf[0] ][ buf[1] ] = buf[2];
            com[ buf[1] ][ buf[0] ] = buf[2];
        }
        scanf("%d", &c);
        while(c--)
        {
            scanf("%s", buf);
            opos[ buf[0] ][ buf[1] ] = true;
            opos[ buf[1] ][ buf[0] ] = true;
        }
        scanf("%d", &n);
        scanf("%s", buf);
//        puts(buf);
        solve();
//        Case #1: [E, A]
        printf("Case #%d: [", cc + 1);
        for(i = 1; i < an;++i)
        {
            if( i > 1 )
                printf(", ");
            putchar(ans[i]);
        }
        putchar(']');
        putchar(10);
    }

    
    return 0;
}

