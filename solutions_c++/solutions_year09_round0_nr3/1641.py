
#include <iostream>
#include <iomanip>
using namespace std;

int cnt[5000][19];
const char *text = "welcome to code jam";

void solve()
{
    int t;
    cin>>t;
    string s;
    getline(cin,s);

    int case_cnt = 0;

    while(t--){
        memset(cnt,0,sizeof(cnt)); 
        getline(cin,s);
        int len = s.size();

        if(s[0]=='w'){
            cnt[0][0]++;
        }

        for(int i=1;i<s.size();++i){
            cnt[i][0]=cnt[i-1][0];
            if(s[i]=='w'){
               cnt[i][0]+=1;
               cnt[i][0]%=10000;
            }

            for(int j=1;j<19;++j){
                cnt[i][j]=cnt[i-1][j];
                if(s[i]==text[j]){
                    cnt[i][j]+=cnt[i-1][j-1];
                    cnt[i][j]%=10000;
                }
            }
        }

        cout<<"Case #"<<++case_cnt<<": "<<setw(4)<<setfill('0')<<cnt[s.size()-1][18]<<endl;
    }
}


int main()
{
    solve();
}


