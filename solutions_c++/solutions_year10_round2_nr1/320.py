#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <utility>
#include <string>
#include <sstream>
#include <complex>
#include <bitset>
#include <numeric>
#include <valarray>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <cstdlib>
using namespace std;
#define rep(i,n) for(int i = 0;i < (int)(n); i++)
#define all(a) (a).begin(),(a).end()
#define foreach(i,c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

const int inf = 987654321;

string parent(string &s) {
    string ret;
    int num = 0, cnt = 0;
    rep(i,s.size()) if (s[i] == '/') ++num;
    rep(i,s.size()) {
        if (s[i] == '/') ++cnt;
        if (cnt == num) break;
        ret += s[i];
    }
    return ret;
}

int main() {
    int T;
    cin >> T;
    rep(I,T) {
        int n, m;
        cin >> n >> m;
        int cnt = 0;
        map<string,pair<string,bool > > dir;
        rep(i,n) {
            string name;
            cin >> name;
            dir[name] = make_pair(parent(name), true);
        }
        rep(i,m) {
            string name;
            cin >> name;
            if (dir.find(name) == dir.end()) {
                dir[name] = make_pair(parent(name), true);
                ++cnt;
                while (true) {
                    name = parent(name);
                    if (name == "" || dir.find(name) != dir.end()) break;
                    dir[name] = make_pair(parent(name), true);
                    ++cnt;
                }
            }
        }
        cout << "Case #" << I+1 << ": " << cnt << endl;
    }
    return 0;
}
