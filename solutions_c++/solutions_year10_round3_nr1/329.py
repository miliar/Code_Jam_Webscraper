#include<iostream>
using namespace std;
struct point{
    int a,b;
}p[1005];
int n;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("tout.txt","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {
        int ans=0;
        cin>>n;
        int i;
        for(i=0;i<n;i++)
        {
            cin>>p[i].a>>p[i].b;
        }
        for(i=0;i<n;i++)
            for(int j=i+1;j<n;j++)
            {
                if((p[i].a-p[j].a)*(p[i].b-p[j].b)<0)
                    ans++;
            }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
