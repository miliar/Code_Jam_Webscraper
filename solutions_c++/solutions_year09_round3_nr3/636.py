#include <cstdio>
#include <cstring>

using namespace std;

#define MAXN 5
#define MAXP 100

int n, p, q;
int tmp[MAXN + 1];
bool flag[MAXP + 1];
bool use[MAXN + 1];
int mins = 2147483647;

void ini(void)
{
    mins = 2147483647;
     memset(use, 0, sizeof(flag));
     memset(flag, 0, sizeof(flag));
     scanf("%d %d", &p, &q);
     int i;
     for(i=1; i<=q; i++)
              scanf("%d", &tmp[i]);
              
     return;
}

int getleft(int r)
{
    int i = 0;
    int sum = 0;
    for(i=r-1; i>0; i--)
    {
               if (flag[i]) return sum;
                  sum++;
    }
    return sum;
}

int getright(int r)
{
    int i = 0;
    int sum = 0;
    for(i=r+1; i<=p; i++)
    {
               if (flag[i]) return sum;
                  sum++;
    }
    return sum;
}

void work(int t, int sum)
{
     if (t > q)
     {
           if (sum < mins)
              mins = sum;
           
     }
     else
     {
         if (sum > mins)
            return;
         int i, ttmp = 0;
         for(i=1; i<=q; i++)
         {
                  if (!use[i])
                  { 
                              use[i] = true;
                              flag[tmp[i]] = true;
                              ttmp = getright(tmp[i]);
                              ttmp += getleft(tmp[i]);
                              work(t + 1, sum + ttmp);
                              flag[tmp[i]] = false;
                              use[i] = false;
                  }
         }
     }
     return;
}

int main(void)
{
    freopen("C-small.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
    
    int i;
    scanf("%d", &n);
    for(i=1; i<=n; i++)
    {
             ini();
             work(1, 0);
             printf("Case #%d: %d\n", i, mins);
    }
    
    return 0;
}
