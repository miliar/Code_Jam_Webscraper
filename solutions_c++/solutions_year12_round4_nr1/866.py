#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define PB push_back
#define MP make_pair
#define ll long long

inline int toInt(string s){int v;istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x){ostringstream sout;sout<<x;return sout.str();}

vector<int> ds;
vector<int> ls;
map<pair<int,int>, bool > m;
int dmax[10001];
int g,n;
bool solve(int pos, int len){
    if(ds[pos] + len >= g) return true;
    if(m.find(MP(pos,len)) != m.end()){
        return m[MP(pos,len)];
    }
    bool res = false;
    for(int i=pos+1;i<n;i++){
        if(ds[i] > ds[pos] + len) break;
        if(dmax[i] > min(ds[i] - ds[pos], ls[i])) continue;
        dmax[i] = min(ds[i]-ds[pos],ls[i]);
        res |= solve(i, min(ds[i] - ds[pos], ls[i]));
    }
    return m[MP(pos,len)] = res;
}

int main(){
    int x;
    cin >> x;
    for(int t=1;t<=x;t++){
        memset(dmax,-1,sizeof(dmax));
        int d,l;
        cin >> n;
        for(int i=0;i<n;i++){
            cin >> d >> l;
            ds.PB(d);
            ls.PB(l);
        }
        cin >> g;

        printf("Case #%d: %s\n", t, solve(0,ds[0])?"YES":"NO");
        ds.clear();
        ls.clear();
        m.clear();
    }
}
