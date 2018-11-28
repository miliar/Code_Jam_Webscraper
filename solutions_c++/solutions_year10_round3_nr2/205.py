#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    freopen("C:/Users/FengJinwen/Desktop/B-large.in", "r", stdin);
    freopen("C:/Users/FengJinwen/Desktop/ans.txt", "w", stdout);
    int l,p,c;
    int i,n;
    double ans;
    int ss;
    scanf("%d",&n);
    for (i=1;i<=n;i++)
    {
        scanf("%d%d%d",&l,&p,&c);
        ans=log(log(p*1.0/l*1.0)/log(c*1.0))/log(2.0);
        ss=int(ans);
        if (ans>ss) ss++;
        if (ss<0) ss=0;
        printf("Case #%d: %d\n",i,ss);
    }

}
