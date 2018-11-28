#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
#include <string>
#include <ctime>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <cstring>

#define pii pair <int, int>
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back

const int INF = 2147483647;
const double EPS = 1E-9;
const double PI = acos(-1);

using namespace std;

int main() {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, n, c, d;
    const int alphabet = 26;
    string s, tmp;
    bool D[alphabet][alphabet];
    int U[alphabet];
    char C[alphabet][alphabet];
    cin >> t;
    for(int q=1; q<=t; ++q) {
        memset(C, 0, sizeof(C)); memset(D, 0, sizeof(D)); memset(U, 0, sizeof(U));
        s = "";
        cin >> c;
        for(int i=0; i<c; ++i) {
            cin >> tmp;
            C[tmp[0] - 'A'][tmp[1] - 'A'] = tmp[2];
            C[tmp[1] - 'A'][tmp[0] - 'A'] = tmp[2];
        }
        cin >> d;
        for(int i=0; i<d; ++i) {
            cin >> tmp;
            D[tmp[0] - 'A'][tmp[1] - 'A'] = true;
            D[tmp[1] - 'A'][tmp[0] - 'A'] = true;
        }
        cin >> n >> tmp;
        for(int i=0; i<n; ++i)
            if(s.length() > 0 && C[tmp[i] - 'A'][s[s.length()-1] - 'A'] != 0) {
                U[s[s.length()-1] - 'A']--;
                s[s.length()-1] = C[tmp[i] - 'A'][s[s.length()-1] - 'A'];
                U[s[s.length()-1] - 'A']++;
            }
            else {
                bool check = false;
                for(int j=0; j<alphabet; ++j)
                    if(U[j]>0 && D[tmp[i] - 'A'][j]) {
                        s = "";
                        memset(U, 0, sizeof(U));
                        check = true;
                    }
                if(!check) {
                    s += tmp[i];
                    U[tmp[i] - 'A']++;
                }
            }
        cout << "Case #" << q << ": [";
        if(s.length() > 0) {
            for(size_t i=0; i<s.size()-1; ++i)
                cout << s[i] << ", ";
            cout << s[s.length()-1];
        }
        cout << "]" << endl;
    }

    return 0;
}
