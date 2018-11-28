#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

void tst()
{
    int n,w,l;
    cin >> n >> w >> l;
    vector<int> r(n);
    for(int i=0;i<n;i++)
        cin >> r[i];
    vector<int> x(n,-1);
    vector<int> y(n,-1);

    vector<pair<int,int> > ri(n);
    for(int i=0;i<n;i++)
        ri[i] = make_pair(r[i],i);
    sort(ri.begin(),ri.end());
    reverse(ri.begin(),ri.end());
    int left = n;

    int Y = -1000000;
    for(;;)
    {
        int W = 0;
        if(left==0)
            break;
        int i1=0;
        for(;i1<n;i1++)
            if(x[ri[i1].second]==-1)
                break;
        x[ri[i1].second] = 0;
        Y += ri[i1].first;
        Y = max(0,Y);
        y[ri[i1].second] = Y;
        W += ri[i1].first;
        left--;
        if(left==0)
            break;
        int i2=i1+1;
        for(;i2<n;i2++)
            if(x[ri[i2].second]==-1 && W+ri[i2].first<=w)
                break;
        if(i2!=n)
        {
        x[ri[i2].second] = w;
        y[ri[i2].second] = Y;
        W += ri[i2].first;
        left--;
        if(left==0)
            break;
        int lx = ri[i1].first;
        for(int i3=i2+1;i3<n;i3++)
            if(x[ri[i3].second]==-1 && W+2*ri[i3].first<=w)
            {
                x[ri[i3].second] = lx + ri[i3].first;
                y[ri[i3].second] = Y;
                lx += 2*ri[i3].first;
                W += 2 *ri[i3].first;
                left--;
            }
        }
        Y += ri[i1].first;
    }
    for(int i=0;i<n;i++)
        cout << ' ' << x[i] << ' ' << y[i];
    
}

int main()
{
    int t;
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        cout << "Case #"<< i <<":";
        tst();
        cout << endl;
    }
}
