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
#define BIT(x) (1LL<<(x))

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef long long LL;
typedef complex<double> Point;

template<typename T> inline int size(const T &a) { return a.size(); }
template<typename T> inline bool operator<(const int &a,const vector<T> &b) { return a<b.size(); }

void process(void)
{
    int x,s,r,t,n;
    scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
    map<int,int> M;
    M.clear();
    M[0] = x;
    for(int i=0;i<n;i++)
    {
        int a,b,c;
        scanf("%d %d %d",&a,&b,&c);
        M[0] -= b-a;
        M[c] += b-a;
    }

    double tot = 0;
    double tt = t;

    foreach(it, M)
    {
        double maxdist = tt * (r + it->first);
        if(maxdist > it->second)
        {
            double elasp = (double)(it->second) / (r + it->first);
            tot += elasp;
            tt -= elasp;
        }
        else
        {
            double dist = tt * (r + it->first);
            tot += tt;
            tt = 0;
            double elasp = ((double)(it->second) - dist) / (s + it->first);
            tot += elasp;
        }
    }

    printf("%.12lf\n", tot);
}

int main(void)
{
    int T;
    cin >> T;
    for(int i=0;i<T;i++)
    {
        cout << "Case #" << i+1 << ": ";
        process();
    }
	return 0;
}

