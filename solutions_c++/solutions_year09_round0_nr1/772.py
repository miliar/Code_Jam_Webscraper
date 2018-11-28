#include <iostream>

using namespace std;

int l,d,n;

char mas[5001][16];

void read()
{
    char hm;
    scanf("%d %d %d", &l, &d, &n);
    for(int i = 0; i < d; i ++)
    {
        scanf("%s", mas[i]);
    }
}

char bla[16][30];
char str[16*30];

int main()
{
    read();
    char ch;
    int ii;
    int ans;
    int t;
    for(int j = 1; j <= n; j ++)
    {
        ans = 0;
        memset(str, 0, sizeof(str));
        memset(bla, 0, sizeof(bla));
        scanf("%s", str);
        t=0;
        for(int i = 0; i < l; i ++)
        {
            if(str[t] == '(')
            {
                ++ t;
                while(str[t] != ')')
                {
                    bla[i][str[t] - 'a'] = 1;
                    ++ t;
                }
            }
            else bla[i][str[t] - 'a'] = 1;
            t++;
        }
        for(int k = 0; k < d; k ++)
        {
            for(ii = 0; ii < l; ii ++)
            {
                if(bla[ii][mas[k][ii] - 'a'] == 0) break;
            }
            if(ii == l) ans ++;
        }
        printf("Case #%d: %d\n",j,ans);
    }
    return 0;
}
