#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>

#define foreach(i,v) for(typeof(v.end())i=v.begin();i!=v.end();++i) 

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef long long ll;

using namespace std;


struct PV
{
    int p;
    ll v;
    PV(int p, int v) : p(p), v(v) { }
};

int D;
vector<PV> pv;

bool isok(double t)
{
    double curLeft = pv[0].p - t;
    double lastPos;
    foreach(it, pv) {
        curLeft = max(curLeft, it->p - t);
        lastPos = curLeft + D * (it->v - 1);
        curLeft += D * it->v;
        if (it->p + t < lastPos)
            return false;
    }
    return true;
}

double solve() 
{
    double mn = 0.0, mx = 1e20;
    double mid;
    while (mx - mn > 1e-7) {
        mid = (mn + mx) / 2;
        if (isok(mid))
            mx = mid;
        else
            mn = mid;
    }
    return (mn + mx) / 2;
}

int main(int argc, const char* argv[])
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int C;
        cin >> C >> D;
        pv.clear();
        for (int j = 0; j < C; j++) {
            int p, v;
            cin >> p >> v;
            pv.push_back(PV(p,v));
        }
        cout << "Case #" << (i+1) << ": " << solve() << endl;
    } 
    return 0;
}
