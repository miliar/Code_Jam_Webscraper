#include <string> 
#include <vector> 
#include <map> 
#include <utility> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <queue> 
#include <stack> 
#include <set> 
#include <sstream> 
#include <algorithm> 
#include <iostream> 
#include <iomanip> 
using namespace std;
  
#define INF 0x3f3f3f3f
#define ALL(v) v.begin(),v.end() 
typedef pair<int,int> pii; 

#define AND 1
#define OR 0

struct node{
    int interior;
    int change;
    int type;
    int val;
}tree[1000000];

int dp[100005][2];

int solve(int x,int des){
    int left,right;
    if(dp[x][des]==-1){
        dp[x][des]=INF;
        if(tree[x].interior){
            dp[x][des]=INF;
            if(tree[x].type==AND){
                if(des==1){
                    left=solve(2*x,1);
                    right=solve(2*x+1,1);
                    if(left!=INF&&right!=INF) dp[x][des]<?=(left+right);                    
                }else{
                    left=solve(2*x,0);
                    right=solve(2*x+1,0);
                    if(left!=INF&&right!=INF) dp[x][des]<?=(left+right);      

                    left=solve(2*x,0);
                    right=solve(2*x+1,1);
                    if(left!=INF&&right!=INF) dp[x][des]<?=(left+right);      

                    left=solve(2*x,1);
                    right=solve(2*x+1,0);
                    if(left!=INF&&right!=INF) dp[x][des]<?=(left+right);                          
                }
            }else{
                if(des==1){
                    left=solve(2*x,0);
                    right=solve(2*x+1,1);
                    if(left!=INF&&right!=INF) dp[x][des]<?=(left+right);      

                    left=solve(2*x,1);
                    right=solve(2*x+1,0);
                    if(left!=INF&&right!=INF) dp[x][des]<?=(left+right);                          

                    left=solve(2*x,1);
                    right=solve(2*x+1,1);
                    if(left!=INF&&right!=INF) dp[x][des]<?=(left+right);                          
                }else{
                    left=solve(2*x,0);
                    right=solve(2*x+1,0);
                    if(left!=INF&&right!=INF) dp[x][des]<?=(left+right);                          
                }
            }
            
            if(tree[x].change){
                 if(tree[x].type==AND){
                    if(des==1){
                        left=solve(2*x,0);
                        right=solve(2*x+1,1);
                        if(left!=INF&&right!=INF) dp[x][des]<?=(left+right+1);      

                        left=solve(2*x,1);
                        right=solve(2*x+1,0);
                        if(left!=INF&&right!=INF) dp[x][des]<?=(left+right+1);                          
    
                        left=solve(2*x,1);
                        right=solve(2*x+1,1);
                        if(left!=INF&&right!=INF) dp[x][des]<?=(left+right+1);                          
                    }else{
                        left=solve(2*x,0);
                        right=solve(2*x+1,0);
                        if(left!=INF&&right!=INF) dp[x][des]<?=(left+right+1);                          
                    }
                }else{
                    if(des==1){
                        left=solve(2*x,1);
                        right=solve(2*x+1,1);
                        if(left!=INF&&right!=INF) dp[x][des]<?=(left+right+1);                    
                    }else{
                        left=solve(2*x,0);
                        right=solve(2*x+1,0);
                        if(left!=INF&&right!=INF) dp[x][des]<?=(left+right+1);      

                        left=solve(2*x,0);
                        right=solve(2*x+1,1);
                        if(left!=INF&&right!=INF) dp[x][des]<?=(left+right+1);      

                        left=solve(2*x,1);
                        right=solve(2*x+1,0);
                        if(left!=INF&&right!=INF) dp[x][des]<?=(left+right+1);                          
                    }
                }
            }
        } else{
            if(tree[x].val==des) dp[x][des]=0;
            else dp[x][des]=INF;
        }
    }
    return dp[x][des];
}

int main(){
    int test;
    scanf("%d",&test);
    for(int t=0;t<test;t++){
        printf("Case #%d: ",t+1);
        
        int m,v;
        scanf("%d %d",&m,&v);
        //cout<<m<<' '<<v<<endl;
        for(int i=0;i<(m-1)/2;i++){
            scanf("%d %d",&tree[i+1].type,&tree[i+1].change);
            tree[i+1].interior=1;
        }
        
        for(int i=(m-1)/2;i<m;i++){
            scanf("%d",&tree[i+1].val);
            tree[i+1].interior=0;
        }
        memset(dp,-1,sizeof(dp));
        int res=solve(1,v);
        if(res==INF) printf("IMPOSSIBLE\n");
        else printf("%d\n",res);
    }
}
