#include<iostream>
#include<vector>
using namespace std;

int M = 1000000007;

int main(){
        int tc;
        cin>>tc;
        for(int t=1;t<=tc;t++){
                int n,m;
                long long int X,Y,Z;
                cin>>n>>m>>X>>Y>>Z;
                long long int A[500001];
                for(int i=0;i<m;i++) cin>>A[i];
                long long int S[500001];
                for(int i=0;i<n;i++){
                        S[i]=A[i%m];
                        A[i%m]=(X*A[i%m]+Y*(i+1))%Z;
                }
                long long int DP[500001];
                for(int i=0;i<n;i++) DP[i]=0;
                for(int i=0;i<n;i++){
                        DP[i]=1;
                        for(int j=0;j<i;j++){
                                if(S[j]<S[i]) DP[i] = (DP[i]+DP[j])%M;
                        }
                }
                unsigned long long int ret=0;
                for(int i=0;i<n;i++){
                        ret= (ret+DP[i])%M;
                }
                cout<<"Case #"<<t<<": "<<ret<<endl;

        }
        return 0;
}


