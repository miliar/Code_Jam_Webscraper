#include <stdio.h>
#include <string>

char s[100];
int T, C, i, j, k, len;
int a[10];

void out()
{
    int i;
    
    for (i=0; i<10; i++) while (a[i]) { printf("%d", i); a[i] --; }
    printf("\n");
}

void go(int x)
{
    int i, k;
    
    k = 0;
    for (i=x+1; i<len-1; i++) if (s[i]<s[i+1]) k ++;
    if (k)
    {
    	printf("%c", s[x]);
    	a[s[x]-'0'] --;
    	go(x + 1);
    } else for (i=s[x]-'0'+1; i<10; i++) if (a[i]) { printf("%d", i); a[i] --; out(); }
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    scanf("%d ", &T);
    for (C=1; C<=T; C++)
    {
        scanf("%s", s);
        memset(a, 0, sizeof(a));
        for (i=0; s[i]!='\0'; i++) a[s[i] - '0'] ++; len = i;
        k = 0; for (i=0; i<len-1; i++) if (s[i]<s[i+1]) k ++;
        printf("Case #%d: ", C);
        if (k) go(0); else
        {
            for (i=1; i<10; i++) if (a[i]) { printf("%d", i); a[i] --; break; }
            a[0] ++;
            out();
        }
    }
}

