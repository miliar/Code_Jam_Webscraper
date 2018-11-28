#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <map>
#include <cmath>

#define mp make_pair

using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int nt, n, testn;
    cin>>nt;
    int i, j;
    int c, d;
    char comb[128][128];
    vector<vector<char> > op;
    int u[128];
    vector<char> res;
    string s, t;
    char ch;
    for(testn=1; testn<=nt; ++testn) {
        res.clear();
        op.clear();
        op.resize(128);
        memset(comb, 0, sizeof(comb));
        memset(u, 0, sizeof(u));
        s = "";
        cin>>c;
        for(i=0; i<c; ++i) {
            cin>>t;
            comb[t[0]][t[1]] = t[2];
            comb[t[1]][t[0]] = t[2];
        }
        cin>>d;
        for(i=0; i<d; ++i) {
            cin>>t;
            op[t[0]].push_back(t[1]);
            op[t[1]].push_back(t[0]);
        }
        cin>>n;
        cin>>s;
        for(i=0; i<n; ++i) {
            if (res.empty()) {
                res.push_back(s[i]);
                u[s[i]]++;
                continue;
            }
            if ((ch = comb[res.back()][s[i]]) != 0) {
                u[res.back()]--;
                res.pop_back();
                res.push_back(ch);
                continue;
            }
            for(j=0; j<op[s[i]].size(); ++j) {
                if (u[op[s[i]][j]]) {
                    res.clear();
                    memset(u, 0, sizeof(u));
                    break;
                }
            }
            if (!res.empty()) {
                res.push_back(s[i]);
                u[s[i]]++;
            }
        }
        cout<<"Case #"<<testn<<": ";
        if (res.empty()) {
            cout<<"[]";
        } else {
            cout<<"["<<res[0];
            for(i=1; i<res.size(); ++i) {
                cout<<", "<<res[i];
            }
            cout<<"]";
        }
        cout<<endl;
    }
    return 0;
}
