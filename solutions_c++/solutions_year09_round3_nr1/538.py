#include <iostream>
#include <stdio.h>
#include <map>
#include <math.h>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>

using namespace std;

int i,t,fix[300],l,r,n;
char s[300];

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d\n",&t);
    for (i=1; i<=t; i++)
    {
        memset(fix,-1,sizeof(fix));
        gets(s);
        n=strlen(s);
        fix[ s[0] ]=1; r=0;
        for (l=1; l<n; l++)
        {
         if (r==1) r++;
         if (fix[ s[l] ]==-1) fix[ s[l] ] = r++;
        }
        if (r<2) r=2;
     //   for (l=0; l<n; l++) cout<<fix[s[l]]<<endl;
        long long ans=0,xar=1;
        for (l=n-1; l>=0; l--)
           { ans+=1LL*xar*fix[ s[l] ]; xar*=r; }
        printf("Case #%d: ",i); cout<<ans<<endl;
    }
    return 0;
}
