#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char a[200];
char s[110];
int main() {
    freopen("/Users/martreenl/Downloads/A-small-attempt3.in", "r", stdin);
    freopen("/Users/martreenl/Downloads/A-small-attempt3.out", "w", stdout);
    
    a['a']='y'; a['b']='h'; a['c']='e'; a['d']='s'; a['e']='o';
    a['f']='c'; a['g']='v'; a['h']='x'; a['i']='d'; a['j']='u';
    a['k']='i'; a['l']='g'; a['m']='l'; a['n']='b'; a['o']='k';
    a['p']='r'; a['q']='z'; a['r']='t'; a['s']='n'; a['t']='w';
    a['u']='j'; a['v']='p'; a['w']='f'; a['x']='m'; a['y']='a';
    a['z']='q';
    
    int n;
    scanf("%d", &n);
    gets(s);
    for (int i=0; i<n; ++i) {
        gets(s);
        printf("Case #%d: ", i+1);
        for (int j=0; j<strlen(s); ++j)
            if (s[j] == ' ') printf(" ");
            else printf("%c", a[s[j]]);
        printf("\n");
    }
    return 0;
}










/*#include<stdio.h>
#include<string.h>
#include<stdlib.h>
const int N = 1000010;
int a[N];

int main() {
    int n, ans=0, sum=0;
    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        int k;
        scanf("%d", &k);
        scanf("%d", &a[k]);
        a[k]=a[k]%30;
    }
    for (int i=1; i<=n; i++) {
        if (sum+5<=30) {
            sum=(sum+5+a[i])%30;
        }
        else {
            ans+=30-sum;
            sum=(5+a[i])%30;
        }
    }
    printf("%d\n",ans);
    return 0;
}*/