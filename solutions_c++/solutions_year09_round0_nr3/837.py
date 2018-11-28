#include <iostream>
#define mod 10000
using namespace std;
string a;
int N;
int dp[512][512];
string t = "welcome to code jam";
void solve(int q){
    for ( int i = 0; i < 512; ++i )
        for ( int j = 0; j < 512; ++j )
            dp[i][j] = 0;
    getline(cin, a);
    int sza = a.size();
    for ( int i = 0; i < a.size(); ++i )
        if ( a[i] == 'w' ) dp[i][0] = 1;
    for ( int i = 0; i < t.size() - 1; ++i ){
        int sum = 0;
        for ( int j = 0; j < a.size(); ++j ){
            sum %= mod;
            if ( a[j] == t[i] ) sum += dp[j][i];
            if ( a[j] == t[i + 1] ) dp[j][i + 1] += sum;
            dp[j][i + 1] %= mod;
        }
    }
    int ans = 0;
    for ( int i = 0; i < a.size(); ++i ){
        ans += dp[i][t.size() - 1];
        ans %= mod;
    }
    string qw = "";
    if ( ans < 10 ) qw += '0';
    if ( ans < 100 ) qw += '0';
    if ( ans < 1000 ) qw += '0';
    cout << "Case #" << q << ": " << qw << ans << endl;
}
int main(){
    cin >> N;
    getline(cin, a);
    for ( int i = 0; i < N; ++i ){
        solve(i + 1);
    }
}
