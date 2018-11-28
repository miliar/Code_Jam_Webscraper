#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<stdlib.h>
using namespace std;

int T, N, i, a[50], cas, len, ok;
char s[50];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &N);
    for (cas = 1; cas <= N; cas++){
        memset(s, 0, sizeof(s));
        scanf("%s", s);
        len = strlen(s);
        for (i=0;i<len;i++) a[i] = s[i] - '0';
        ok = 0;
        for (i=1;i<len;i++)
            if (a[i-1] < a[i]) ok = 1;
        if (ok){
            next_permutation(a, a+len);
        }else{
            a[len++] = 0;  
            sort(a, a+len);
            for (i=0;i<len;i++) if (a[i] != 0) break;
            a[0] = a[i];
            a[i] = 0;
        }
        memset(s, 0, sizeof(s));
        for (i=0;i<len;i++) s[i] = a[i]+'0';
        printf("Case #%d: %s\n", cas, s);
    }
    return 0;
}
