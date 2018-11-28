#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<cmath>
#include<map>
#include<cstdlib>
#include<sstream>
#include<cstring>
#include<numeric>
#include<stack>
#include<queue>
#include<cstdlib>
#include<ctype.h>
#include<algorithm>
using namespace std;
#define min(a,b) a>b?b:a
#define max(a,b) a>b?a:b
#define PI 2*acos(0.0)
#define INF 1<<17
#define setbit(a,b) a|=1<<b
#define C1(a) __builtin_popcount(a)
#define CLZ(a) __builtin_clz(a)
#define CTZ(a) __builtin_ctz(a)
#define TB(a,b) a&(1<<b)
#define PB(a,b) a.push_back(b)
#define ALL(a) (a.begin(),a.end())
#define clear(a) a.erase(a.begin(),a.end())
typedef vector<string> vs;
typedef vector<int> vi;
typedef long long LL;

int main(){
    ifstream I;
    ofstream P;
    I.open("D:\\Codings\\Codejam\\C-small-attempt2.in");
    P.open("D:\\Codings\\Codejam\\test.out");
    int t;
    I>>t;
    for(int ca=1;ca<=t;ca++){
        int n;
        I>>n;//cout<<"N = "<<n<<endl;
        bool adj[101][101],t[101][101];int x,y,a,b,tmx=0,tmy=0;
        memset(adj,0,sizeof(adj));
        for(int i=0;i<n;i++){
            I>>x>>y>>a>>b;
            tmy=max(tmx,x);tmy=max(tmx,a);
            tmx=max(tmy,y);tmx=max(tmy,b);
                int mx=max(y,b);
                int mn=min(y,b);
                int mxx=max(a,x);
                int mnx=min(a,x);
                for(int j=mnx;j<=mxx;j++){
                    for(int k=mn;k<=mx;k++){
                        //printf("%d %d\n",k,j);
                        adj[k][j]=1;
                    }
                }
        }
        /*for(int i=1;i<=tmx;i++){
            for(int j=1;j<=tmy;j++){
                printf("%d ",adj[i][j]);
            }puts("");
        }*/
        bool flag=1;int ret=0;
        while(1){
            bool f=0;ret++;
            for(int i=1;i<=tmx;i++){
                for(int j=1;j<=tmy;j++){
                    t[i][j]=adj[i][j];
                }
            }
            for(int i=1;i<=tmx;i++){
                for(int j=1;j<=tmy;j++){
                    if(t[i][j]==1&&t[i-1][j]==0&&t[i][j-1]==0)adj[i][j]=0;
                    if(t[i][j]==0&&t[i-1][j]==1&&t[i][j-1]==1)adj[i][j]=1;
                }
            }
            int count=0;
            for(int i=1;i<=tmx;i++){
                for(int j=1;j<=tmy;j++){
                    if(adj[i][j]==1)count++;
                }
            }//puts("here");
            if(!count)break;
        }
        P<<"Case #"<<ca<<": "<<ret<<endl;
    }
    return 0;
}
