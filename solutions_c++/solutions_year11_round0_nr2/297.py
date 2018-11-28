#include<stdio.h>
#include<string.h>

char com[300][300];
bool opp[300][300];

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    
    int T, tt, n, i, j;
    char str[128], stack[128], top;
    
    scanf("%d", &T);
    for(tt = 1; tt <= T; tt++)
    {
        memset(com, 0, sizeof(com));
        memset(opp, 0, sizeof(opp));
        scanf("%d", &n);
        while(n--){
            scanf("%s", &str);
            com[str[0]][str[1]] = com[str[1]][str[0]] = str[2];
        }
        scanf("%d", &n);
        while(n--){
            scanf("%s", &str);
            opp[str[0]][str[1]] = opp[str[1]][str[0]] = true;
        }
        scanf("%d %s", &n, &str);
        stack[0] = str[0];
        top = 0;
        for(i = 1; i < n; i++){
            if(top >= 0 && com[str[i]][stack[top]] > 0){
                stack[top] = com[str[i]][stack[top]];
                continue;
            }
            for(j = 0; j <= top; j++)
                if(opp[stack[j]][str[i]]) break;
            if(j <= top){
                top = -1;
                continue;
            }
            stack[++top] = str[i];
        }
        printf("Case #%d: [", tt);
        if(top >= 0)printf("%c", stack[0]);
        for(i = 1; i <= top; i++) printf(", %c", stack[i]);
        printf("]\n");
    }    
    return 0;
}
