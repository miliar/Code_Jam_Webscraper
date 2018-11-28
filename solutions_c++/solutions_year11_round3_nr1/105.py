#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <cstring>
#include <queue>
#include <map>
#include <set>

using namespace std;

int n,i,p,l,k,t;
char s[200][200];
int main()
{
    
    
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    
    scanf("%d",&t);
    for (i = 1; i <= t; i++)
    {
        scanf("%d%d\n",&n,&p);
        for (l=0; l<n; l++) gets(s[l]);
        printf("Case #%d:\n",i);
        
        for (l=0; l<n-1; l++)
            for (k=0; k<p-1; k++)
                if (s[l][k]=='#')
                    if (s[l][k+1]=='#' && s[l+1][k]=='#' && s[l+1][k+1]=='#')
                    {
                        s[l][k] = s[l+1][k+1] = '/';
                        s[l+1][k] = s[l][k+1] = 92;
                    }
       int boo = 1;
       for (l=0; l<n; l++)
         for (k=0; k<p; k++) 
            if (s[l][k]=='#') boo = 0;
            
       if (!boo) puts("Impossible"); else 
       for (l=0; l<n; l++) puts(s[l]);
    }
    
    return 0;
}
