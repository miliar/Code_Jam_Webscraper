#include<stdio.h>
#include<string.h>
int K, Res;
char str[50024];
char str2[50024];
int a[20];
bool used[20];
void process()
{
    int i, r;
    for(i = 0; i < strlen(str); ++i)
    {
        str2[i] = str[(i - i % K) + a[i % K]];
    }
    str2[i] = '\0';
    r = 1;
    for(i = 1; i < strlen(str); ++i)
        if(str2[i] != str2[i - 1]) ++r;
    if(r < Res) Res = r;
}
void A(int p)
{
     if(p >= K) process();
     else
     {
         int i;
         for(i = 0; i < K; ++i)
             if(!used[i])
             {
                 used[i] = 1;
                 a[p] = i;
                 A(p + 1);
                 used[i] = 0;
             }
     }
}
int main()
{
    int t, ctr;
    freopen("D_S.in", "r", stdin);
    freopen("D_S.out", "w", stdout);
    scanf("%d", &t);
    for(ctr = 1; ctr <= t; ++ctr)
    {
        scanf("%d", &K);
        scanf("%s", str);
        memset(used, 0, sizeof(used));
        Res = strlen(str);
        A(0);
        printf("Case #%d: %d\n", ctr, Res);
    }
}
