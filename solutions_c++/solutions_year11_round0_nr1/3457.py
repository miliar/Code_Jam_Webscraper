#include "iostream"
using namespace std;
#include "stdio.h"
#include "string.h"

inline int maxInt(int a,int b)
{
       return a>b?a:b;
}
inline int iAbs(int a)
{
       return a>0?a:-a;
}

int main()
{
    int tt;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&tt);
    for(int ti=1;ti<=tt;ti++)
    {
            int pb=1,tb=0,po=1,to=0;
            int timenow=0,p=0;
            int n,i,j;
            char s[10];
            scanf("%d",&n);
            for(i=0;i<n;i++)
            {
                scanf("%s",s);
                scanf("%d",&p);
                if(s[0]=='O')
                {
                    to += iAbs(p-po)+1;
                    po = p;
                    timenow = maxInt(timenow+1,to);
                    to = timenow;
                }
                else
                {
                    tb += iAbs(p-pb)+1;
                    pb = p;
                    timenow = maxInt(timenow+1,tb);
                    tb = timenow;
                }
            }
            printf("Case #%d: %d\n",ti,timenow);
    }
    return 0;
}
