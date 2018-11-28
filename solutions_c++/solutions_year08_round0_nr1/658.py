#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
const int maxn = 200;
const int oo = 1000000000;
string server[maxn],str;
int que[2000];
int f[maxn][2000];
int i,j,k,s,q;

void work()
{
    for (i = 1;i <= s; ++i)
        if (i != que[1])
            f[i][1] = 0;
        else f[i][1] = oo;        
    for (i = 1;i <= s; ++i)
        for (j = 2; j <= q; ++j)
            f[i][j] = oo;
    for (j = 2; j <= q; ++j)
    {
        for (i = 1;i <= s; ++i)
            if (i != que[j])
            {
                for (k = 1; k <= s; ++k)
                    if (i == k && f[k][j-1] < f[i][j])
                        f[i][j] = f[k][j-1];
                    else if (f[k][j-1] + 1 < f[i][j])
                        f[i][j] = f[k][j-1] + 1;                        
            }
    }
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Test;
    cin >> Test;
    for (int T = 1; T <= Test; ++T)
    {
        cin >> s;
        getline(cin,server[0]);
        for (i = 1;i <= s;++i)
            getline(cin,server[i]);
        cin >> q;
        getline(cin,str);
        for (i = 1; i <= q; ++i)
        {
            getline(cin,str);
            for (j = 1; j <= s; ++j)
                if (str == server[j])
                {
                    que[i] = j;
                    break;
                }
        }
        work();
        int ans = oo;
        for (i = 1;i <= s; ++i)
            if (f[i][q] < ans)
                ans = f[i][q];
        printf("Case #%d: %d\n",T,ans);
    }
    return 0;
}
