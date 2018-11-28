#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char s[1009], t[1009];
const char *st = "welcome to code jam";
int n, i, j, k, tn, d[1009], len, tt;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%d", &n);
    gets(s);
    for (tt=1;tt<=n;tt++){
        gets(t);
        tn = strlen(t);
        len = strlen(st);
        memset(d, 0, sizeof(d));
        for (i=0;i<tn;i++) if (t[i]=='m') d[i] = 1;
        
        for (i=len-2;i>=0;i--){
            k = 0;
            for (j=tn-1;j>=0;j--){
                if (t[j] == st[i]){ 
                    d[j] = k;  
                    //printf("d[%d] = %d\n", j, k);
                }
                if (t[j] == st[i+1]) k += d[j];
                if (k >= 10000) k%= 10000;
            }
            for (j=tn-1;j>=0;j--)
                if (t[j] != st[i]) d[j] = 0;  
        }
        k = 0;
        for (j=tn-1;j>=0;j--){
            if (t[j] == 'w') k += d[j];
            if (k >= 10000) k%= 10000;
        }
        printf("Case #%d: %04d\n", tt, k);
    }
    return 0;
}
/*
4
elcomew elcome to code jam
wweellccoommee to code qps jam
welcooomooe tooo cooodooe jam
*/
