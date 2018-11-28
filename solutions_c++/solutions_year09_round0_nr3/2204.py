#include <stdio.h>
#include <iostream>
#include <string>

#define MOD 10000
using namespace std;

int n;

void solve()
{
    int dp[32];
    memset(dp,0,sizeof(dp));
    string s;
    getline(cin,s);
    if(s[0]=='w') dp[0]=1;
    for(int i=1;i<s.size();i++)
    {
        if(s[i]=='w') dp[0]=(dp[0]+1)%MOD;
        if(s[i]=='e') dp[1]=(dp[1]+dp[0])%MOD;
        if(s[i]=='l') dp[2]=(dp[2]+dp[1])%MOD;
        if(s[i]=='c') dp[3]=(dp[3]+dp[2])%MOD;
        if(s[i]=='o') dp[4]=(dp[4]+dp[3])%MOD;
        if(s[i]=='m') dp[5]=(dp[5]+dp[4])%MOD;
        if(s[i]=='e') dp[6]=(dp[6]+dp[5])%MOD;
        if(s[i]==' ') dp[7]=(dp[7]+dp[6])%MOD;
        if(s[i]=='t') dp[8]=(dp[8]+dp[7])%MOD;
        if(s[i]=='o') dp[9]=(dp[9]+dp[8])%MOD;
        if(s[i]==' ') dp[10]=(dp[10]+dp[9])%MOD;
        if(s[i]=='c') dp[11]=(dp[11]+dp[10])%MOD;
        if(s[i]=='o') dp[12]=(dp[12]+dp[11])%MOD;
        if(s[i]=='d') dp[13]=(dp[13]+dp[12])%MOD;
        if(s[i]=='e') dp[14]=(dp[14]+dp[13])%MOD;
        if(s[i]==' ') dp[15]=(dp[15]+dp[14])%MOD;
        if(s[i]=='j') dp[16]=(dp[16]+dp[15])%MOD;
        if(s[i]=='a') dp[17]=(dp[17]+dp[16])%MOD;
        if(s[i]=='m') dp[18]=(dp[18]+dp[17])%MOD;
    }
    cout << dp[18]/1000 << dp[18]/100%10 << dp[18]/10%10 << dp[18]%10 << endl;
}

int main()
{
    cin >> n;
    cin.get();
    for(int i=1;i<=n;i++)
    {
        cout << "Case #" << i << ": ";
        solve();
    }
    
    return 0;
}
