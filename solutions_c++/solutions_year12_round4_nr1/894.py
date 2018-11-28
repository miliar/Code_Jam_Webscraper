#include <iostream>
#include <string>
#include <fstream>
#include <limits>
#include <list>
#include <stack>
#include <numeric>
#include <queue>
#include <algorithm>
#include <functional>
#include <stack>
#include <bitset>
#include <map>
#include <list>
#include <math.h>
#include <set>
#include <stdio.h>
#include <ctype.h>
#include <vector>
#include <sstream>

#define vvvvi(T) vector<vector<vector<vector<T> > > >
#define vvvi(T) vector<vector<vector<T> > >
#define vvi(T) vector<vector<T> >

using namespace std;

string getLine(istream& stream) {
    string res;
    getline(stream, res);
    return res;
}

vector<string> getLineFields(istream& stream) {
    string line = getLine(stream);
    stringstream str;
    str << line;
    vector<string> fields;
    string temp;
    while(str>>temp)
    {
        fields.push_back(temp);
    }
    return fields;
}

template <typename T>
T str2type(string a) {
    stringstream t;
    t << a;
    T b;
    t >> b;
    return b;
}

bool solve1(const vector< pair<long long, long long> >& v, int i, long long r, long long d) {
    if (v[i].first + r >= d) return true;
    for (int j = i + 1; j < v.size(); ++j) {
        if (v[j].first > v[i].first + r) break;
        if (solve1(v, j, min(v[j].second, v[j].first - v[i].first), d))
            return true;
    }
    return false;
}

void solve() {
    int n;
    cin >> n;
    vector< pair<long long, long long> > v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i].first >> v[i].second;
    }
    long long d;
    cin >> d;
    
    if (solve1(v, 0, v[0].first, d)) {
        cout << "YES" << endl;
    }
    else
        cout << "NO" << endl;
    return;
    
    long long curr = v[0].first;
    int curi = 0;
    if (v[curi].first + curr >= d) {
        cout << "YES" << endl;
        return;
    }
    
    
    while(true) {
        long long maxd = v[curi].first + curr;
        long long maxr = -1;
        int maxi = -1;
        for (int i = curi + 1; i < n; ++i) {
            if (v[i].first > v[curi].first + curr) {
                break;
            }
            long long r = min(v[i].first - v[curi].first, v[i].second);
            if (maxd < v[i].first + r) {
                maxd = v[i].first + r;
                maxr = r;
                maxi = i;
            }
        }
        if (d <= maxd) {
            cout << "YES" << endl;
            return;
        }
        if (maxi == -1) {
            cout << "NO" << endl;
            return;
        }
        curi = maxi;
        curr = maxr;
    }
}

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cout << "Case #" << t + 1 << ": ";
        solve();
    }
    return 0;
}
