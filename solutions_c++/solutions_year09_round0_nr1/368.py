#include <stdio.h>

int in, clu, de;
char data[5000][16];
int can[15][26];

int main ()
{
    scanf("%d%d%d", &in, &clu, &de);
    for (int i = 0; i < clu; i ++)
        scanf("%s", data[i]);
    for (int i = 0; i < de; i ++)
    {
        char buf[1000];
        scanf("%s", buf);
        
        for (int j = 0; j < in; j ++)
            for (int k = 0; k < 26; k ++)
                can[j][k] = 0;
        int k = 0;
        for (int j = 0; j < in; j ++)
        {
            if (buf[k] == '(')
            {
                k ++;
                while (buf[k] != ')')
                {
                    can[j][buf[k]-'a'] = 1;
                    k ++;
                }
            }
            else
                can[j][buf[k]-'a'] = 1;
            k ++;
        }
        
        int ans = 0;
        
        for (int j = 0; j < clu; j ++)
        {
            int flag = 1;
            for (int k = 0; flag && k < in; k ++)
                flag &= can[k][data[j][k] - 'a'];
            ans += flag;
        }
        
        printf("Case #%d: %d\n", i + 1, ans);
    }
    
    return 0;
}
