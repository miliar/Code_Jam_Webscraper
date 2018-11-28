#include<iostream>
#include<fstream>
#include<vector>
#include<string>

using namespace std;

int main()
{

    ofstream fout("codejam.out");

    int N;
    cin>>N;
    
    string line;
    getline(cin,line);

    string ans = "welcome to code jam";

    for(int n = 1; n <= N; ++n){
        getline(cin,line);

        vector<int> dp(line.size(),0);

        for(int i = 0; i < dp.size(); ++i) if(line[i] == 'w') dp[i] = 1;

        for(int i = 1; i < ans.size(); ++i){
            int counter = 0;
            for(int k = 0; k < dp.size(); ++k){
                counter += dp[k];
                counter %= 10000;
                if(line[k] == ans[i]) dp[k] = counter;
                else dp[k] = 0;
            }
        }

        int ret = 0;
        for(int i = 0; i < dp.size(); ++i) ret = (ret + dp[i])%10000;
        
        fout<<"Case #"<<n<<": ";
        if(ret < 10) fout<<"0";
        if(ret < 100) fout<<"0";
        if(ret < 1000) fout<<"0";
        fout<<ret<<endl;
    }

    return 0;
}
