#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <complex>

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,long long> PII;
typedef long long LL;
typedef complex<double> Point;

template<typename T> inline int size(const T &a) { return a.size(); }
template<typename T> inline bool operator<(const int &a,const vector<T> &b) { return a<b.size(); }

vector<vector<PII> > array1,array2;

void matchup(const vector<PII> &a, const vector<PII> &b, int cost, vector<PII> &res)
{
    map<int,LL> r1;
    for(int i=0;i<size(a);i++)
    {
        for(int j=0;j<size(b);j++)
        {
            LL tmp = a[i].second + b[j].second + cost;
            int t1 = min(a[i].first, b[j].first);

            if(r1.find(t1) == r1.end() || r1[t1] > tmp)
                r1[t1] = tmp;

            if(t1 > 0)
            {
                if(r1.find(t1-1) == r1.end() || r1[t1-1] > tmp-cost)
                {
                    r1[t1-1] = tmp-cost;
                }
            }
        }
    }

    foreach(it,r1)
    {
        res.pb(mp(it->first,it->second));
    }
}

void process(void)
{
    int p;
    scanf("%d",&p);
    int sz = (1<<p);

    array1.clear();
    array1.resize(sz);
    for(int i=0;i<sz;i++)
    {
        int tmp;
        scanf("%d",&tmp);
        array1[i].pb(mp(tmp,0));
    }

    for(int i=0;i<p;i++)
    {
        array2.clear();
        array2.resize(sz/2);
        for(int j=0;j<sz;j+=2)
        {
            int cost;
            scanf("%d",&cost);
            vector<PII> &a = array1[j], &b = array1[j+1];

            matchup(a,b,cost,array2[j/2]);
        }

        sz/=2;
        array1.swap(array2);
    }
    LL mincost = array1[0][0].second;
    for(int i=0;i<array1[0].size();i++)
    {
        if(mincost > array1[0][i].second)
            mincost = array1[0][i].second;
    }
    cout << mincost << endl;
}

int main(void)
{
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        process();
    }
}

