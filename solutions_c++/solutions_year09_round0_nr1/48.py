#include <cstdio>

int l, d, n;
char valid[30][30];
char words[10000][30];
char buf[1000];

int main()
{
    int i, j, t;
    
    scanf("%d %d %d\n", &l, &d, &n);
    
    for (i=0 ;i<d; i++)
    {
        scanf("%s", words[i]);
    }
    for (t=0; t<n; t++)
    {
        int resp = 0;
        int pos = 0;
        scanf("%s", buf);
        for(i=0; i<l; i++)
        {
            for (j=0; j<30; j++)
            {
                valid[i][j] = 0;
            }
            if (buf[pos] == '(')
            {
                pos++;
                while(1)
                {
                    if(buf[pos] == ')')
                        break;
                    valid[i][buf[pos]-'a'] = 1;
                    pos++;
                }
            }
            else
            {
                valid[i][buf[pos]-'a'] = 1;
            }
            pos++;
        }
        /*for(i=0; i<l; i++)
        {
            for (j=0; j<30; j++)
            {
                if (valid[i][j] != 0)
                    printf("%c ", (j+'a'));
            }
            printf("\n");
        }*/
        for (i=0; i<d; i++)
        {
            for (j=0; j<l; j++)
            {
                if (valid[j][words[i][j]-'a'] == 0)
                    break;
            }
            if (j == l)
                resp++;
        }
        printf("Case #%d: %d\n", t+1, resp);
    }
    return 0;
}
