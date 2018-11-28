#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cstdlib>
#include <cassert>

#define pb push_back
#define mp make_pair
#define tr(i,x) for(typeof((x).begin()) i = x.begin(); i!=x.end(); ++i)
#define all(x) (x).begin(),(x).end()
#define vi vector<int>
using namespace std;

int bc(int x)
{
    if(x)
        return (x&1) + bc(x/2);
    return 0;
}

int brute(vector<pair<int,int> >& d)
{
    int k=d.size();
    int best=1000000;
    for(int mask=0;mask<(1<<k);mask++)
    {
        int high = 0;
        for(int i=0;i<k;i++)
        {
            if((mask&(1<<i)) == 0)
                continue;
            if(d[i].first > high+1)
                break;
            high = max(high,d[i].second);
//            cerr << high << ' ';
        }
        if(high < 10000)
            continue;
//        cout << high << ' ';
//        cout << mask << endl;
        best = min(best,bc(mask));
    }
    return best;
}

int pr(vector<pair<int,int> >& d)
{

    int tick = 0;
    int p = 0;
    int lim = 0;
//    cerr << endl;
    for(int i=0;i<d.size();)
    {
        if(d[i].first > p+1)
            return 1000000;
//        cerr << d[i].first << ' ';
//        cerr << '(' << p << ' ' << lim << ')';
        while(d[i].first <= p+1 && i<d.size())
        {
            lim = max(lim,d[i].second);
            i++;
        }
//        cerr << '(' << p << ' ' << lim << ')';
//        cerr << 't';
        tick++;
        p=lim;
        if(lim==10000)
            break;
    }
    if(lim < 10000)
    {
        return 1000000;
    }
//    cerr << endl;
//    cerr << lim << endl;
//    cerr << "unfail " << tick << ' ' << p << ' ' << lim << endl;
    
    return tick;

}

void tst()
{
    int n;
    cin >> n;

    map<string,vector<pair<int,int> > > data;
    string in;
    int a,b;
    for(int i=0;i<n;i++)
    {
        cin >> in >> a >> b;
        data[in].pb(mp(a,b));
    }
    vector<vector<pair<int,int> > > seg;
    tr(i,data)
        seg.pb(i->second);

    int best = 1000000;

    n = seg.size();
    for(int i=0;i<n;i++)
        for(int j=i;j<n;j++)
            for(int k=j;k<n;k++)
            {
                vector<pair<int,int> > d;
                tr(x,seg[i]) d.pb(*x);
                tr(x,seg[j]) d.pb(*x);
                tr(x,seg[k]) d.pb(*x);
                tr(i,d)
                    i->second *= -1;
                sort(all(d));
                tr(i,d)
                    i->second *= -1;
                best = min(best,pr(d));
/*                cerr << endl;
                cerr << pr(d) << ' ' << brute(d) << endl;
                if(pr(d) != brute(d))
                {
                    cerr << "fail\n";
                    tr(z,d)
                        cerr << z->first << ' ' << z->second << endl;
                    cerr << endl;
                }
                assert(pr(d) == brute(d));*/
            }
    if(best < 100000)
    cout << best;
    else
        cout << "IMPOSSIBLE";

}

int main()
{
    int n;
    cin >> n;
    for(int i=1;i<=n;i++)
    {
        cout << "Case #"<<i<<": ";tst();cout<<endl;
    }
}
