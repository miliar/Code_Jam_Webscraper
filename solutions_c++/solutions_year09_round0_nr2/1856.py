#include <iostream>
#include <string>
#include <queue>
using namespace std;
#define N 100
#define MAXN 1000000

struct node{
    int x,y;
    int t;
};    
int h,w;
int g[N][N];
char ans[N][N];
bool v[N][N];
char u[255];
int x[] = {-1,0,0,1,};
int y[] = {0,-1,1,0};
priority_queue<node> ss;

bool operator < (struct node a,struct node b){
    return a.t < b.t;
}    
bool check(int x,int y){
    if (x <0 || y<0 || x>=h || y>=w) return false;
    return true;
}
    
char dfs(int a,int b){
    v[a][b] = 1;
    int dx,dy;
    int low =  g[a][b];
    for (int i=0 ;i<4 ;++i){
        int tx = a + x[i];
        int ty = b + y[i];
        if (!check(tx,ty) || g[tx][ty] >= low) continue;
        low = g[tx][ty];
        dx = tx;
        dy = ty; 
    }    
    if (v[dx][dy]) ans[a][b] = ans[dx][dy];
    else ans[a][b] = dfs(dx,dy);
    return ans[a][b];
}
    
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,index = 0;
    cin>>T;
    while (T--){
        cin>>h>>w;
        node tmp;
        while (!ss.empty()) ss.pop();
        for (int i=0 ;i<h; ++i)
            for (int j=0 ;j<w; ++j) {
                cin>>g[i][j];
                tmp.x = i;
                tmp.y = j;
                tmp.t = g[i][j];
                ss.push(tmp);
            }       
        memset(ans,0,sizeof(ans));
        memset(v,0,sizeof(v));
        char d = 'a';
        for (int i=0 ;i<h; ++i)
            for (int j=0 ;j<w ;++j){
                bool f = true;
                for (int k=0 ;k<4; ++k){
                    int tx = i + x[k];
                    int ty = j + y[k];
                    if (!check(tx,ty)) continue;
                    if (g[tx][ty] < g[i][j]){
                        f = false;
                        break;
                    }    
                }
                if (f){
                    v[i][j] = 1;
                    ans[i][j] = d++;
                }    
            }    
        while (!ss.empty()){
            tmp = ss.top();
            ss.pop();
            if (!v[tmp.x][tmp.y]) dfs(tmp.x,tmp.y);
        }     
        printf("Case #%d:\n",++index);
        memset(u,0,sizeof(u));
        d = 'a';
        for (int i=0 ;i<h ;++i)
            for (int j=0 ;j<w ;++j){
                int k = ans[i][j]-'a';
                if (u[k]==0) u[k] = d++;
                printf("%c",u[k]);
                if (j < w-1) printf(" ");
                else printf("\n");
            }    
            
    }    
    return 0;
}    
