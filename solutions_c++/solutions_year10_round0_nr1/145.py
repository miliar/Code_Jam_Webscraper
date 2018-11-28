//freopen("1.in","r",stdin);
//freopen("1.out","w",stdout);

#include<cstdio>
using namespace std;

int main()
{
    int t,n,k,temp,T=1;
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&k);
        temp=1;
        while(n--) temp*=2;
        if((k+1)%temp==0) printf("Case #%d: ON\n",T++);
        else printf("Case #%d: OFF\n",T++);
    }
    return 0;
}
