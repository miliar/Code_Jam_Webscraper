#include <iostream>
using namespace std;

#define MaxLen 500
#define MOD 10000

char s[MaxLen+5];
int d[2][19];
int now,pre;
int n;
char str[19] = { 'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m' };
int len;

int main()
{
    
    
    scanf("%d",&n);
    gets(s);
    for (int k = 0; k < n; k++) {
        
        gets(s);
        len = strlen(s);
        
        now = 0; pre = 1;
        memset(d, 0, sizeof(d));
        if ( s[0] == 'w' ) d[0][0] = 1;
        for (int i = 1; i < len; i++) {
            now = 1 - now; pre = 1 - pre;
            memset(d[now],0,sizeof(d[now]));
            if ( s[i] == 'w' ) d[now][0]++;
            d[now][0] = ( d[now][0] + d[pre][0] ) % MOD;
            for (int j = 1; j < 19; j++) {
              if ( s[i] == str[j] )
                 d[now][j] = (d[now][j] + d[pre][j-1]) % MOD;
              d[now][j] = ( d[now][j] + d[pre][j] ) % MOD;
            }
        }
        
        printf("Case #%d: %.4d\n",k+1,d[now][18]);
        
    }
    
    return 0;
}
