#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

map<string, int> mymap;

int calc(const vector<string> &v, int n, const string d)
{
    int i, j, N;
    int f[100][26];
    int done[100];
    int rest;
    bool flg;
    int ret = 0;

    if (v.size() == 1) {
        return 0;
    }

    N = v.size();

    memset(done, 0, sizeof(done));
    
    memset(f, 0, sizeof(f));
    for(i=0;i<N;i++) {
        for(j=0;j<v[i].size();j++) {
            f[i][v[i][j]-'a'] |= (1 << j);
        }
    }

    rest = N;
    for(i=0;i<26;i++) {
        flg = false;
        for(j=0;j<N;j++) {
            if (!done[j] && f[j][d[i]-'a']) {
                flg = true;
                break;
            }
        }
        if (!flg)
            continue;
        if (!f[n][d[i]-'a']) {
            ret--;
        }
        for(j=0;j<N;j++) {
            if (!done[j] && (f[j][d[i]-'a'] != f[n][d[i]-'a'])) {
                done[j] = 1;
                rest--;
            }
        }
        if (rest == 1)
            return ret;
    }

}

int
main(void)
{
    int i, j, k, ret, m;
    int N, M;
    int tc, TC;
    string s;
    string vd[10000];
    int    cnt[10000];
    vector<string> v;
    int    vf[10000];
    string vl[100];
    string dict;

    cin >> TC;

    for(tc=1;tc<=TC;tc++) {
        cin >> N >> M;
        for(i=0;i<N;i++) {
            cin >> vd[i];
        }
        cout << "Case #" << tc << ":";
        for(k=0;k<M;k++) {
            cin >> dict;
            mymap.clear();
            for(i=1;i<=10;i++) {
//                 cout << "len=" << i << endl;
                v.clear();
                for(j=0;j<N;j++) {
                    if (vd[j].size() == i) {
                        v.push_back(vd[j]);
                    }
                }
//                 for(j=0;j<v.size();j++) {
//                     cout << v[j] << " ";
//                 }
//                 cout << endl;
                for(j=0;j<v.size();j++) {
                    ret = calc(v, j, dict);
//                     cout << v[j] << "=" << ret << endl;
                    mymap[v[j]] = ret;
                }
            }
            int mymin = 1;
            int ii;
            for(i=0;i<N;i++) {
                if (mymap[vd[i]] < mymin) {
                    mymin = mymap[vd[i]];
                    ii = i;
                }
            }
            cout << " " << vd[ii];
        }
        cout << endl;
    }
    
    return 0;
}
