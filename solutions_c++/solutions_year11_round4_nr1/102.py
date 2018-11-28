#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;
double tst()
{
    int x;
    int s;
    int r;
    cin >> x >> s >> r;
    r -= s;
    int n;
    double t;
    cin >> t >> n;
    vector<pair<int,int> > wl(n);
    for(int i=0;i<n;i++)
    {
        int b,e,w;
        cin >> b >> e >> w;
        wl[i].first = w+s;
        wl[i].second = e-b;
        x -= (e-b);
    }
    n++;
    wl.push_back(make_pair(s,x));
    sort(wl.begin(),wl.end());

    double ans=0;
    for(int i=0;i<n;i++)
    {
        int w = wl[i].first;
        int l = wl[i].second;
        if(l/((double)w+r)<=t)
        {
            ans += l/((double)w+r);
            t -= l/((double)w+r);
        }
        else
        {
            ans += t + (l-t*((double)w+r))/((double)w);
            t = 0;
        }
    }
    return ans;

}
int main()
{
    int t;
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: %.7lf\n",i,tst());
    }

}
