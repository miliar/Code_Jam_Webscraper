#include<stdio.h>
#include<string.h>
const char w[50] = "welcome to code jam";
char tmp[1000], s[1000];
const int mod = 10000;
int test, t, w_len;
void get_s()
{
    int i, j, k;
    bool b;
    k = 0;
    for(i = 0; tmp[i] != '\0'; i ++)
    {
        b = false;
        for(j = 0; w[j] != '\0'; j ++)
            if(w[j] == tmp[i])
            {
                b = true;
                break;
            }
        if(b)
            s[k ++] = tmp[i];
    }
    s[k] = '\0';    
}
int dp[504][27];
void dfs()
{
    int i, j, k, s_len, tmp;
    s_len = strlen(s);
    for(i = s_len - 1; i >= 0; i --)
    {
        for(j = 0; j < w_len; j ++)
        {
            if(s[i] == w[j])
            {
                if(j == w_len - 1)
                    dp[i][j] = 1;
                else
                {
                    tmp = 0;
                    for(k = i + 1; k < s_len; k ++)
                    {
                        tmp += dp[k][j + 1];
                    }
                    dp[i][j] = tmp % mod;
                }
            }
            else
                dp[i][j] = 0;
        }
    }
}
int get_ans()
{
    int i, s_len;
    int ans = 0;
    s_len = strlen(s);
    for(i = 0; i < s_len; i ++)
        ans += dp[i][0];
    return ans % mod;
}
void print(int ans)
{
    if(ans < 10)
        printf("000%d\n", ans);
    else if(ans < 100)
        printf("00%d\n", ans);
    else if(ans < 1000)
        printf("0%d\n", ans);
    else
        printf("%d\n", ans);
}
int main()
{
    scanf("%d", &test);
    w_len = strlen(w);
    int ans;
    char c = getchar();
    for(t = 1; t <= test; t ++)
    {
        gets(tmp);
        get_s();
        dfs();
        ans = get_ans();
        printf("Case #%d: ", t);
        print(ans);
    }
    return 0;
}
