#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>
#include <queue>
#include <fstream>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define tr(i, a) for (typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair
#define N 120
typedef long long ll;
char C[N][N];
char D[N][N];
string ans;
void solve(char u){
    if(ans.length() == 0)
        ans += u;
    else{
        int n = ans.length();
        char v = ans[n - 1];
        if(C[u][v]){
            ans[n - 1] = C[u][v];
        }else{
            ans += u;
            //! n++
        }
        forn(i, n)
            if(D[ans[i]][ans[ans.length() - 1]]){
                ans = "";
                break;
            }
    }
}
string out(){
    string res = "[";
    forn(i, ans.length()){
        res += ans[i];
        if(i + 1 != ans.length())
            res += ", ";
    }
    return res + "]";
}
int main() {
    int T;
    cin >> T;
    forn(_t, T){
        ans = "";
        zero(C);
        zero(D);
        int c, d, n;
        cin >> c;
        forn(i, c){
            string s;
            cin >> s;
            C[s[0]][s[1]] = C[s[1]][s[0]] = s[2];
        }
        cin >> d;
        forn(i, d){
            string s;
            cin >> s;
            D[s[0]][s[1]] = D[s[1]][s[0]] = 1;
        }
        cin >> n;
        string s;
        cin >> s;
        forn(i, n)
            solve(s[i]);
        cout << "Case #" << _t + 1 << ": " << out() << endl;
    }
    return 0;
}
