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
bool adj[102][102],b[102][102];
int n;
int solve(){
    int st=0;
    while(true){        
        st++;        
        for(int i=1; i<=100;i++)
            for(int j=1; j<=100; j++)
                if(adj[i-1][j] && adj[i][j-1])
                    b[i][j]=true;
                else if (!adj[i-1][j] && !adj[i][j-1])
                    b[i][j]=false;
                else
                    b[i][j]=adj[i][j];
        int i,j;
        for(i=1; i<=100;i++)
            for(j=1; j<=100; j++)
                if(b[i][j]) goto x;
        x:{
            if(i==101 && j==101) break;
        }
        for(i=1; i<=100;i++)
            for(j=1; j<=100; j++)
                adj[i][j]=b[i][j];
    }
    return st;
}
int main(){
    freopen("C-small.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    int x,y,z,t;
    for(int test=0; test<ntest; test++){
        memset(adj,false,sizeof adj);
         memset(b,false,sizeof b);
        printf("Case #%d: ",test+1);  
        scanf("%d",&n);
        for(int i=0; i<n; i++){
            scanf("%d %d %d %d",&x,&y,&z,&t);
            for(int i=x; i<=z; i++)
                for(int j=y; j<=t; j++){                   
                    b[i][j]=adj[i][j]=true;            
                }
        }
        printf("%d\n",solve());
    }
    return 0;
}
