#include<iostream>
using namespace std;
pair<int,int> a[1010];
int n;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tt,cases,i,ans;
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        scanf("%d",&n);
        for (i=0;i<n;i++)
        {
            scanf("%d",&a[i].first);
            a[i].first--;
            a[i].second=i;
        }       
        sort(a,a+n);
        ans=0;
        for (i=0;i<n;i++)
        if (a[i].second!=i) ans++;
        printf("Case #%d: %d.000000\n",tt+1,ans);
    }
    return 0;
}
