#include<cstdio>
#include<cstring>
#include<cctype>
using namespace std;
int T,n,S,p;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d %d %d",&n,&S,&p);
        int ans=0,a;
        while(n--)
        {
            scanf("%d",&a);
            if(a%3==0) {
                a=a/3;
                if(a==p-1&&S&&a>=1) S--,ans++;
                else if(a>=p) ans++;
            }
            else if(a%3==2) {
                a=(a+1)/3;
                if(a>=p&&a>=1) ans++;
                else if(a==p-1&&S) S--,ans++;
            }
            else if(a%3==1){
                a=(a+2)/3;
                if(a>=p) ans++;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
    
