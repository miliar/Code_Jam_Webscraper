#include <iostream>
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
typedef long double Double;
typedef vector<long double> vd;

void solve(int num) {
    printf("Case #%d:\n", num);
    int N;
    cin >> N;
    vs S(N);
    for (int i = 0; i < N; ++i) {
        cin >> S[i];
    }
    vd A1(N), A2(N), A3(N);
    for (int i = 0; i < N; ++i) {
        int c1 = 0, c2 = 0;
        for (int j = 0; j < N; ++j) {
            if (S[i][j] == '1' || S[i][j] == '0') ++c2;
            if (S[i][j] == '1') ++c1;
        }
        A1[i] = (Double)c1 / c2; 
        //print(A1[i]);
    }
    for (int i = 0; i < N; ++i) {
        int cnt = 0;
        for (int k = 0; k < N; ++k) {
            if (S[k][i] == '.') continue;
            int c1 = 0, c2 = 0;
            for (int j = 0; j < N; ++j) {
                if (j == i) continue;
                if (S[k][j] == '1' || S[k][j] == '0') ++c2;
                if (S[k][j] == '1') ++c1;
            }
            A2[i] += (Double)c1 / c2;
            ++cnt;
        }
        A2[i] /= cnt;
        //print(A2[i]);
    }
    for (int i = 0; i < N; ++i) {
        int cnt = 0;
        for (int j = 0; j < N; ++j) {
            if (S[i][j] == '.') continue;
            A3[i] += A2[j];
            ++cnt;
        }
        A3[i] /= cnt;
        //print(A3[i]);
    }
    for (int i = 0; i < N; ++i) {
        double cur = 0.25 * A1[i] + 0.5 * A2[i] + 0.25 * A3[i];
        printf("%0.12lf\n", cur);
    }
}

int main() {
    int tst;
    cin >> tst;
    for (int i = 1; i <= tst; ++i) 
        solve(i);
    return 0;
}
