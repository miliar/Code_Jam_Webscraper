#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>

using namespace std;
#define MaxN 1000

char x[20] = "welcome to code jam";
char y[MaxN];
int f[20];

void solve()
{
    memset(f,0,sizeof(f));
    int len = strlen(y);
    f[0] = 1;
    for (int i = 1; i <= len ; i++)
      {
          for (int j = 19; j >= 1; j--)
           if (y[i - 1] == x[j - 1]) f[j] = (f[j] + f[j - 1]) % 10000;
      }
    printf("%04d\n", f[19]);
}

int main()
{
//    freopen("test.in","r",stdin);
//    freopen("test.out","w",stdout);
    int Case;
    scanf("%d", &Case); 
    getchar();
    for (int i = 1; i <= Case ; i++)
    {
        printf("Case #%d: ",i); 
        gets(y);
        solve();
    }   
    return 0;
}

