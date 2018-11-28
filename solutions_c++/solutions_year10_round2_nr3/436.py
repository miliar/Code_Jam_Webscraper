#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

#define MOD 100003

#define MAX_N 500

int cnt_memo[MAX_N][MAX_N];
int comb[MAX_N+1][MAX_N+1];


int count(int n,int k){
    int res=0;
    if(cnt_memo[n][k]>=0){
        return cnt_memo[n][k];
    }
    if(k==1){
        return 1;
    }
    for(int i=1;i<=k-1;i++){
        res+=(count(k,i)*comb[n-k-1][k-i-1])%MOD;
        res%=MOD;
    }
    cnt_memo[n][k]=res;
    return res;
}

int main(){

    for(int i=0;i<=MAX_N;i++){
        comb[i][0]=1;
        comb[i][i]=1;
        for(int j=1;j<i;j++){
            comb[i][j]=(comb[i-1][j-1]+comb[i-1][j])%MOD;
        }
    }

    int tcases;
    cin>>tcases;

    for(int tcase=1;tcase<=tcases;tcase++){

        cout<<"Case #"<<tcase<<": ";

        int n;
        cin>>n;

        memset(cnt_memo,-1,sizeof(cnt_memo));

        int cnt=0;
        for(int k=1;k<=n-1;k++){
            cnt+=count(n,k);
            cnt%=MOD;
        }
        cout<<cnt<<endl;
    }


    return 0;
}
