#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <utility>
#include <functional>
#include <sstream>
#include <climits>
#include <cfloat>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstring>
#include <cstdio>
using namespace std;

const int N=1000;

struct node
{
    int w,d;
    node(int w=0,int d=0)
    {
        this->w=w;
        this->d=d;
    }
    bool operator<(const node &x) const
    {
        return w<x.w;
    }
};

node a[N+1];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Tests;
    scanf("%d",&Tests);
    for(int Test=1;Test<=Tests;Test++)
    {
        printf("Case #%d: ", Test);
        //
        int x,s,r,t,n;
        scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
        for(int i=0;i<n;i++)
        {
            int w,b,e;
            scanf("%d%d%d",&b,&e,&w);
            a[i]=node(w,e-b);
            x-=e-b;
        }
        a[n]=node(0,x);
        sort(a,a+n+1);
        double res=0;
        double T=t;
        for(int i=0;i<=n;i++)
        {
            double z=((double)a[i].d)/(a[i].w+r);
            if(z>T)
            {
                res+=T;
                res+=(a[i].d-(a[i].w+r)*T)/(a[i].w+s);
                T=0;
            }
            else
            {
                res+=z;
                T-=z;
            }
        }
        printf("%.10lf\n",res);
    }
    return 0;
}
