#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector <int> VI;
typedef vector <double> VD;
typedef vector <vector<int > > VVI;
typedef pair <int,int> PII;
typedef vector <LL> VL;
typedef vector <string> VS;

VS split(string s, string t=" ") {
    VS ret;
    int a,b=0;
    while ((a=s.find_first_not_of(t,b))!=-1) {
        b=s.find_first_of(t,a);
        ret.push_back(s.substr(a,b-a));
    }
    return ret;
}

const int inf = 1000000000;

int main()
{
    int _nn;
    scanf("%d\n", &_nn);
    for (int tr=0; tr<_nn; tr++) {
        int n,m;
        scanf("%d\n", &n);
        scanf("%d\n", &m);
        vector<vector<pair<int, int> > > v(m);
        for (int p=0; p<m; p++) {
            string line;
            getline(cin,line);
            VS vec = split(line);
            for (int i=1; i<vec.size(); i+=2) {
                v[p].push_back(make_pair(atoi(vec[i].c_str())-1,atoi(vec[i+1].c_str())));
            }
        }

        VI ret;

        for (int i=0; i<(1<<n); i++) {
            bool ok1 = true;
            for (int j=0; j<m; j++) {
                bool ok = false;
                for (int k=0; k<v[j].size(); k++) {
                    if (((i >> v[j][k].first)&1) == v[j][k].second ) {
                        ok = true;
                        break;
                    }
                }
                if (!ok) {
                    ok1 = false;
                    break;
                }
            }
            if (ok1) {
                ret.push_back(i);
            }
        }
        if (ret.size() == 0) {
            printf("Case #%d: IMPOSSIBLE\n", tr+1);
        } else {
            int cnt = inf;
            int best = 0;
            for (int i=0; i<ret.size(); i++) {
                if (cnt > __builtin_popcount(ret[i])) {
                    cnt = __builtin_popcount(ret[i]);
                    best = ret[i];
                }
            }
            printf("Case #%d:", tr+1);
            for (int i=0; i<n; i++) {
                printf(" %d", (best>>i)&1);
            }
            printf("\n");
        }
    }
    return 0;
}

