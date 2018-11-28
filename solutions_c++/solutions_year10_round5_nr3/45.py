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

map<int,int> mm;

void process(void)
{
    int n;
    scanf("%d",&n);
    mm.clear();
    for(int i=0;i<n;i++)
    {
        int a,b;
        scanf("%d %d",&a,&b);
        mm[a] += b;
    }

    int cnt = 0;
redo:
    foreach(it, mm)
    {
        if(it->second >= 2)
        {
            cnt++;
            mm[it->first -1]++;
            mm[it->first +1]++;
            it->second -= 2;
            goto redo;
        }
    }

    cout << cnt << endl;
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
	return 0;
}

