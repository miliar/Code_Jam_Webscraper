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
typedef long long ll;

int path[1005][1005];
int valid[1005][1005];
#define M 10007

int main(){
    int test;
    scanf("%d",&test);
    for(int t=0;t<test;t++){
        printf("Case #%d: ",t+1);
        memset(path,0,sizeof(path));
        memset(valid,-1,sizeof(valid));
        int r,c,inv;
        scanf("%d %d %d",&r,&c,&inv);
        for(int i=0;i<inv;i++){
            int rr,cc;
            scanf("%d %d",&rr,&cc);
            valid[rr-1][cc-1]=0;
        }
        path[0][0]=1;
        for(int i=0;i<r;i++)
            for(int j=0;j<c;j++){
                int ny=i+2;
                int nx=j+1;
                if(valid[ny][nx])
                   path[ny][nx]=(path[ny][nx]+path[i][j])%M;
                ny=i+1;
                nx=j+2;
                if(valid[ny][nx])
                    path[ny][nx]=(path[ny][nx]+path[i][j])%M;
            }
        printf("%d\n",path[r-1][c-1]);
        
    }
}
