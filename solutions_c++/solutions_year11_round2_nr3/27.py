#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <bitset>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>

using namespace std;

#include <ext/numeric>
#include <ext/functional>
using namespace __gnu_cxx;

ostringstream message;
template<typename T>
void assert(bool t, const T& ign);
void parse_arguments(int argc, char* argv[], int& case_begin, int& case_end);

int n, m;
vector<pair<int, int> > a[2001];
int find(vector<pair<int, int> >& a, int target) {
    pair<int, int> x;
    x.first = target;
    x.second = 10*n;
    int r = lower_bound(a.begin(), a.end(), x) - a.begin();
    if (r == 0) return -1;
    return a[r-1].second;
}
int W[2001][2001];
int d[2001][2001];
int go(int u, int v) {
    if (W[u][v]) return d[u][v];
    W[u][v] = 1;
    int target = (v < u) ? v+n : v;
    int nodes = 1;
    int x = u;
    int res = n;
    while (x != v) {
        int z = find(a[x], (v < x ? v+n:v) - (x == u));
        if (z == -1) {x++; if (x==n) x=0;}
        else {
            res = min(res, go(x, z));
            x = z;
        }
        nodes++;
    }
    res = min(res, nodes);
    d[u][v] = res;
    return res;
}

int C[2001];
int w[2001];

void fill(int u, int v, int cu, int cv, int cc) {
    if (W[u][v]==2) return;
    W[u][v] = 2;
    int target = (v < u) ? v+n : v;
    int x = u;

    int h = cu+1; if (h==cc+1) h=1;
    if (h==cv) {h++; if (h==cc+1) h=1;}
    while (x != v) {
        int z = find(a[x], (v < x ? v+n:v) - (x == u));
        if (z == -1) {x++; if (x==n) x=0; 
            if (x != v) {
                C[x] = h;
                h++; if (h==cc+1) h=1;
                if (h==cv) {h++; if (h==cc+1) h=1;}
            }
        }
        else {
            if (z != v) {
                C[z] = h;
                h++; if (h==cc+1) h=1;
                if (h==cv) {h++; if (h==cc+1) h=1;}
            }
            fill(x, z, C[x], C[z], cc);
            x = z;
        }
    }
}

void process(int cur_case, bool solve_case){
    cin >> n >> m;
    for (int i = 0; i < n; ++i) a[i].clear();
    vector<int> u, v;
    
    for (int i = 0; i < m; ++i) {
        int x; cin >> x; u.push_back(x-1);
    }
    for (int i = 0; i < m; ++i) {
        int x; cin >> x; v.push_back(x-1);
    }
    for (int i = 0; i < m; ++i) {
        a[u[i]].push_back(make_pair(v[i] < u[i] ? v[i]+n:v[i], v[i]));
        a[v[i]].push_back(make_pair(u[i] < v[i] ? u[i]+n:u[i], u[i]));
    }

    if (solve_case) {
        cerr << "case " << cur_case << endl;
        for (int i = 0; i < n; ++i)
            sort(a[i].begin(), a[i].end());
        memset(W, 0, sizeof(W));

        int r = min(go(v[0], u[0]), go(u[0], v[0]));
        memset(C, 0, sizeof(C));
        memset(w, 0, sizeof(w));
        if (r == 2) {
            int k = 0;
            for (int i = 0; i < n; ++i)
                if (a[i].size() > a[k].size()) k = i;
            queue<int> q;
            q.push(k);
            C[k] = 1;
            w[k] = 1;
            while(!q.empty()) {
                cerr << k << endl;
                int k = q.front(); q.pop();
                for (int i = 0; i < a[k].size(); ++i) {
                    int j = a[k][i].second;
                    if (!C[j]) {C[j] = 2-C[k]; if (!w[j]){w[j] = 1; q.push(j);}}
                }
                int j = (k+1) % n;
                if (!C[j]) {C[j] = 2-C[k]; if (!w[j]){w[j] = 1; q.push(j);}}
                j = (k+n-1) % n;
                if (!C[j]) {C[j] = 2-C[k]; if (!w[j]){w[j] = 1; q.push(j);}}
            }
        } else {
            C[v[0]] = 1;
            C[u[0]] = 2;
            fill(v[0], u[0], 1, 2, r);
            fill(u[0], v[0], 2, 1, r);
        }

        cout << "Case #" << cur_case << ": " << r << endl;
        cout << C[0];
        for (int i = 1; i < n; ++i)
            cout << " " << C[i];
        cout << endl;
    }
}

void test() {

}

int main(int argc, char* argv[]) {
    int case_begin = 1;
    int case_end = 2000000000;
    parse_arguments(argc, argv, case_begin, case_end);
    int cases;
    cin >> cases;
    assert(case_begin <= cases, message << "empty test case range");
    cerr << "Solving cases [" << case_begin << ".." 
                              << min(case_end, cases+1) << ")" << endl;
    for (int cur_case = 1; cur_case <= cases; ++ cur_case) {
        process(cur_case, case_begin <= cur_case && cur_case < case_end);
    }
    return 0;
}

void parse_arguments(int argc, char* argv[], int& case_begin, int& case_end) {
    if (argc == 2 && string("test") == string(argv[1])) {
        test();
        exit(0);
    }
    else if (argc == 2) {
        sscanf(argv[1], "%d", &case_begin);
        case_end = case_begin + 1;
    } else if (argc == 3) {
        sscanf(argv[1], "%d", &case_begin);
        sscanf(argv[2], "%d", &case_end);
        assert(case_begin < case_end, 
               message << "invalid test case range: " 
                       << case_begin << " " 
                       << case_end << endl);
    } else if (argc > 1) {
        cerr << "invalid arguments " << endl;
        exit(1);
    }
}

template<typename T>
void assert(bool t, const T& ign) {
    if (!t) {
        cerr << "bug: "<< message.str() << endl;
        exit(1);
    }
    message.clear();
}