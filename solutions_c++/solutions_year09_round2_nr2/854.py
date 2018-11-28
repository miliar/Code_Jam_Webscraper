#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>

using namespace std;

#define MaxN 10000

int n,len;
char s[MaxN];

void solve()
{
    bool flag = true;
    len = strlen(s);
    if (next_permutation(s,s+len)) 
    {
        while (s[0] == '0')
        {
            if (!next_permutation(s,s+len))
            {
                flag = false;
                break;
            }
        }
        if (flag)
        {
             printf("%s\n",s);
             return;
        }
    }
    for (int i = len ; i > 0 ; i--)
        s[i] = s[i - 1];
    s[0] = '0';

    len++;
    s[len] = '\0';
    for (int i = 1; i < len ; i++)
        if (s[i] != '0')
        {
            swap<char>(s[0],s[i]);
            break;
        }
    printf("%s\n",s);
}

int main()
{
//    freopen("test.in","r",stdin);
//    freopen("test.out","w",stdout);
    int Case;
    scanf("%d", &Case);
    for (int i = 1; i <= Case ; i++)    
    {
        printf("Case #%d: ", i);
        scanf("%s", s);
        solve();
    }
    return 0;
}

