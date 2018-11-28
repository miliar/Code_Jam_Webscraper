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

bool process(void)
{
    LL n,d,g;
    LL dd,gg,ddd;
    cin >> n >> d >> g; ddd = d;
    d = __gcd(100LL,d); dd = 100 / d;

    if(dd > n)
    {
        cout << "Broken" << endl;
        return true;
    }

    if((ddd != 100 && g == 100) || (ddd != 0 && g == 0))
    {
        cout << "Broken" << endl;
        return true;
    }

    cout << "Possible" << endl;

	return true;
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

