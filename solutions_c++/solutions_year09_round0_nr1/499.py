#include<stdio.h>
int l, d, n;

bool b[20][26];
char s[2000];
char word[5000][50];

void get_match()
{
    int i, len = 0, j;
    
    for(i = 0; i < l; i ++)
        for(j = 0; j < 26; j ++)
            b[i][j] = false;
    for(i = 0; s[i] != '\0'; )
    {
        if(s[i] == '(')
        {
            i ++;
            for(j = 0; s[i + j] != ')'; j ++)
                b[len][s[i + j] - 'a'] = true;
            i = i + j + 1;
        }
        else
        {
            b[len][s[i] - 'a'] = true; 
            i ++;
        }
        len ++;
    }
}
int main()
{
    int i, t, ans, j;
    scanf("%d%d%d", &l, &d, &n);
    for(i = 0; i < d; i ++)
        scanf("%s", word[i]);
    for(t = 1; t <= n; t ++)
    {
        scanf("%s", s);
        get_match();
        ans = 0;
        for(i = 0; i < d; i ++)
        {
            for(j = 0; j < l; j ++)
            {
                if(!b[j][word[i][j] - 'a'])
                    break;
            }
            if(j == l)
                ans ++;
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
