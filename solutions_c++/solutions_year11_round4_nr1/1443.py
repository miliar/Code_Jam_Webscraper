#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define maxn 1010
double t;
double X;
int N;
int T;
double S,R;
struct Node
{
    double length;
    double w;
}nd[maxn];
bool cmp(Node nd1,Node nd2)
{
    return nd1.w < nd2.w;
}
int main()
{
    double B,E;
    int i;
    double left;
    double sum;
    double tleft;
    double ans;
    int cs;
    freopen("A-large.in","r",stdin);
    freopen("A-small.out","w",stdout);
    while(scanf("%d",&T)!=EOF)
    {
        cs = 1;
        while(T--)
        {
            scanf("%lf%lf%lf%lf%d",&X,&S,&R,&t,&N);
            sum = 0.0;
            for(i = 0 ; i < N; i++)
            {
                scanf("%lf%lf%lf",&B,&E,&nd[i].w);
                nd[i].length = E - B;
                sum += nd[i].length;
            }
            sort(nd,nd+N,cmp);
//            printf("%.2lf\n",sum);
            tleft = t;
            left = X - sum;
            ans = 0.0;
            if(R * tleft > left)
            {
               ans = left / R;
               tleft -= ans;
            }
            else
            {
                ans = (left - R * tleft)/S + tleft;
                tleft = 0.0;
            }
  //          printf("%.8lf\n",ans);
            for(i = 0 ; i < N ; i++)
            {
                if((R+nd[i].w) * tleft > nd[i].length){
                    ans += nd[i].length/(R+nd[i].w);
                    tleft -= nd[i].length/(R+nd[i].w);
                }
                else
                {
                    ans += (nd[i].length - (R + nd[i].w) * tleft)/(S+nd[i].w) + tleft;
                    tleft = 0;
                }
            }
            printf("Case #%d: %.9lf\n",cs++,ans);
        }
    }
    return 0;
}
