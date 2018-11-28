#include<iostream>
#include<cstring>
#include<vector>
typedef long long ll;
const ll MAXN = 505;
const ll MOD = 100003;


ll memo[MAXN][MAXN];
ll pascal_memo[505][505];
ll npr(ll n,ll r){
    if(n<0 || r<0 ||r>n)return 0;
    if(n<=0 || r<=0)return 1;
    if(r>=n)return 1;
    if(pascal_memo[n][r]!=0)
        return pascal_memo[n][r];
    ll c = npr(n-1,r-1)+npr(n-1,r-0);
    c%=MOD;
    pascal_memo[n][r]=c;
    return c;
}

ll rec(ll n,ll k){
    if(k==1)return 1;
    //if(k==n-1)return 1;
    if(memo[n][k]!=-1)return memo[n][k];
    ll total = 0;
    for(ll i=1;i<k;i++){//i = kuinka monta lukua ennen k:ta
        ll t_low = rec(k,i);
        ll t_hi  = npr(n-k-1,k-i-1);
        total+=t_low*t_hi;
        total%=MOD;
    }
    //std::cout<<"rec("<<n<<","<<k<<")="<<total<<std::endl;
    memo[n][k]=total;
    return total;
}
int main(){

    memset(memo,-1,sizeof(memo));
    for(ll i=0;i<10;i++){
        for(ll j=0;j<10;j++){
 //           std::cout<<npr(i,j)<<" ";
        }
//        std::cout<<"\n";
    }
    int t;
    std::cin>>t;
    for(int j=0;j<t;j++){
        int n;
        std::cin>>n;
        ll total = 0;
        for(int i=1;i<n;i++){
            total+=rec(n,i);
            total%=MOD;
        }
        std::cout<<"Case #"<<(j+1)<<": "<<total<<std::endl;
    }
    
}
