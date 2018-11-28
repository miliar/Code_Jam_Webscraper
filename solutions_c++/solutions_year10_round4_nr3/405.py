#include <vector> 
#include <list> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

#define ME(s) memset((s), 0, sizeof((s)))
#define MM(s,a) memset((s),(a),sizeof((s)))
#define MCP(s,a) memcpy((s), (a), sizeof(s))
#define LLD long long
#define PII pair<int, int>
#define mkp(a,b) make_pair((a),(b))
#define x first
#define y second
#define FOR(i,n) for (int (i)=0;(i)<(n);++(i))

int map[2][120][120];
int t,T;
void init(){
        int n,x1,y1,x2,y2;
        scanf("%d",&n);
        int t1=0,t2,now=0;
        ME(map);
        FOR(z,n){
                scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
                for (int x=x1;x<=x2;++x)
                for (int y=y1;y<=y2;++y)  if (map[0][x][y]==0){
                        map[0][x][y]=1;
                        ++now;
                }
        }
        int ans=0;
        while (now!=0){
                ++ans;
                now=0;
                t2=t1^1;
                for (int x=1;x<=100;++x)
                for (int y=1;y<=100;++y) 
                if (map[t1][x-1][y] && map[t1][x][y-1]) {
                        map[t2][x][y]=1;
                        ++now; 
                } else
                if (map[t1][x][y] && (map[t1][x-1][y] || map[t1][x][y-1])) {
                         map[t2][x][y]=1;
                        ++now; 
                } else
                map[t2][x][y]=0;
                t1=t2;
        }
        printf("Case #%d: %d\n",t,ans);
}
int main(){
        freopen("a.in","r",stdin);
        freopen("a.out","w",stdout);
        cin>>T;
        for(t=1;t<=T;++t){
                init();
        }
       // while (1>0) {}

}
