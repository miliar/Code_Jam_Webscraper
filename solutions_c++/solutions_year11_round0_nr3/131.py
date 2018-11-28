#include<cstdio>
#include<algorithm>
using namespace std;

inline int Rint(){ int x; scanf("%d", &x); return x; }

const int maxn = 1000 + 10;
int n;
int a[maxn];
int main()
{
    int Tcase = Rint();
    while( Tcase -- )
    {
            n = Rint();
            for( int i = 0; i < n; ++ i )
                 a[i] = Rint();
            sort(a, a + n);
            int Xor = 0;
            for( int i = 0; i < n; ++ i )
                 Xor ^= a[i];
            static int o = 1;
            printf("Case #%d: ", o ++);
            if( Xor )
            {
                puts("NO");
                continue;
            }
            int sum = 0;
            for( int i = 1; i < n; ++ i )
                 sum += a[i];
            printf("%d\n", sum);
    }
    return 0;
}
