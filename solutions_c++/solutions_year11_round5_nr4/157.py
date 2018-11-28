#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long LL;

const int maxn = 64;

char s[maxn];

int cas;
LL ans;

void check(LL sum )
{
    //cout<<sum<<endl;
    LL x = round(sqrt(sum));
    if (x*x == sum || (x+1)*(x+1) == sum) ans = sum;
}

void dfs(int i, LL sum )
{
    if (!s[i])
    {
        check(sum);
        return ;
    }
    if (s[i] != '0') dfs(i+1, (sum<<1)^1);
    if (s[i] != '1') dfs(i+1, sum<<1);
}

int main()
{
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-small-attempt1.out", "w", stdout);
    scanf("%d",&cas);
    for (int run = 1; run<=cas; run++ )
    {
        scanf("%s",s);
        printf("Case #%d: ",run);
        dfs(0, 0);
        //cout<<strlen(s)<<' '<<ans<<' ';
        for (int i = strlen(s)-1; i>=0; i-- )
            printf("%d",(ans&((LL)1<<i))>0);
        printf("\n");
    }
    //system("pause");
    fclose(stdin);
    fclose(stdout);
    return 0;
}
