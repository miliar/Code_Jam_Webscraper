#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long long LL;

const int maxn = 1000010;

bool bo[maxn];
int cas;
LL n;

void prepare()
{
    for (int i = 2; i<maxn; i++ )
        if (!bo[i])
            for (int j = i+i; j<maxn; j+=i )
                bo[j] = 1;
}

int myLog(LL n, LL m )
{
    int ret = 1;
    LL t = m;
    while (t*m <= n)
    {
        t *= m;
        ret++;
    }
    return ret;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    prepare();
    scanf("%d",&cas);
    for (int run = 1; run<=cas; run++ )
    {
        cin>>n;
        LL ans = n>1?1:0;
        for (LL i = 2; i*i<=n; i++ )
            if (!bo[i])
                ans += myLog(n,i)-1;
        cout<<"Case #"<<run<<": "<<ans<<endl;
    }
    //system("pause");
    return 0;
}
