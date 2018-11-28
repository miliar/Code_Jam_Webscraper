#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <sstream>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <iomanip>

using namespace std;



typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<string> VS;

const int inf = (1<<30) - 1;
const int nil = -inf;

#define ABS(a) ((a)>0?(a):(-a))

const double eps = 1e-4;

vector<string> parse(string s) {
    for(int i=0; i<s.size(); i++)
        if (s[i]=='/')
            s[i] = ' ';
    string a;
    stringstream ss(s);
    string t;
    VS res;
    while(ss >> t) {
        a += "/"+t;
        res.push_back(a);
    }
    return res;
}

void solve(int T) {
    int m, n;
    set<string> a;
    cin >> m >> n;
    for(int i=0; i<m; i++) {
        string s;
        cin >> s;
        VS u = parse(s);
        for(int i=0; i<u.size(); i++)
            a.insert(u[i]);
    }
    int count = 0;
    for(int i=0; i<n; i++) {
        string s;
        cin >> s;
        VS u = parse(s);
        for(int i=0; i<u.size(); i++) {
            if (a.find(u[i])==a.end()) {
                count++;
                a.insert(u[i]);
            }
        }
    }
    cout << "Case #" << T+1 << ": " << count << endl;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin.sync_with_stdio(false);
    int n;
    cin >> n;
    for(int i=0; i<n; i++) {
        solve(i);
    }

    return 0;
}
