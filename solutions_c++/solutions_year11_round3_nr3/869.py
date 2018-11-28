#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;
int n,l,h;
int a[105];
int main()
{
//    freopen("C-small-attempt0.in","r",stdin);
//    freopen("C-small-attempt0.out","w",stdout);
    int i,j;
    int t;
    int cases = 1;
//    int flag ;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&n,&l,&h);
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        for(i=l;i<=h;i++)
        {
//            flag = 0;
            for(j=0;j<n;j++)
            {
                if(!(i%a[j]==0 || a[j]%i==0))
                    break;
            }
            if(j==n) break;
        }
        if(i>h) printf("Case #%d: NO\n",cases++);
        else printf("Case #%d: %d\n",cases++,i);
    }
	return 0;
}
