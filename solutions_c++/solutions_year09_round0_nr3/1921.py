#include <iostream>

using namespace std;

const char a[19] = {'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};
const int n = 19;

int m;
char s[510];
int f[20][510];

void init()
{
     char c;
     
     m=0;
     while (scanf("%c", &c)!=EOF)
     {
           if (c=='\n') break;
           s[m] = c;
           m++;      
     }
}

void work()
{
     int i, j;
     memset(f, 0, sizeof(f));
     if (s[0] == a[0]) f[0][0] = 1;
     for (j=1; j<m; j++)
         if (s[j] == a[0]) f[0][j] = (f[0][j-1]+1)%10000; else f[0][j] = f[0][j-1];
     for (i=1; i<n; i++)
         for (j=1; j<m; j++)
             if (s[j] == a[i])
                f[i][j] = (f[i-1][j-1]+f[i][j-1])%10000;
             else
                f[i][j] = f[i][j-1];
     printf("%04d\n", f[n-1][m-1]);
}
     
int main()
{
    int t, i;
    
    scanf("%d\n",&t);
    i = 0;
    while (t--)
    {
          printf("Case #%d: ", ++i);
          init();
          work();
                
    }    
    return 0;
}
