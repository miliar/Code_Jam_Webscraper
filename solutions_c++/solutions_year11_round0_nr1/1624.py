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
typedef pair<char,int> pci; 
typedef pair<pair<int,int>,int> piii;

int d[105][105][105];

int da[9]={-1,-1,-1,0,0,0,1,1,1};
int db[9]={-1,0,1,-1,0,1,-1,0,1};

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d: ",tt);
        
        int n;
        scanf("%d",&n);
        
        vector<pci> vs;
        pci temp;
        for(int i=0;i<n;i++){
            cin>>temp.first;
            scanf("%d",&temp.second);
            vs.push_back(temp);
        }
        
        
        piii s,x;
        s.first.first=1; s.first.second=1; s.second=0;
        
        queue<piii> q;
        q.push(s);
        memset(d,-1,sizeof(d));
        d[1][1][0]=0;
        
        while(!q.empty()){
            x=q.front(); q.pop();
            
            if(x.second==n) {printf("%d",d[x.first.first][x.first.second][n]); break;}
            piii nx;
            
            for(int i=0;i<9;i++){
                nx.first.first=x.first.first+da[i]; nx.first.second=x.first.second+db[i];
                nx.second=x.second;
                if(nx.first.first>=1&&nx.first.first<=100&&
                   nx.first.second>=1&&nx.first.second<=100&&
                   d[nx.first.first][nx.first.second][nx.second]==-1){
                    d[nx.first.first][nx.first.second][nx.second]=d[x.first.first][x.first.second][x.second]+1;
                    q.push(nx);
                }
            }
            
            
            if(vs[x.second].first=='O'&&x.first.first==vs[x.second].second){
                nx=x;
                nx.second++;
                for(int i=0;i<9;i++){
                    nx.first.second=x.first.second+db[i];
                    if(nx.first.first>=1&&nx.first.first<=100&&
                        nx.first.second>=1&&nx.first.second<=100&&
                        d[nx.first.first][nx.first.second][nx.second]==-1){
                        d[nx.first.first][nx.first.second][nx.second]=d[x.first.first][x.first.second][x.second]+1;
                        q.push(nx);
                    }
                }
            }
            
            if(vs[x.second].first=='B'&&x.first.second==vs[x.second].second){
                nx=x;
                nx.second++;
                for(int i=0;i<9;i++){
                    nx.first.first=x.first.first+da[i];
                    if(nx.first.first>=1&&nx.first.first<=100&&
                        nx.first.second>=1&&nx.first.second<=100&&
                        d[nx.first.first][nx.first.second][nx.second]==-1){
                        d[nx.first.first][nx.first.second][nx.second]=d[x.first.first][x.first.second][x.second]+1;
                        q.push(nx);
                    }
                }         
            }
            
        }
        
        printf("\n");
    }

    return 0;
}
