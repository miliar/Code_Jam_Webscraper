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

void solve() {
    int n;
    cin >> n;
    vector<int> p(n-1);
    for (int i = 0; i < n-1; ++i) {
        cin >> p[i];
        --p[i];
    }
    
    vector<int> h(n, 0);
    
    for (int attempt = 0; attempt < 100000; ++attempt) {
        bool ok = true;
        for (int i = 0; i < n - 1; ++i) {
            int maxp = i + 1;
            double maxa = (h[i+1] - h[i]);
            for (int j = i + 2; j < n; ++j) {
                double a = 1.0 * (h[j] - h[i]) / (j - i);
                if (maxa < a) {
                    maxa = a;
                    maxp = j;
                }
            }
            if (maxp != p[i]) {
                h[p[i]]++;
                ok = false;
                break;
            }
        }
        if (ok) {
            for (int i = 0; i < n; ++i)
                cout << " " << h[i];
            cout << endl;
            
            return;
        }
    }
    cout << " Impossible" << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cout << "Case #" << t + 1 << ":";
        solve();
    }
    return 0;
}
