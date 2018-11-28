#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;
//dp normaleta

string s;
const int MOD = 10000;
int memo[1000][25];
int n;
string pat="welcome to code jam";
const int m = 19;

int rec(int i, int j) { //amb s[0..i] quants cops puc formar pat[0...j]
    if (i<0 or i>=n) return 0;
    int &ans=memo[i][j];
    if (ans>=0) return ans;
    if (j==0 and s[i]==pat[j]) return ans=(1+rec(i-1,j))%MOD;
    if (s[i]==pat[j]) {
        return ans=(rec(i-1,j-1)+rec(i-1,j))%MOD;
    }
    else return ans=(rec(i-1,j)%MOD);
}

int main() {
    int t; cin >> t;
    getline(cin,s); //endline
    for (int z=1;z<=t;++z) {
        cout << "Case #"<<z<<": ";
        getline(cin,s);
        n=s.size();
        for (int i=0;i<n;++i) for (int j=0;j<25;++j) memo[i][j]=-1;
        int ans=rec(n-1,m-1);
        if (ans<1000) cout << 0;
        if (ans<100) cout << 0;
        if (ans<10) cout << 0;
        cout << ans << endl;
    }
}
