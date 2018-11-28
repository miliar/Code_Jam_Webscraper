#include <cstdio>
#include <cstring>

#define MOD 10000
#define SIZE 19
char frase[20] = "welcome to code jam";
char buf[10000];
int len;
int quant[20];

int main()
{
    int t;
    int i, j, k;
    int resp = 0;
    
    scanf("%d\n", &t);
    
    for (int teste=0; teste<t; teste++)
    {
        resp = 0;
        gets(buf);
        len = strlen(buf);
        for (i=0; i<SIZE; i++)
        {
            quant[i] = 0;
        }
        for (i=0; i<len; i++)
        {
            char let = buf[i];
            if (let == 'm')
            {
                resp = (resp + quant[SIZE-2]) % MOD;
            }
            for (j=SIZE-2; j>0; j--)
            {
                if (let == frase[j])
                {
                    quant[j] =  (quant[j] + quant[j-1]) % MOD;
                }
            }
            if (let == 'w')
            {
                quant[0] = (quant[0] + 1) % MOD;
            }
        }
        printf("Case #%d: %04d\n", teste+1, resp);
    }
    return 0;
}
