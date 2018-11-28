#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
int a[111];
int T;
int n,m,k;
int main()
{
  //  freopen("out.txt","w",stdout);
    cin>>T;
    int casno=1;
    while(T--)
    {
        cin>>n>>m>>k;
        for(int i=0;i<n;i++) cin>>a[i];
        int ans=0;
        for(int i=0;i<n;i++)
        {
            if(a[i]<=1)
            {
                if(a[i]==0&&k==0) ans++;
                if(a[i]==1&&k<=1) ans++;
                continue;
            }
            if(a[i]>=3*k-2) ans++;
            if(a[i]<3*k-2&&a[i]>=3*k-4&&m!=0) m--,ans++;
        }
        printf("Case #%d: %d\n",casno++,ans);
    }
}
