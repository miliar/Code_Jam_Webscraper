#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;
int a[10050];
int main()
{
    int i,j,k,l,test,mx,n,s[10005],e[10005],mx1,t=1;
    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);

    scanf("%d",&test);
    while(test--)
    {
        scanf("%d",&n);
        memset(a,0,sizeof(a));
         mx1=0;
        for(i=0;i<n;i++)
        {
            scanf("%d %d",&s[i],&e[i]);

        }
        mx=0;
        for(i=0;i<n;i++)
        {
            int c=0;
          for(j=0;j<n;j++)
          {
              if(i==j)
              continue;
              if((s[i]>s[j]&&e[i]<e[j])||(s[i]<s[j]&&e[i]>e[j]))
              c++;
          }
            if(c>mx)
            mx=c;
        }
        printf("Case #%d: %d\n",t++,mx);

    }
    return 0;
}
