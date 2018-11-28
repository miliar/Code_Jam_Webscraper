#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string code = "welcome to code jam";
string text;

const int MOD = 10000;

int dp[501][501];

int solve(int codepos, int textpos) {
    if (codepos == code.size()) {
        return 1;
    }
    if (textpos == text.size()) {
        return 0;
    }
    int &ret = dp[codepos][textpos];
    if (ret != -1) {
        return ret;
    }
    ret = solve(codepos, textpos + 1);
    if (code[codepos] == text[textpos]) {
        ret = (ret + solve(codepos + 1, textpos + 1)) % MOD;
    }
    return ret;
}

int main() {
    int cases;
    cin >> cases;
    getline(cin, text);
    for (int i = 1; i <= cases; i++) {
        getline(cin,text);
        memset(dp,-1,sizeof(dp));
        int ret = solve(0, 0);
        cout << "Case #" << i << ": ";
        if (ret < 1000) cout<<0;
        if (ret < 100) cout<<0;
        if (ret < 10) cout<<0;
        cout<<ret<<endl;
    }
}
