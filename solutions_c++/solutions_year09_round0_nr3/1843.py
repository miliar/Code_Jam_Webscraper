#include <iostream>
#include <string>
using namespace std;
#define N 510
#define M 10000

const static string s = "welcome to code jam";
int ans[N][40];
int l;

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    string cmd;
    int T,index = 0;
    l = s.length();
    cin>>T;
    getline(cin,cmd);
    while (T--){
        getline(cin,cmd);
        memset(ans,0,sizeof(ans));
        //cout<<cmd<<endl;
        printf("Case #%d: ",++index);
        //cout<<cmd<<endl;
        for (int i=0 ;i<cmd.length(); ++i){
            for (int j=0 ;j<l && j<=i ;++j){
                if (cmd[i] != s[j]) continue;
                if (j == 0) ans[i][j] = 1;
                else{
                    for (int k=j-1 ;k<i ;++k) {
                        ans[i][j] += ans[k][j-1];
                        ans[i][j] %= M;
                    }    
                }    
            }    
        }   
        int cnt = 0;
        for (int i=l-1; i<cmd.length(); ++i) {
            cnt += ans[i][l-1];
            cnt %= M;
        }    
        if (cnt < 1000) printf("0");
        if (cnt < 100) printf("0");
        if (cnt < 10) printf("0");
        printf("%d\n",cnt);
    }        
    return 0;
}    
