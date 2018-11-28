#include <iostream>
#include <sstream>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <algorithm>

using namespace std;
const int MAXN = 510;
const int MOD = 10000;
const string welcome = " welcome to code jam";
int dp[MAXN][MAXN];




int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    cin>>T;
    cin.ignore();
    for(int tc=1;tc<=T;tc++) {
        string word;
        getline(cin,word);

        memset(dp,-1,sizeof(dp));
        dp[0][0]=1;
        int n=word.size(),m=welcome.size()-1;
        word=" "+word;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++) {
                if(dp[i][j]==-1) continue;
                for(int k=i+1;k<=n;k++) {
                    if(word[k]==welcome[j+1]) {
                        if(dp[k][j+1]==-1) dp[k][j+1]=dp[i][j];
                        else dp[k][j+1]=(dp[k][j+1]+dp[i][j])%MOD;
                    }
                }
            }
        }
        int ret=0;
        for(int i=1;i<=n;i++) {
            if(dp[i][m]==-1) continue;
            ret=(ret+dp[i][m])%MOD;
        }
        cout<<"Case #"<<tc<<": ";
        ostringstream oss;oss<<ret;
        string str = oss.str();
        if(str.size()<4) {
            int size=str.size();
            for(int i=0;i<4-size;i++) str="0"+str;
            cout<<str<<endl;
        }
        else cout<<str<<endl;
    }
    return 0;
}
