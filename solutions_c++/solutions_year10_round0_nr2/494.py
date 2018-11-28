#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <queue>
#include <list>
#include <set>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);

    int i,j,n,test,Case=1,minv,a[10],diff[10],x,ind,maxv,cnt,ans;

    scanf("%d",&test);
    while(test--)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%d",&a[i]);
        sort(&a[0],&a[n]);
        for(i=1;i<n;i++)
            diff[i-1]=a[i]-a[i-1];
        x=diff[0];
        for(i=1;i<n-1;i++)
            x=__gcd(x,diff[i]);
        //cout<<x<<endl;
        if(a[0]%x==0)
            ans=0;
        else ans=x-(a[0]%x);
        printf("Case #%d: %d\n",Case++,ans);
    }

    return 0;
}
