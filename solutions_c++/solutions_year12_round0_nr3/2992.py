#include <iostream>
#include <set>
#include <sstream>

using namespace std;
typedef long long ll;

set<int> memo;
stringstream ss;
int getcnt(int n, int mn, int mx){
    ss.clear();
    ss << n;
    string s, t;
    ss >> s;
    t = s;
    int c = 0;
    int k;
    do{
        ss.clear();
        t = t.substr(1) + t[0];
        ss << t;
        ss >> k;
        if(mn <= k && k <= mx){
            ++c;
            memo.insert(k);
        }
    }while(t != s);
    return c;
}
void solve(){
    memo.clear();
    int a,b;
    ll res = 0;
    cin >> a >> b;
    for(int i=a; i<=b; ++i){
        if(!memo.count(i)){
            int c = getcnt(i, a, b);
            res += (ll)c * (c - 1) / 2;
        }
    }
    cout << res << endl;
}
int main(){
    int T;
    cin >> T;
    for(int cas=1; cas<=T; ++cas){
        cout << "Case #" << cas << ": ";
        solve();
    }
    return 0;
}


