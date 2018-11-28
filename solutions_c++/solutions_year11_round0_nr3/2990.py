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

const int B = 20;

inline int p2(int i)
{
    return 1<<i;
}

int n, m;

int val[N];

int cnt[20];

bool check()
{
    int i, j;
    ms(cnt, 0);
    for(i = 0; i < n;++i)
    {
        for(j = 0;j < B;++j)
            if( p2(j) & val[i] )
                ++cnt[j];
    }
    for(i = 0; i < B;++i)
        if( cnt[i] % 2 )
            return false;
    return true;
}


int main()
{
        freopen("in", "r", stdin);
        freopen("out","w",stdout); 
    int i, j, cas = 0;
    
    scanf("%d", &cas);
    for(int cases = 0; cases < cas;++cases)
    {
        scanf("%d", &n);
        for(i = 0;i < n;++i)
            scanf("%d", &val[i]);
        
        printf("Case #%d: ", cases + 1);
        if( check() )
        {
            sort(val, val + n);
            int ans = 0;
            for(i = 1; i < n;++i)
                ans += val[i];
            printf("%d\n", ans);
        }
        else
            puts("NO");
    }
    
    
 


    
    return 0;
}

