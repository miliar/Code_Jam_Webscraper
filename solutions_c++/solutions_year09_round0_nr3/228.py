#include <stdio.h>
#include <cstring>

char T[100] = "$welcome to code jam";
char S[1000], SS[1000];
int f[511][511];

int cnt(int n)
{
    int ans = 0;
    if(n==0) return 1;
    while(n)
    {
        ans++;
        n /= 10;
    }
    return ans;
}

void solve(int tc)
{
    printf("Case #%d: ", tc);

    int l1 = strlen(SS), l2 = strlen(T);

    for(int i=0; i<l1; ++i) S[i+1] = SS[i];
    S[0] = 'X';
    S[l1+1] = 0;
    memset(f, 0, sizeof f);
    f[0][0] = 1;

    int ans = 0;
    for(int i=1; i<=l1; ++i)
    {
        for(int j=1; j<l2; ++j)
        {
            if(S[i] == T[j])
            {
                for(int k=0; k<i; ++k) f[i][j] = (f[i][j] + f[k][j-1]) % 10000;
                if(j==l2 - 1) ans = (ans + f[i][j]) % 10000;
            }
        }
    }
    int num = cnt(ans);
    for(int i=1; i<=4-num; ++i) printf("0");
    printf("%d\n", ans);
}

int main()
{
    int t,k = 0;
    scanf("%d\n", &t);
    while(t--)
    {
        gets(SS);
        solve(++k);
    }
    return 0;
}

