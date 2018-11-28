#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

int n,m,res,sam;
char d[12000][15],l[30];
int len[12000];
bool visit[12000];

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int ft = 1;ft <= t;ft++)
    {
        scanf("%d%d",&n,&m);
        for (int i = 0;i < n;i++)
        {
            scanf("%s",d[i]);
            len[i] = strlen(d[i]);
        }
        printf("Case #%d:",ft);
        for (int i = 0;i < m;i++)
        {
            scanf("%s",l);
            res = 0;
            int fai = 0;
            for (int j = 0;j < n;j++)
            {
                int tfai = 0;
                memset(visit,false,sizeof(visit));
                for (int k = 0;k < n;k++)
                    if (len[k] != len[j])
                        visit[k] = true;
                for (int q = 0;q < 26;q++)
                {
                    int left = 0;
                    for (int k = 0;k < n;k++)
                        if (visit[k] == false)
                        {
                            for (int p = 0;p < len[k];p++)
                                if (d[k][p] == l[q])
                                {
                                    left++;
                                    break;
                                }
                        }
                    if (left >= 1)
                    {
                        bool flag = false;
                        for (int p = 0;p < len[j];p++)
                            if (d[j][p] == l[q])
                            {
                                flag = true;
                                break;
                            }
                        if (flag == false)
                            tfai++;
                        for (int k = 0;k < n;k++)
                            if (visit[k] == false)
                            {
                                for (int p = 0;p < len[k];p++)
                                    if (d[k][p] == l[q] || d[j][p] == l[q])
                                        if (d[k][p] != l[q] || d[j][p] != l[q])
                                            visit[k] = true;
                            }
                    }
                }
                //cout << j << ' ' << tfai << ' ' << fai << endl;
                if (tfai > fai)
                {
                    res = j;
                    fai = tfai;
                }
            }
            printf(" %s",d[res]);
        }
        printf("\n");
    }
}
