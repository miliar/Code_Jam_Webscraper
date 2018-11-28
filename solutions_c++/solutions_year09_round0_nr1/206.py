#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

int L, D, N;
string str[50010];
char buf[1024];
bool flag[16][256];

int main()
{
    int i, j, k;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    while(scanf("%d%d%d", &L, &D, &N) == 3)
    {
     for(i = 0; i < D; i++)
     {
           scanf("%s", &buf);
           str[i] = buf;
           }
     sort(str, str + D);
     for(i = 1; i <= N; i++)
     {
           scanf("%s", &buf);
           memset(flag, 0, sizeof(flag));
           int len = strlen(buf);
           j = k = 0;
           int c = 0;
           while(j < len)
           {
                   k = j + 1;
                   if(buf[j] == '(')
                   {
                             while(k < len && buf[k] != ')')
                               k++;
                             for(int w = j + 1; w < k; w++)
                                     flag[c][buf[w]] = true;
                             j = k + 1;
                   }
                   else
                   {
                       flag[c][buf[j]] = true;
                       j = k;
                   }
                   ++c;
           }
           printf("Case #%d: ", i);
           int ret = 0;
           for(j = 0; j < D; j++)
           {
                 for(k = 0; k < L; k++)
                 {
                       if(!flag[k][str[j][k]])
                       break;
                 }
                 if(k >= L)
                 ret++;
           }
           printf("%d\n", ret);
     }
     }
    return 0;
}
