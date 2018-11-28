#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

//#define mp make_pair
#define pb push_back
#define ll long long
//#define mp make_pair

const int maxn = 20000, maxm = 121, maxp = 21;
string s[maxn], a[maxm];
map <string, bool> mp;

int main() {
    int v = 0, i, t, n, m, h;
    cin >> t;
    string tmp, rtmp;
    map <string, bool>::iterator iter;
    bool good;
    for (int it = 1; it <= t; ++it) {
        cin >> n >> m;
        for (int i = 0; i < n; ++i)
            cin >> s[i];
        cout << "Case #" << it << ": ";
        for (int k = 0; k < m; ++k) {
            cin >> a[k];
            mp.clear();
            for (int i = 0; i < n; ++i) {
                tmp = "";
                for (int j = 0; j < s[i].size(); ++j) 
                    tmp += "_";
                tmp += a[k][0];
                for (int j = 0; j < a[k].size(); ++j) {
                    tmp[s[i].size()] = a[k][j];
                    //rtmp = tmp;
                    //if (mp.find(tmp) == mp.end()) mp[tmp] = 0;
                    good = 0;
                    for (int l = 0; l < s[i].size(); ++l) 
                        if (s[i][l] == a[k][j]) {
                            if (!good) mp[tmp] = good;
                            tmp[l] = s[i][l], good = 1;
                        }
                }
            }
            int maxf = 0, now, best = 0, last, ok = 0;
            for (int i = 0; i < n; ++i) {
                now = 0;
                tmp = "";
                for (int j = 0; j < s[i].size(); ++j)
                    tmp += "_";
                tmp += a[k][0];
                //cout << tmp << endl;
                last = 0;
                ok = 0;
                while (ok != s[i].size()) {
                    tmp[s[i].size()] = a[k][last];
                    //if (last < 8) cout << tmp << endl;
                    good = 0;
                    if (mp.find(tmp) != mp.end()) {
                        for (int j = 0; j < s[i].size(); ++j)
                            if (s[i][j] == a[k][last]) good = 1, tmp[j] = s[i][j], ++ok;
                        if (!good) ++now;
                    }
                    ++last;
                    //cout << tmp << endl;
                    
                }
                if (maxf < now) maxf = now, best = i;
            }   
            cout << s[best] << " ";
        }
        cout << endl;
    }
}
