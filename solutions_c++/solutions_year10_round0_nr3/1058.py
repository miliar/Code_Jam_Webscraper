#include <iostream>
using namespace std;
int a[2000],b[2000],c[2000];
int used[2000],post[2000];
int main()
{
    freopen( "C:/Users/FengJinwen/Desktop/C-small-attempt1.in", "r", stdin );
    freopen( "C:/Users/FengJinwen/Desktop/ans.txt", "w", stdout );
    int t,p;
    int r,m,n,temp,r1,r2,r3;
    int i,j,tempj;
    __int64 ans;
    bool round;
    scanf("%d",&t);
    for (p=1;p<=t;p++)
    {
        round=false;
        ans=0;
        memset(used,0,sizeof(used));
        memset(post,0,sizeof(post));
        scanf("%d%d%d",&r,&m,&n);
        for (i=0;i<n;i++)
            scanf("%d",&a[i]);
        j=0;
        for (i=1;i<=r;i++)
        {
            temp=0;
            tempj=j;
            while (temp+a[j]<=m)
            {
                temp+=a[j];
                j++;
                if (j>=n) j%=n;
                if (j==tempj) break;
            }
            ans+=temp;
        }
        printf("Case #%d: %d\n",p,ans);
    }
}
