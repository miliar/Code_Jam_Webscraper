#include<iostream>
#include<algorithm>
using namespace std;
int t, n, m;
int ans[100], val[100];
char L[100][27];
struct DIR{char str[12];}dir[10000];
bool cmp(DIR a, DIR b)
{
    return strlen(a.str) < strlen(b.str);
}

bool vst[10000];
bool know[10];
int judge(int id, char c)
{
    bool flag = false;
    for(int i = 0; i < strlen(dir[id].str); i++)
        if (dir[id].str[i] == c)
        {
            flag = true;
            know[i] = true;
        }
    bool kn = true;
    for(int i = 0; i < strlen(dir[id].str); i++)
        if (!know[i]) kn = false;
    if (kn) return -2;
    if (flag)
    {
        for(int i = 0; i < n; i++)
            if (!vst[i])
            {
                for(int j = 0; j < strlen(dir[id].str); j++)
                    if (know[j] && dir[i].str[j] != dir[id].str[j] || !know[j] && dir[i].str[j] == c)
                    {
                        vst[i] = true;
                        break;
                    }
            }
        return 1;
    }else
    {
        bool have = false;
        for(int i = 0; i < n; i++)
            if (!vst[i])
            {
                for(int j = 0; j < strlen(dir[i].str); j++)
                    if (dir[i].str[j] == c)
                    {
                        vst[i] = true;
                        have = true;
                        break;
                    }
            }
        if (have) return -1;
        return 0;
    }
}
void output()
{
    printf("Ê£Óà:\n");
    for(int i = 0; i < n; i++)
        if (!vst[i]) printf("%s\n", dir[i].str);
}
int main()
{
    freopen("BB.txt", "w", stdout);
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++)
    {
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; i++)
            scanf("%s", dir[i].str);
        //sort(dir, dir + n, cmp);
        for(int i = 0; i < m; i++)
            scanf("%s", L[i]);
        for(int i = 0; i < m; i++) val[i] = 0x7fffffff;
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                int lose = 0;
                for(int k = 0; k < n; k++) vst[k] = 0;
                for(int k = 0; k < n; k++)
                    if (strlen(dir[k].str) != strlen(dir[j].str)) vst[k] = 1;
                memset(know, 0, sizeof(know));
                for(int k = 0; k < 26; k++)
                {
                    int ttt = 0;
                    for(int ii = 0; ii < n; ii++)
                        if (!vst[ii]) ttt++;

                    if (ttt == 1) break;
                    int tmp = judge(j, L[i][k]);
                    if (tmp == -2) break;
                    if (tmp == -1) lose--;

                    //if (tmp == 1 || tmp == -1)
                      //  printf("²Â%c", L[i][k]);
                    //if (tmp == 1) printf("yes\n");
                    //else if (tmp == -1) printf("no\n");
                    //if (tmp != 0) output();
                }
                if (lose < val[i])
                {
                    val[i] = lose;
                    ans[i] = j;
                }
            }
            //cout << val[i] << endl;
        }
        printf("Case #%d:", tt);
        for(int i = 0; i < m; i++)
            printf(" %s", dir[ans[i]].str);
        printf("\n");
    }
    return 0;
}
