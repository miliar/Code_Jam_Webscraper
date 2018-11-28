#include<fstream>

using namespace std;


int main(){
    
    ifstream cin("file.in");
    ofstream cout("file.out");
    
    int T; cin>>T;
    for(int t=1;t<=T;t++){
        
        int N; cin>>N;
        long long p[N+1], l[N];
        for(int i=0;i<N;i++){
            cin>>p[i]>>l[i];
        }
        
        
        long long dp[N+1];
        //long long D;
        cin>>p[N];
                
        memset(dp,-1,sizeof(dp));
        dp[N]=0; //need 0
        
        for(int i=N-1;i>=0;i--){
            int pos=i+1;
            while(pos<=N && p[i]+l[i]>=p[pos]){
                if(dp[pos]!=-1 && dp[pos]<=p[pos]-p[i]){
                    dp[i]=p[pos]-p[i];
                    break;
                }
                pos++;
            }
            //cout<<i<<' '<<dp[i];
        }
        
        cout<<"Case #"<<t<<": ";
        if(dp[0]>=0 && dp[0]<=p[0]) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
}

                    
                
