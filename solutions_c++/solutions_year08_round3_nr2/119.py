#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main(){
        int tc;
        cin>>tc;
        for(int t = 1;t<=tc;t++){
                string s;
                cin>>s;
                int l = s.size();
                long long int DP[41][210];
                for(int i=0;i<40;i++)
                        for(int j=0;j<210;j++){
                                DP[i][j]=0;
                        }
                DP[0][0]=1;
                for(int i=1;i<=l;i++){
                        for(int j=0;j<i;j++){
                                int val=0;
                                for(int k=j;k<i;k++){
                                        val = (val*10+s[k]-'0')%210;
                                }
                                for(int k=0;k<210;k++){
                                        DP[i][(k+val)%210]+=DP[j][k];
                                        if(j==0) continue;
                                        DP[i][(k+210-val)%210]+=DP[j][k];
                                }
                        }
                }
                long long int ret=0;
                for(int k=0;k<210;k++){
                        if(k%2==0 ||k %3==0 ||k %5 ==0 ||k%7==0) {
                                ret+=DP[l][k];
                        }
                }
                cout<<"Case "<<t<<": "<<ret<<endl;
        }
        return 0;
}

