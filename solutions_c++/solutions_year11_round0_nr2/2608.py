#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
using namespace std;
int t, c, d, n;
char form[128][128], str[300];
bool opp[128][128];
char ans[200];
int cnt;
int main()
{
    freopen("B.txt", "w", stdout);
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++)
    {
        scanf("%d", &c);
        memset(form, 0, sizeof(form));
        memset(opp, 0, sizeof(opp));
        for(int i = 0; i < c; i++)
        {
            scanf("%s", str);
            form[str[0]][str[1]] = str[2];
            form[str[1]][str[0]] = str[2];
        }
        scanf("%d", &d);
        for(int i = 0; i < d; i++)
        {
            scanf("%s", str);
            opp[str[0]][str[1]] = opp[str[1]][str[0]] = true;
        }
        cnt = 0;
        scanf("%d", &n);
        scanf("%s", str);
        for(int i = 0; i < n; i++)
        {
            ans[cnt++] = str[i];
            if (cnt > 1 && form[ans[cnt - 1]][ans[cnt - 2]] != 0)
                ans[cnt - 2] = form[ans[cnt - 1]][ans[cnt - 2]], cnt--;
            else if (cnt > 1)
            {
                for(int j = 0; j < cnt - 1; j++)
                    if (opp[ans[cnt - 1]][ans[j]]) cnt = 0;
            }
        }
        printf("Case #%d: [", tt);
        if (cnt > 0) printf("%c", ans[0]);
        for(int i = 1; i < cnt; i++) printf(", %c", ans[i]);
        printf("]\n");
    }
    return 0;
}
