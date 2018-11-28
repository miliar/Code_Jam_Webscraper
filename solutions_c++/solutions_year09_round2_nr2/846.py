#include <stdio.h>
#include <string.h>

char s[32];
int D[10];

int minim(int from)
{
    int i;
    
    for (i = from; i < 10; ++i)
        if (D[i])
        {
            --D[i];
            return i;
        }
    return -1;
}

int main()
{
    int T, i, j, k, len, tst, ok;
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    for (scanf("%d", &T), tst = 1; tst <= T; ++tst)
    {
        scanf("%s", &s);
        
        memset(D, 0, sizeof(D));
        len = strlen(s);
        
        ok = 0;
        for (i = len-2; i >= 0 && !ok; --i)
        {
            ++D[s[i+1]-'0'];
            for (j = s[i]-'0'+1; j < 10; ++j)
                if (D[j])
                {
                    ok = 1; 
                    ++D[s[i]-'0']; 
                    s[i] = j + '0';
                    --D[s[i]-'0'];
                    for (k = i+1; k < len; ++k)
                        s[k] = minim(0) + '0';
                    printf("Case #%d: %s\n", tst, s);
                    break;
                }
        }
        if (!ok)
        {
            ++D[s[0]-'0'];
            printf("Case #%d: %d0", tst, minim(1));
            int r;
            while ((r = minim(0)) != -1)
                printf("%d", r);
            printf("\n");
        }
    }
    
    return 0;
}
