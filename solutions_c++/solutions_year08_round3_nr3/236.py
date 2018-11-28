#include<iostream>
#include<vector>
#include<memory.h>
using namespace std;
int n;
long long dp[1010][1010];
vector<long long> v,a;

long long fun(int ind,int last){
     if(ind == n && last!= 1002) return 1;
     if(ind == n) return 0;
     
     if(dp[ind][last] != -1) return dp[ind][last];
     long long r1=0,r2=0;
     if(last== 1002 || v[ind] > v[last])
               r1 = fun(ind+1,ind);
     r2 = fun(ind+1,last);
     
     return dp[ind][last] = ((r1%1000000007)+(r2%1000000007))%1000000007;
}

int main(){
    freopen("test.in","rt",stdin);
    freopen("test.out","w",stdout);
//    cout<<"Hello World"<<endl;
    long long N,m,x,y,z,X;
    cin>>N;
    for(int tt=0;tt<N;tt++){
            cin>>n>>m>>x>>y>>z;
            for(int i=0;i<m;i++){
                    cin>>X;
                    a.push_back(X);
            }
            for(int i=0;i<n;i++){
                    v.push_back(a[i%m]);
                    a[i%m] = (x * a[i % m] + y * (i + 1)) % z;
                    //cout<<v[i]<<endl;
            }
            cout<<"Case #"<<tt+1<<": ";
            memset(dp,-1,sizeof(dp));
            
            cout<<fun(0,1002)<<endl;
            
            v.clear();
            a.clear();
    }
    return 0;
}   
