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
inline void setmax(int &a, int b) { if(a < b) a=b; }

vector<int> primes;

void init(void)
{
    primes.pb(2);
    for(int i=3;i<=1000000;i+=2)
    {
        bool fail=false;
        for(int j=0;j<size(primes);j++)
        {
            if(primes[j] * primes[j] > i) break;
            if((i % primes[j]) == 0) { fail=true; break; }
        }
        if(!fail) primes.pb(i);
    }
    cerr << size(primes) << endl;
}

map<int,int> facto;

void process(void)
{
    LL n;
    scanf("%lld",&n);
    if(n == 1)
    {
        cout << 0 << endl;
        return;
    }
    LL tmax, tmin;
    facto.clear();

    LL ret = 1;

    for(int i=0;i<size(primes);i++)
    {
        if(n < primes[i]) break;
        LL tmp = n;
        int cnt = 0;
        for(cnt=0;tmp>=primes[i];cnt++, tmp/=primes[i]);
        if(cnt)
        {
            //cout << cnt << endl;
            ret += cnt - 1;
        }
    }

    cout << ret << endl;
    return;

    tmax = 1;
    foreach(it, facto)
    {
        tmax += it->second;
    }

    tmin = 0;
    foreach(it, facto)
    {
        tmin++;
    }
    if(tmin == 0) tmin++;

    cout << tmax - tmin << endl;
}

int main(void)
{
    init();
    int T;
    cin >> T;
    for(int i=0;i<T;i++)
    {
        cout << "Case #" << i+1 << ": ";
        process();
    }
	return 0;
}

