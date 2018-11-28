#include <cstdio>
#include <cstring>

using namespace std;

#define MAXD 5000
#define MAXL 15

int L, D, N;
char lab[MAXD + 1][MAXL + 1];


void ini(void)
{
     freopen("A-small.in", "r", stdin);
     freopen("A-small.out", "w", stdout);
     
     
     scanf("%d %d %d\n", &L, &D, &N);
     
     int i;
     for(i=1; i<=D; i++)
              scanf("%s\n", lab[i]);
     
     return;
}

void work(void)
{
     int i, j, k, res = 0, now, count;
     int sl;
     bool flag, tt, tt2;
     char temp[500];
     
     
     for(i=1; i<=N; i++)
     {
              scanf("%s\n", temp);
              sl = strlen(temp);
              res = 0;
              
              for(k=1; k<=D; k++)
              {
                       count = 0; flag = false; tt2 = true;
                       for(j=0; j<sl; j++)
                       {
                                if (!tt2)
                                   break;
                                if (!flag && temp[j] == '(')
                                {
                                          tt = false;
                                          flag = true;
                                          continue;
                                }
                                if (flag && temp[j] == lab[k][count])
                                {
                                         tt = true;
                                         continue;
                                }
                                if (flag && temp[j] == ')')
                                {
                                         if (!tt)
                                            tt2 = false;
                                         flag = false;
                                         count++;
                                         continue;
                                }
                                
                                if (!flag && temp[j] == lab[k][count])
                                   count++;
                                else if (!flag)
                                   tt2 = false;
                       }
                       if (tt2) res++;
              }
              printf("Case #%d: %d\n", i, res);
     }
     return;
}

int main(void)
{
    ini();
    work();
    return 0;
}
