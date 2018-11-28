#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
using namespace std;
typedef long long ll;

string f(string s) {
    string ans = "";
    for (int i = 1; i < int(s.size()); ++i ) ans += s[i];
    ans+=s[0];
    return ans;
}

int transf(string s) {
    int r = 0;
    for (int i = 0; i < int(s.size());++i) {
        r*=10;
        r+=s[i]-'0';
    }
    return r;
}

string tostring(int x){ 
    string ans="";
    if (x==0) return "0";
    while(x>0) {
        ans=char(x%10+'0')+ans;
        x/=10;
    }
    return ans;
}

bool valid(string s, int a, int b) {
    int c = transf(s);
    return (a<=c and c<=b);
}

const int M = 2000000+1;

int main() {
    int t; cin >> t;
    for (int cas = 1; cas <= t; ++cas) {
        int a, b; cin >> a >> b;
        ll ans=0;
        vector<int> usat(M,0), repus(M,0); //0 no usat, i usat quan c=i
        for (int c = a; c <= b; ++ c) {
            string s = tostring(c);
            int n = int(s.size());
            string rep=s;
            ll r = 1;

            usat[c] = c;
            for (int i=0;i<n-1;++i) {
                s=f(s);
                if (s[0]!='0' and valid(s,a,b)) {
                    rep=min(rep,s); //em quedo la menor com representant
                    int rr = transf(s);
                    if (usat[rr]!=c)  {
                        usat[rr]=c;
                        ++r;
                    }
                }
            }

            if (repus[transf(rep)]==0) {
                repus[transf(rep)]=c;
                ans+=r*(r-1)/2;
            }
        }
        cerr << "Case #" << cas << ": " << ans << endl;
        cout << "Case #" << cas << ": " << ans << endl;
    }
}
