#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

int d[20000];
int a[20000];

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    _int64 ll,ans,tmp;
    int i,j,l,t,n,x;
    scanf("%d",&t);
    for (l=0;l<t;l++)
    {
        scanf("%lld%d",&ll,&n);
        for (i=0;i<n;i++)
            scanf("%d",&a[i]);
        sort(a,a+n);
        for (i=0;i<100*a[n-1];i++)
            d[i]=2000000000;
        d[0]=0;
        for (i=0;i<=100*a[n-1];i++)
            if (d[i]!=-1)
            {
                for (j=0;j<n;j++)
                    if (i+a[j]<=100*a[n-1])
                        if (d[i]+1<d[i+a[j]])
                            d[i+a[j]]=d[i]+1;
            }
        tmp=ll/a[n-1];
        x=ll%a[n-1];
        ans=ll+1;
        for (i=0;i<100;i++)
        {
            if ((d[x]!=2000000000)&&(tmp+d[x]<ans)) ans=tmp+d[x];
            tmp--;
            x+=a[n-1];
            if (tmp<0) break;
        }
        if (ans==ll+1)
            printf("Case #%d: IMPOSSIBLE\n",l+1);
        else
            printf("Case #%d: %lld\n",l+1,ans);
    }
	return 0;
}

