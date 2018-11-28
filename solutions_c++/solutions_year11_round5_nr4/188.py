#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <cctype>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

const int MAXS = 200;
char str[MAXS], anss[MAXS];
long long ans;
int len;

void solve(int depth, long long val)
{
    if(ans != -1) return ; //answer found
    
    if(depth == len)
    {
        long long sq = (long long) sqrt(val);
        
        if(sq*sq == val)
            ans = val;
        return ;
    }
    
    if(str[depth] == '?')
    {        
        solve(depth+1, (val<<1LL)+1);        
        solve(depth+1, (val<<1LL));
    }
    else
        solve(depth+1, (val<<1LL)+(str[depth]-'0'));
}

int main()
{
    freopen("Ds.in", "r", stdin);
    freopen("outd_s.txt", "w", stdout);
    int T, anslen;
    scanf("%d\n", &T);
    
    for(int t = 1; T--; ++t)
    {
        scanf("%s\n", str);        
        len = strlen(str);        
        ans = -1;
        
        solve(0, 0);
        
        anslen = 0;
        if(ans != 0)
        {
            while(ans)
            {
                anss[anslen++] = (ans%2)+'0';
                ans >>= 1LL;
            }
        }
        else
            anss[anslen++] = '0';
            
        reverse(anss, anss+anslen);
        
        printf("Case #%d: ", t);
        for(int i = 0; i < anslen; i++)
            printf("%c", anss[i]);
        printf("\n");    
    }
    return 0;
}
