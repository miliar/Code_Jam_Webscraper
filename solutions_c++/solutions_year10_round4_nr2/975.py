#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
int ntest;
struct match{
    int p;
    vector<int> vt;
    bool operator < (const match &s) const{
        return p!=s.p? p>s.p : vt.size()<s.vt.size();
    }
}f[1<<11];
int p;
int m[1<<10];
int n;
void init(int node){
    f[node].vt.clear();
    if(node>= n ){            
        f[node].p=1;
        f[node].vt.push_back( node% n );                
        return ;
    }        
    f[node].p=1;
    init(node*2);
    init(node*2+1);   
    for(int i=0; i< f[node*2].vt.size(); i++){   
        f[node].vt.push_back(f[node*2].vt[i]);
        f[node].vt.push_back(f[node*2+1].vt[i]);
    }    
}
int main(){
    freopen("B-small.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    for(int test=0; test<ntest; test++){
        printf("Case #%d: ",test+1);  
        scanf("%d",&p);
        n = (1<<p);
        for(int i=0; i< n ; i++){
            scanf("%d",&m[i]);           
        }             
        init(1);
        int x;
        int res=0;
        for(int i=p-1; i>-1; i--)
            for(int j= (1<<i); j< (1<<(i+1)); j++){                
                scanf("%d",&f[j].p);                
                res+= f[j].p;
            }                    
        sort(f+1,f+n);            
        bool vis[n];
        memset(vis,false, sizeof vis);
        //while(true){
            for(int i=1; i<n; i++)
                if(!vis[i]){                    
                    int j;                    
                    for(j=0; j<f[i].vt.size(); j++){                        
                        if( !m[f[i].vt[j]] ) break; 
                    }                                       
                    if(j==f[i].vt.size()){                                                
                        for(j=0; j<f[i].vt.size(); j++)
                            m[f[i].vt[j]] --; 
                        vis[i]=true;                        
                        res-= f[i].p;                        
                    }
                }        
        printf("%d\n",res);
    }
    return 0;
}
