#include<iostream>
#include <algorithm>

using namespace std;

double cnt,tt = 0;

struct pint{
    double sta;
    double from,to;
};
bool cmp(pint a, pint b)
{
    return a.sta < b.sta;
}
struct pint Pint[1001000];
int n,x,s,r,t;
double ans,has = 0.0;


int main(){
    freopen("A-large.in","r",stdin);
    freopen("jeogia.txt","w",stdout);
    scanf("%lf",&cnt);
    while(true)
    {
        if (cnt == 0) break;
        cnt = cnt - 1;
        scanf("%lf %lf %lf %lf %lf",&x,&s,&r,&t,&n);
        for(int i=1;i<=n;i++)
            scanf("%lf %lf %lf",&Pint[i].from,&Pint[i].to,&Pint[i].sta);

        Pint[n+1].from = 0, Pint[n+1].to = Pint[1].from, Pint[n+1].sta = 0;
        for(int i=1;i<n;i++)
        {
            Pint[n+1+i].from = Pint[i].to;
            Pint[n+1+i].to = Pint[i+1].from;
            Pint[n+1+i].sta = 0;
        }
        Pint[2*n+1].from = Pint[n].to, Pint[2*n+1].to = x, Pint[2*n+1].sta = 0;

        sort(Pint + 1, Pint +1 + 2*n + 1, cmp);

        has = (double)t;
        ans = 0.0;

        for(int i=1;i<=2*n+1;i++)
        {
            if(1.0 * (Pint[i].to - Pint[i].from) / (Pint[i].sta + r) <= has)
            {
                has -= 1.0 * (Pint[i].to - Pint[i].from) / (Pint[i].sta + r);
                ans += 1.0 * (Pint[i].to - Pint[i].from) / (Pint[i].sta + r);
            }else
            {
                ans += has + (Pint[i].to - Pint[i].from - has * (Pint[i].sta + r)) / (Pint[i].sta + s);
                has = 0;
            }
        }
        printf("Case #%d: %.10lf\n",++tt,ans);
    }
    return 0;
}

