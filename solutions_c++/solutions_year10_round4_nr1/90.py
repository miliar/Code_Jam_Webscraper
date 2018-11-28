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
typedef pair<int,int> PII;
typedef long long LL;
typedef complex<double> Point;

template<typename T> inline int size(const T &a) { return a.size(); }
template<typename T> inline bool operator<(const int &a,const vector<T> &b) { return a<b.size(); }

int n;
int mm[55][55];

bool check(int x,int y,int val)
{
    if(x < 0 || y < 0 || x >= n || y >= n) return false;
    return mm[x][y] != val;
}

bool validate(int sz,int xx,int yy)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            int px = i + xx;
            int py = j + yy;

            if(check(py - xx,px - yy,mm[i][j])) return false;
            if(check(sz-1-px - xx, sz-1-py - yy, mm[i][j])) return false;
            if(check(sz-1-py - xx, sz-1-px - yy, mm[i][j])) return false;
        }
    }
    return true;
}

void process(void)
{
    scanf("%d",&n);
    vector<vector<PII> > order(n*2-1);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            order[i+j].pb(mp(i,j));
        }
    }
    memset(mm,0,sizeof(mm));

    for(int i=0;i<size(order);i++)
    {
        for(int j=0;j<size(order[i]);j++)
        {
            int tmp;
            scanf("%d",&tmp);
            mm[order[i][j].first][order[i][j].second] = tmp;
        }
    }

    for(int i=n;;i++)
    {
        int diff = i-n;
        for(int j=0;j<=diff;j++)
        {
            for(int k=0;k<=diff;k++)
            {
                if(validate(i,j,k))
                {
                    cout << (long long)i*i - n*n << endl;
                    return;
                }
            }
        }
    }
}

int main(void)
{
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        process();
        cerr << i << endl;
    }
}

