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
#include<string.h>

using namespace std;
int A[101],W[101],T[10001],arr[101];
char S[1001],SS[101][101];
int k,c;
bool valid(int r,int cc)
{
    if(r>=k || cc>=c || r<=-1 || cc<=-1) return 0;
    return 1;
}
int main()
{
   freopen("c.txt","r",stdin);
   freopen("c.out","w",stdout);
    int t,i,j,cnt,w,l,cas=1,ans;
    double RPI,WP,OWP,OOWP;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d %d",&k,&c,&w);
        for(i=0;i<k;i++) scanf("%d",&T[i]);

          for(i=c;i<=w;i++)
          {
              l=0;
            for(j=0;j<k;j++)
            {
                if(T[j]%i==0 || i%T[j]==0) continue;
                    l=1; break;
            }
            if(l==0){ans=i;break;}
          }

          if(l) printf("Case #%d: NO\n",cas++);
          else
          printf("Case #%d: %d\n",cas++,ans);
    }

    return 0;
}
