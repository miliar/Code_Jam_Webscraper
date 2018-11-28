#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
int n,s,p;
int a[1005];
int main()
{
    int T,ans;
    freopen("E:\\B-small-attempt1.in","r",stdin);
    freopen("E:\\B.out","w",stdout);
    scanf("%d",&T);
    for (int ca=1;ca<=T;ca++)
    {
        scanf("%d%d%d",&n,&s,&p);
        for (int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        sort(a,a+n);
        ans=0;
        for (int i=0;i<n;i++)
        {
            if (a[i]==0 && p!=0) continue;
            if (p*3-2<=a[i]) ans++;
            else if ((p*3-4==a[i] || p*3-3==a[i]) && s)
            {
                s--;
                ans++;
            }
//            int avg=a[i]/3;
//            if (avg>=p) ans++;
//            else if (avg==p-1)
//            {
//                if (a[i]%3==0 && s) {ans++;s--;}
//                else if (a[i]%3!=0) ans++;
//            }
//            else if (avg==p-2 && a[i]%3==2)
//            {
//                ans++;
//                s--;
//            }
        }
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
