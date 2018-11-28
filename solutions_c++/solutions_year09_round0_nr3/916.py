#include <iostream>
#include <string>

using namespace std;

const int MOD = 10000;

const string wcj = "welcome to code jam";

int dp[128 * 1024][21];
int was[128 * 1024][21];
string input;
int Time;

int calc(int p1, int p2){    
    if (was[p1][p2] == Time)
        return dp[p1][p2];    
    if (p1 == 0 && p2 == 0){        
        return 1;
    }
    if (p2 == 0){
        return 1;
    }
    if (p1 == 0){
        return 0;
    }
    dp[p1][p2] = (calc(p1 - 1, p2) + calc(p1 - 1, p2 - 1) * (input[p1 - 1] == wcj[p2 - 1])) % MOD;
    was[p1][p2] = Time;
    return dp[p1][p2];
}

int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    freopen("test.err","w",stderr);

    int n;
    cin >> n;
    getline(cin,input);
    for (int i = 0; i < n; i++){        
        input = "";
        getline(cin,input);                
        cerr << input.size() << '\n';
        ++Time;
        printf("Case #%d: %04d\n",Time,calc(input.size(),wcj.size()));
    }

    return 0;
}