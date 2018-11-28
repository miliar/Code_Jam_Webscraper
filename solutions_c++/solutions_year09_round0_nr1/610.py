#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
using namespace std;
typedef long long ent;
typedef set<int> SI;
typedef vector<SI> VS;

int main() {
    int r,d,n; //mida, paraules_diccio, tests
    int cas=1;
    cin >> r >> d >> n;
        vector<string> v(d);
        for (int i=0;i<d;++i) cin >> v[i];
        vector<vector<bool> > T(r,vector<bool>(26,false));
        string s;
        int p=0; //token id
        int lloc=0;
        for (int z=0;z<n;++z) {
            lloc=0;
            p=0;
            cin >> s;
            for (int j=0;j<r;++j) for (int k=0;k<26;++k) T[j][k]=false;
            for (int j=0;j<s.size();++j) {
                if (s[j]=='(') ++lloc;
                else if (s[j]==')') --lloc;
                if (s[j]==')') ++p;
                else if (s[j]!='(') {
                    T[p][s[j]-'a']=1;
                    if (lloc==0) ++p;
                }
            }
            int ans=0;
            for (int i=0;i<d;++i) {
                bool ok=true;
                for (int j=0;ok and j<r;++j) 
                    if (not T[j][v[i][j]-'a']) ok=false;
                if (ok) ++ans;
            }
            cout << "Case #"<<cas++<<": " << ans << endl;
        }

}
