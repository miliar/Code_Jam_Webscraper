#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

#define x first
#define y second
#define rep(i,n) for(int i=0; i<int(n); i++)

using namespace std;

typedef vector<int> vi;
typedef vector<vi>  vvi;
typedef pair<int,int> pii;
typedef long long ll;

int main() {
    int __N; cin >> __N;
    for (int Nc = 1; Nc <= __N; Nc++) {
        int k;
        int mini = 500000;
        string s, t;
        cin >> k >> s;
        t = s;
        vi v(k);
        rep(i,k) v[i]=i;
        do {
            rep (i, t.size()) {
                t[i] = s[(i/k)*k + v[i%k]];
            }
            int cnt = 1;
            char ante=t[0];
            for (int i = 1; i < t.size(); i++) {
                if (t[i] != ante) {
                   cnt++;
                   ante = t[i];         
                }
            }
            mini = min(cnt, mini);
        }while(next_permutation(v.begin(),v.end()));
        cout << "Case #" << Nc << ": " << mini << endl;
    }
}
