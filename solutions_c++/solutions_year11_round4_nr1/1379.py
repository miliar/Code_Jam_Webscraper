#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <utility>
#include <set>
#include <map>
using namespace std;
typedef long long LL;
struct walk{
    long t;
    long s;
}mas[1001];
bool cmp(walk a,walk b)
{
    return a.s<b.s;
}
int main()
{
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
        LL T,X,s,r,n,i,j,g,h,sum;
        LL B,E;
        double ans,t,d;
        cin>>T;
        for(int it=1;it<=T;it++){
            cin >> X >> s >> r >> t >> n;
            sum=0;
            for(i=0;i<n;i++){
                cin>>B>>E>>g;
                mas[i].t=(E-B);
                mas[i].s=g;
                sum+=mas[i].t;
            }
            mas[n].t=(X-sum);
            mas[n].s=0;
            sort(mas,mas+n+1,cmp);
            ans=0;
            for(i=0;i<=n;i++)
            {
                if(t*(r+mas[i].s)>=mas[i].t){
                    d=(mas[i].t+.0)/(r+mas[i].s);
                    ans+=d;
                    t-=d;
                }else{
                    d=(r+mas[i].s)*t;
                    ans+=(mas[i].t-d)/(s+mas[i].s)+d/(r+mas[i].s);
                    t=0;
                }
            }
            printf("Case #%d: %.8f\n",it,ans);
        }
        return 0;
}
