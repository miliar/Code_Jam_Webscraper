#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <algorithm>
using namespace std;
//#define ONLINE_JUDGE
#define PB push_back
#define MP make_pair
#define CLR(x,y) memset((x),y,sizeof(x))
#define rep(i,n) for(int i=0; i<(n); i++)
#define forr(i,a,b) for(int i=(a);i<=(b);i++)

const int maxn=51;

char mp[maxn][maxn+5];
int dx[4]={0,0,1,1};
int dy[4]={0,1,0,1};
int n,m;

bool check(int x,int y) {
    rep(i,4) {
        int xx=x+dx[i], yy=y+dy[i];
        if(xx<0||xx>=n||yy<0||yy>=m||mp[xx][yy]!='#') return false;        
    }   
    return true;
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    #endif

    int tt, cas = 1;
    scanf("%d", &tt);
    for(cas=1; cas<=tt; cas++) {
        //To-Do
        
        scanf("%d%d",&n,&m);
        rep(i,n) {
            scanf("%s",mp[i]);   
        }
        bool fin=true;
        rep(i,n) 
        {
            rep(j,m)
            {
                if(mp[i][j]=='#') {
                    if(check(i,j)) {
                        mp[i][j]='/';
                        mp[i][j+1]='\\';
                        mp[i+1][j]='\\';
                        mp[i+1][j+1]='/';
                    }
                    else {
                        fin=false;
                        break;   
                    }   
                }
            }
            if(!fin) break;
        }
        printf("Case #%d:\n",cas);
        if(!fin) printf("Impossible\n");
        else {
            rep(i,n) printf("%s\n",mp[i]);   
        }
    }
    //system("pause");
    return 0;
}
