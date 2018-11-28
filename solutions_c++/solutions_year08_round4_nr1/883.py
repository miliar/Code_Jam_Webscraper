#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

#define left(x) (2*x)
#define right(x) (2*x+1)
#define parent(x) (x/2)

int M,V;
int G[50001],C[50001];
int value[50001];

int interior;

int memo[50001][3];
int seen[50001][3];

#define INF 10001

int kase=1;

bool isInterior(int n){
     return n<=M/2;
}


int solve(int node,int v){
    if(node<=M&&!isInterior(node)) return (value[node]==v)?0:INF;
    int &ret=memo[node][v];
    if(seen[node][v]==kase) return ret;
    seen[node][v]=kase;
    ret=INF;
    if(isInterior(node)){
        if(G[node]&&v){
           ret<?=solve(left(node),1)+solve(right(node),1);
        }
        else if(G[node]&&!v){
             ret<?=solve(left(node),1)+solve(right(node),0);
             ret<?=solve(left(node),0)+solve(right(node),0);
             ret<?=solve(left(node),0)+solve(right(node),1);
        }
        else if(!G[node]&&v){
             ret<?=solve(left(node),1)+solve(right(node),0);
             ret<?=solve(left(node),1)+solve(right(node),1);
             ret<?=solve(left(node),0)+solve(right(node),1);
        }
        else if(!G[node]&&!v){
             ret<?=solve(left(node),0)+solve(right(node),0);
        }
        
        if(C[node]){
            if(!G[node]&&v){
               ret<?=solve(left(node),1)+solve(right(node),1)+1;
            }
            else if(!G[node]&&!v){
                 ret<?=solve(left(node),1)+solve(right(node),0)+1;
                 ret<?=solve(left(node),0)+solve(right(node),0)+1;
                 ret<?=solve(left(node),0)+solve(right(node),1)+1;
            }
            else if(G[node]&&v){
                 ret<?=solve(left(node),1)+solve(right(node),0)+1;
                 ret<?=solve(left(node),1)+solve(right(node),1)+1;
                 ret<?=solve(left(node),0)+solve(right(node),1)+1;
            }
            else if(G[node]&&!v){
                 ret<?=solve(left(node),0)+solve(right(node),0)+1;
            }
        }
    }
    return ret;
}

int main(){
    int test;
    cin>>test;
    while(test--){
        cin>>M>>V;
        memset(memo,-1,sizeof(memo));
        interior=M/2;
        for(int i=1;i<=interior;i++) cin>>G[i]>>C[i];
        for(int i=interior+1;i<=M;i++) cin>>value[i];
        int result=solve(1,V);
        if(result<INF)
        cout<<"Case #"<<kase++<<": "<<result<<endl;
        else cout<<"Case #"<<kase++<<": IMPOSSIBLE"<<endl;
        
    }
    return 0;
    
}
