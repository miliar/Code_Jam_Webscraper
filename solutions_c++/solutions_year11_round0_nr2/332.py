#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

char combine[256][256];
char opp[256][256];

bool isopp(char * ans, int &len)
{
    for (int i = 0; i < len; i++)
    {
        for (int j = i + 1; j < len; j++)
        {
            if (opp[ans[i]][ans[j]])
            {
                return true;
            }
        }
    }
    return false;
}

void tocombine(char * ans, int &len)
{
    while(len > 1)
    {
        char x = ans[len - 1];
        char y = ans[len - 2];
        if (combine[x][y])
        {
            ans[len - 2] = combine[x][y];
            len = len - 1;
        }
        else
        {
            return;
        }
    }
}

void solve()
{
    memset(combine, 0, sizeof combine);
    memset(opp, 0, sizeof opp);
    
    int C, D, N;
    cin >> C;
    for (int i = 0; i < C; i++)
    {
        string cs;
        cin >> cs;
        combine[cs[0]][cs[1]] = cs[2];
        combine[cs[1]][cs[0]] = cs[2];    
    }
    cin >> D;
    for (int i = 0; i < D; i++)
    {
        string ds;
        cin >> ds;
        opp[ds[0]][ds[1]] = 1;
        opp[ds[1]][ds[0]] = 1;
    }
    cin >> N;
    string ns;
    cin >> ns;
    char ans[1024] = {0};
    int len = 0;
    
    for (int i = 0; i < ns.size(); i++)
    {
        ans[len++] = ns[i];
        tocombine(ans, len);
        if (isopp(ans, len))
        {
            len = 0;
        }   
    }
    
    printf("[");
    for (int i = 0; i < len; i++)
    {
        printf("%c", ans[i]);
        if (i != len - 1)
        {
            printf(", ");
        }
    }
    printf("]\n");
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int i = 1; i <= T; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
