#include <cstdio>
#include <cstring>

using namespace std;


int n;
char temp[10000];
int lt;
int number[50];
long long muln[20];
     long long res = 0;

void ini(void)
{
     scanf("%s\n", temp);    
     lt = strlen(temp);
     memset(number, -1, sizeof(number));
     
     return;
}

int getnu(char t)
{
    if ('0' <= t && t <= '9')
       return t - '0';
    else
       return 10 + (t - 'a');
}

void work(void)
{
     int i, j, k, l;
     k = 0;
     
     for(i=0; i<lt; i++)
     {
              l = getnu(temp[i]);
              if (i == 0)
                 number[l] = 1;
              else
              {
                  if (number[l] == -1)
                  {
                                if (k == 1) k++;
                                number[l] = k;
                                k++; 
                  }
              }
     }
     
     if (k == 0)
     {
           muln[0] = 1;
           for(i=1; i<=lt; i++)
              muln[i] = muln[i - 1] * 2;
           res = muln[lt] - 1;
           return; 
     }
     
     if (k == 1) k++;
     
     res = 0;
     muln[0] = 1;
     for(i=1; i<lt; i++)
              muln[i] = muln[i - 1] * k;
     
     for(i=0; i<lt; i++)
              res += muln[lt - 1 - i] * number[getnu(temp[i])];
     
     return;
}



int main(void)
{
    freopen("A-small.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
     
    scanf("%d\n", &n);
    int i;
    for(i=1; i<=n; i++)
    {    
        ini();
        work();
        printf("Case #%d: %I64d\n", i, res);
    }
    return 0;
}
