#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cas;
    int casi;
    cin >> cas;
//    scanf("%d",&cas);
    int pd,pg;
    long long n;
    bool ans;
    int i;
    for(casi=1;casi<=cas;casi++)
    {
        ans=true;
        cin >> n >> pd >> pg;
//        cout << n << endl;
//        scanf("%d%d%d",&n,&pd,&pg);
        if(pg==0 && pd)
        {
            printf("Case #%d: Broken\n",casi);
            continue;
        }
        if(pg==100 && pd!=100)
        {
            printf("Case #%d: Broken\n",casi);
            continue;
        }
        if(n>=100)
        {
            printf("Case #%d: Possible\n",casi);
            continue;
        }
        ans=false;
        for(i=1;i<=n;i++)
        {
            if(i*pd%100==0) ans=true;
        }
        if(ans) printf("Case #%d: Possible\n",casi);
        else printf("Case #%d: Broken\n",casi);
    }
}
