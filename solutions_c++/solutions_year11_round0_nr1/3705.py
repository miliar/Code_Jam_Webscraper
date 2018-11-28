#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
using namespace std;
int T,n;
struct data
{
    int x;
    char f;
};
data R[10005];
void init()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&T);
}
int abs(int a,int b)
{
    if (a>b) return a-b;
    else return b-a;
}
int solve()
{
    memset(R,0,sizeof(R));
    int i,j,cnt=0;
    scanf("%d",&n);
    int tb=0,to=0;
    for (i=0;i<n;i++)
    {
        data tmp;
        scanf("%s %d",&tmp.f,&tmp.x);
        R[cnt++]=tmp;
    }
    int posb=1,poso=1;
    for (i=0;i<cnt;i++)
    {
        if (R[i].f=='B')
        {
            int d=abs(R[i].x,posb);
            posb=R[i].x;
            tb=max(tb+d,to)+1;
        }
        else
        {
            int d=abs(poso,R[i].x);
            poso=R[i].x;
            to=max(to+d,tb)+1;
        }
    }
    int ans=max(to,tb);
    return ans;
}
int main()
{
    init();
    for (int cases=1;cases<=T;cases++)
    {
        int ans=solve();
        printf("Case #%d: %d\n",cases,ans);
    }
    return 0;
}
