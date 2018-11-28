#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
using namespace std;
#define pb push_back
#define mp make_pair
#define tr(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define all(x) x.begin(),x.end()

void tst()
{
    int w;
    int l,u;
    int g;
    cin >> w >> l >> u >> g;
    vector<int> lx(l);
    vector<int> ly(l);

    vector<double> hl(w+2),hu(w+2);
    for(int i=0;i<l;i++)
        cin >> lx[i] >> ly[i];

    vector<int> ux(u);
    vector<int> uy(u);

    for(int i=0;i<u;i++)
        cin >> ux[i] >> uy[i];

    for(int i=0;i+1<l;i++)
        for(int j=lx[i];j<=lx[i+1];j++)
            hl[j] = (j-(double)lx[i])/(lx[i+1]-(double)lx[i]) * (ly[i+1]-ly[i]) + ly[i];
    hl[w+1]=hl[w];
    
    for(int i=0;i+1<u;i++)
        for(int j=ux[i];j<=ux[i+1];j++)
            hu[j] = (j-(double)ux[i])/(ux[i+1]-(double)ux[i]) * (uy[i+1]-uy[i]) + uy[i];
    hu[w+1]=hu[w];



    vector<double> pl(w+2),pu(w+2);

    for(int i=1;i<w+2;i++)
    {
        pl[i] = pl[i-1] + (hl[i]+hl[i-1])/2;
        pu[i] = pu[i-1] + (hu[i]+hu[i-1])/2;
    }

    double totarea = pu[w]-pl[w];

    for(int i=1;i<g;i++)
    {
        double s = (totarea * i) / g;
        double low = 0;
        double high = w;
        while(high>low+0.0000001)
        {
            double mid = (low+high)/2;
            double ar=0;
            int mm = (int)mid;
            ar += pu[mm];
            ar -= pl[mm];

            ar += (hu[mm]+(hu[mm+1]-hu[mm])*(mid-mm)+hu[mm])/2 * (mid-mm);
            ar -= (hl[mm]+(hl[mm+1]-hl[mm])*(mid-mm)+hl[mm])/2 * (mid-mm);

            if(ar > s)
                high = mid;
            else
                low = mid;


        }
        printf("%.6lf\n",(low+high)/2);
    }


}

int main()
{
    int t;
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d:\n",i);
        tst();
    }
}
