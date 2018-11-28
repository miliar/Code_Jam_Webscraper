#include<iostream>
using namespace std;

struct type
{
    int a,b;
}X[1005];

bool cmp(const type &a, const type &b)
{return a.a<b.a;}
int main()
{
    freopen("C:\\Users\\Administrator\\Desktop\\IN.txt","r",stdin);
    freopen("C:\\Users\\Administrator\\Desktop\\OUT.txt","w",stdout);
    int test,n;
    scanf("%d",&test);
    for(int t=1; t<=test; t++)
    {
        scanf("%d",&n);
        for(int i=0; i<n; i++)
        {
            scanf("%d%d",&X[i].a, &X[i].b);
        }    
        sort(X, X+n, cmp);
        int ans=0;
        for(int i=0; i<n; i++)
        {
            for(int j=i+1; j<n; j++)
            {
                if(X[i].b>X[j].b)
                ans++;
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }
}
