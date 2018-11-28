#include<iostream>
using namespace std;

int P,N,T,S,arr[105];
int dp[150][159];


int sol(int ind,int tak)
{
 if(tak>S)return -(1<<22);  
 if(ind == N)return 0;
 int ans = -(1<<22);
 
 if(dp[ind][tak]!=-1)return dp[ind][tak];
 
 if(arr[ind]%3==0)ans = max(ans,sol(ind+1,tak)+((arr[ind]/3>=P)?1:0));  
 if((arr[ind]+1)%3==0&&((arr[ind]+1)/3)-1>=0)ans = max(ans,sol(ind+1,tak)+(((arr[ind]+1)/3>=P)?1:0));  
 if((arr[ind]+2)%3==0&&((arr[ind]+2)/3)-1>=0)ans = max(ans,sol(ind+1,tak)+(((arr[ind]+2)/3>=P)?1:0));
 if((arr[ind]+2)%3==0&&((arr[ind]+2)/3)-2>=0)ans = max(ans,sol(ind+1,tak+1)+(((arr[ind]+2)/3>=P)?1:0));  
 if((arr[ind]+3)%3==0&&((arr[ind]+3)/3)-2>=0)ans = max(ans,sol(ind+1,tak+1)+(((arr[ind]+3)/3>=P)?1:0));  
 if((arr[ind]+4)%3==0&&((arr[ind]+4)/3)-2>=0)ans = max(ans,sol(ind+1,tak+1)+(((arr[ind]+4)/3>=P)?1:0));  

    
 return dp[ind][tak] = ans;   
}



int main()
{
    
    freopen("B-large.in","r",stdin);
    freopen("tt.out","w",stdout);
    cin>>T;
    for(int cas = 1 ;cas<=T; ++cas){
            memset(dp,-1,sizeof dp);
            cin>>N>>S>>P;
            int i;
            for(i=0;i<N;++i)cin>>arr[i];
            cout<<"Case #"<<cas<<": "<<sol(0,0)<<endl;        
            
            
    }
    
    
    
    return 0;    
}
