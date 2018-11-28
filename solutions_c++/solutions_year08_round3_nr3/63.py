#include<iostream>
using namespace std;

long long N,T,M,X,Y,Z;

long long A[500001],L[500001];

int memo[500001];

int MOD=1000000007;
int main(){
    int Case=1;
    cin>>T;
    while(T--){
        cin>>N>>M>>X>>Y>>Z;
        for(int i=0;i<M;i++){
                cin>>A[i];
        }
        for(int i=0;i<N;i++){
                L[i]=A[i%M];
                A[i%M]=((X*A[i%M])%Z + Y*(i+1))%Z;                
        }
        for(int i=0;i<N;i++){
                memo[i]=1;
                for(int j=0;j<i;j++){
                       if(L[i]>L[j]){
                                     memo[i]+=memo[j];
                                     memo[i]%=MOD;
                       }
                }
        }
        long long res=0;
        for(int i=0;i<N;i++) { res= (res+memo[i])%MOD;
        }
        cout<<"Case #"<<Case<<": "<<res<<endl;
        Case++;
    }
    system("pause");
}
