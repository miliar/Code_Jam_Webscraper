#include <stdio.h>
#include <string>
using namespace std;

char pattern[20] = "welcome to code jam";
int DP[500][19];

int main()
{
    int N;
    scanf("%d\n", &N);
    
    for (int iq = 0; iq < N; iq++)
    {
        int ans = 0;
        
        char text[501];
        
        gets(text);
        
        printf("Case #%d: ", iq+1);
        memset(DP, 0, sizeof(DP));
        for (int i = 0; i < strlen(text); i++)
         for (int k = 0; k < 19; k++) if (text[i] == pattern[k])
         { 
             if (k == 0) DP[i][k] = 1;
             else for (int j = 0; j < i; j++) DP[i][k] += DP[j][k-1], DP[i][k] %= 10000;
             
             if (k == 18) ans += DP[i][k], ans %= 10000;
         }
         
        printf("%04d\n", ans);
    }
    return 0;
        
}
