#include <iostream>
#include <string>
using namespace std;
const string p = "!welcome to code jam";
int dp[50];
int main(){
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int n;
    cin >> n;
    string s;
    getline(cin,s);
    for(int i = 1;i <= n;++i){
        getline(cin,s);
        memset(dp,0,sizeof(dp));
        dp[0] = 1;
        for(int j = 0;j < s.size();++j)
            for(int k = 1;k < p.size();++k)
                if(s[j] == p[k])
                    dp[k] = (dp[k-1] + dp[k]) % 10000;
        cout << "Case #" << i << ": ";
        if(dp[p.size()-1] < 1000) cout << 0;
        if(dp[p.size()-1] < 100) cout << 0;
        if(dp[p.size()-1] < 10) cout << 0;
        cout << dp[p.size()-1] << endl;
    }
}
