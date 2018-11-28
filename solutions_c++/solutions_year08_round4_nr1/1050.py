#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<map>
#include<queue>
#include<stack>
#include<cmath>
#include<iomanip>
#include<set>

using namespace std;

vector<bool> G;
vector<bool> C;
vector<bool> I;

int dp[1005][2];

/*void dfs(int a){
    if(a>=(M+1)/2) return;
    
   
}*/

int main(){
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);

    int N,M;
    int V,ax1,ax2;
    cin>>N;
    
    int X[1005][2];
    //int gr[1005];
    
    for(int caso=1;caso<=N;caso++){
        cin>>M>>V;
        //cout<<M<<" "<<V<<endl<<endl;
        G.clear(); C.clear();I.clear();
        
        for(int i=0;i<(M-1)/2;i++){
            cin>>ax1>>ax2;
            G.push_back(ax1); C.push_back(ax2);
        }
        
        for(int i=0;i<(M+1)/2;i++){            
            cin>>ax1;
            //cout<<i<<" "<<ax1<<endl;
            I.push_back(ax1);
        }
        //cout<<endl;
        //memset(gr,0,sizeof(gr));
        
        int cont=1;
        
        for(int i=1;cont<M;i++){
            for(int j=0;j<2 && cont<M;j++){
                cont++;
                X[i][j]=cont;
                //cout<<i<<" "<<cont<<endl;
            }
        }
        //cout<<endl;
        int a,b;
        
        memset(dp,-1,sizeof(dp));
        
        for(int i=(M+1)/2;i<=M;i++){
            dp[i][I[i-(M+1)/2]]=0;
            dp[i][1-I[i-(M+1)/2]]=-1;
        }
        
        /*for(int i=1;i<=(M-1)/2;i++){
            cout<<X[i][0]<<" "<<X[i][1]<<endl;
        }*/
        
        for(int i=(M-1)/2;i>=1;i--){            
            //if(gr[i]==2){
                
                ax1=X[i][0]; ax2=X[i][1];
                //cout<<i<<" "<<ax1<<" "<<ax2<<endl;
                
                if(dp[ax1][0]!=-1 && dp[ax2][0]!=-1){
                    if(G[i-1]==1){
                         if(dp[i][0]==-1) dp[i][0]=dp[ax1][0]+dp[ax2][0];
                         else dp[i][0]=min(dp[i][0],dp[ax1][0]+dp[ax2][0]);
                    }else{
                        if(dp[i][0]==-1) dp[i][0]=dp[ax1][0]+dp[ax2][0];
                        else dp[i][0]=min(dp[i][0],dp[ax1][0]+dp[ax2][0]);
                    }
                }
                
                if(dp[ax1][0]!=-1 && dp[ax2][1]!=-1){
                    //cout<<"entra:";
                    if(G[i-1]==1){
                        //cout<<"and"<<endl;
                         if(dp[i][0]==-1) dp[i][0]=dp[ax1][0]+dp[ax2][1];
                         else dp[i][0]=min(dp[i][0],dp[ax1][0]+dp[ax2][1]);
                         
                         if(C[i-1]==1){
                            if(dp[i][1]==-1) dp[i][1]=1+dp[ax1][0]+dp[ax2][1];
                            else dp[i][1]=1+min(dp[i][1],dp[ax1][0]+dp[ax2][1]);
                        }
                    }else{
                        //cout<<"or"<<endl;
                        if(dp[i][1]==-1) dp[i][1]=dp[ax1][0]+dp[ax2][1];
                        else dp[i][1]=min(dp[i][1],dp[ax1][0]+dp[ax2][1]);
                        
                        if(C[i-1]==1){
                            if(dp[i][0]==-1) dp[i][0]=1+dp[ax1][0]+dp[ax2][1];
                            else dp[i][0]=1+min(dp[i][0],dp[ax1][0]+dp[ax2][1]);
                        }
                    }
                }
                
                if(dp[ax1][1]!=-1 && dp[ax2][0]!=-1){
                    if(G[i-1]==1){
                         if(dp[i][0]==-1) dp[i][0]=dp[ax1][1]+dp[ax2][0];
                         else dp[i][0]=min(dp[i][0],dp[ax1][1]+dp[ax2][0]);
                         
                         if(C[i-1]==1){
                            if(dp[i][1]==-1) dp[i][1]=1+dp[ax1][1]+dp[ax2][0];
                            else dp[i][1]=1+min(dp[i][1],dp[ax1][1]+dp[ax2][0]);
                        }
                    }else{
                        if(dp[i][1]==-1) dp[i][1]=dp[ax1][1]+dp[ax2][0];
                        else dp[i][1]=min(dp[i][1],dp[ax1][1]+dp[ax2][0]);
                        
                        if(C[i-1]==1){
                            if(dp[i][0]==-1) dp[i][0]=1+dp[ax1][1]+dp[ax2][0];
                            else dp[i][0]=1+min(dp[i][0],dp[ax1][1]+dp[ax2][0]);
                        }
                    }
                }
                
                if(dp[ax1][1]!=-1 && dp[ax2][1]!=-1){
                    if(G[i-1]==1){
                         if(dp[i][1]==-1) dp[i][1]=dp[ax1][1]+dp[ax2][1];
                         else dp[i][1]=min(dp[i][1],dp[ax1][1]+dp[ax2][1]);
                    }else{
                        if(dp[i][1]==-1) dp[i][1]=dp[ax1][1]+dp[ax2][1];
                        else dp[i][1]=min(dp[i][1],dp[ax1][1]+dp[ax2][1]);
                    }
                }
            //}
        }
        
        /*for(int i=M;i>=1;i--){
            cout<<"i : "<<i<<endl;
            cout<<"0 : "<<dp[i][0]<<"  1: "<<dp[i][1]<<endl;
            cout<<endl;
        }*/
        
        //cout<<V<<endl;
        
        cout<<"Case #"<<caso<<": ";
        if(dp[1][V]==-1) cout<<"IMPOSSIBLE"<<endl;
        else cout<<dp[1][V]<<endl;
    }

    return 0;
}
