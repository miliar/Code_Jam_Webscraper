#include <iostream>
#include <string.h>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>
using namespace std;
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz(x) ((int)((x).size()))
#define rep(i, N) for (int i = 0; i < N; ++i)
#define foreach(it,v) for(__typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define print(x) cerr<<#x<<" = ";pr(x);cerr<<endl;
#define PRC(l,r) pr(l);foreach(it,v)pr(it==v.begin()?"":","),pr(*it);pr(r);
template<class T>void pr(T x){cerr<<x;} 
template<class T>void pr(vector<T>v){PRC('[',']');} 
template<class T1,class T2>void pr(pair<T1,T2>x){pr(x.first);pr(':');pr(x.second);} 
template<class T>void pr(set<T>v){PRC('{','}');} 
template<class T1,class T2>void pr(map<T1,T2>v){PRC('{','}');}
typedef long long lint;
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
bool Op[256][256];
char Map[256][256];

void solveTestCase(int tst) {
    memset(Op, false, sizeof(Op));
    memset(Map, false, sizeof(Map));
    char s[10000];
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%s", s);
        Map[s[0]][s[1]] = s[2];
        Map[s[1]][s[0]] = s[2];
    }
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%s", s);
        Op[s[0]][s[1]] = true;
        Op[s[1]][s[0]] = true;
    }
    scanf("%d", &n);
    scanf("%s", s);
    vector<char> v;
    for (int i = 0; i < n; ++i) {
        char ch = s[i];
        if (v.empty()) {
            v.pb(ch);
            continue;
        }
        char pch = v.back();
        if (Map[pch][ch]) {
            v.pop_back();
            v.pb(Map[pch][ch]);
            continue;
        }
        bool fnd = false;
        for (int j = 0; j < sz(v); ++j) {
            pch = v[j];
            if (Op[pch][ch]) {
                v.clear();
                fnd = true;
                break;
            }
        }
        if (fnd) continue;
        v.pb(ch);
    }

    cout << "Case #" << tst << ": ";
    printf("[");
    for (int i = 0; i < sz(v); ++i) {
        if (i) printf(", ");
        printf("%c", v[i]);
    }
    printf("]\n");
}

int main() {
    int tst;
    cin >> tst;
    for (int i = 1; i <= tst; ++i)
        solveTestCase(i);
    return 0;
}
