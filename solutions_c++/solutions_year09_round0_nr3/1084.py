#include <stdio.h>
#include <string.h>

int main()
{
    freopen("C-large.in", "rt", stdin);
    freopen("C-large.txt", "wt", stdout);
    
    int t;
    char txt[1000];
    
    scanf("%d\n", &t);
    
    for(int tt = 1; tt <= t; tt++)
    {
        gets(txt);
//        printf("%s\n", txt);

        int l = strlen(txt);
        int cnt[20];

        memset(cnt, 0, sizeof(int)*20);
        
        for(int i = 0; i < l; i++)
        {
            switch(txt[i])
            {
            // welcome to code jam
            case 'w': cnt[0]++; break;
            case 'e': cnt[1] += cnt[0];  cnt[6] += cnt[5]; cnt[14] += cnt[13]; break;
            case 'l': cnt[2] += cnt[1]; break;
            case 'c': cnt[3] += cnt[2]; cnt[11] += cnt[10]; break;
            case 'o': cnt[4] += cnt[3]; cnt[9] += cnt[8]; cnt[12] += cnt[11]; break;
            case 'm': cnt[5] += cnt[4]; cnt[18] += cnt[17]; break;
//          case 'e': cnt[6] += cnt[5]; break;
            case ' ': cnt[7] += cnt[6]; cnt[10] += cnt[9]; cnt[15] += cnt[14]; break;
            case 't': cnt[8] += cnt[7]; break;
//            case 'o': cnt[9] += cnt[8]; break;
//            case ' ': cnt[10] += cnt[9]; break;
//          case 'c': cnt[11] += cnt[10]; break;
//            case 'o': cnt[12] += cnt[11]; break;
            case 'd': cnt[13] += cnt[12]; break;
//          case 'e': cnt[14] += cnt[13]; break;
//            case ' ': cnt[15] += cnt[14]; break;
            case 'j': cnt[16] += cnt[15]; break;
            case 'a': cnt[17] += cnt[16]; break;
//            case 'm': cnt[18] += cnt[17]; break;
            }
            
            for(int j = 0; j <= 18; j++)
                cnt[j] %= 10000;
        }
        
        printf("Case #%d: %.4d\n", tt, cnt[18]);
    }
    
//    for(;;);
    
    return 0;
}
