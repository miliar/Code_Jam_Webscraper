#include <iostream>
#include <vector>
#include <string.h>
#define maxn 110
#define inf 1000000000
#define pb push_back
#define vpi vector<pp>::iterator
using namespace std;
typedef pair<int, int> pp;

const int l1[] = {-1,0,0,1};
const int l2[] = {0,-1,1,0};

int H, W, G[maxn][maxn];
vector<pp> g[maxn][maxn];
char ans[maxn][maxn];

void init(){
    for (int i = 0; i < maxn; i++){
        for (int j = 0; j < maxn; j++){
            g[i][j].clear();
            G[i][j] = inf;
        }
    }    
}

void input(){
    cin >> H >> W;
    for (int i = 1; i <= H; i++){
        for (int j = 1; j <= W; j++){
            cin >> G[i][j];   
        }    
    }    
}

void direct(int a, int b){
    int lowest = inf, r1=-1, r2=-1;
    for (int i = 0; i < 4; i++){
        int k1 = a+l1[i], k2 = b+l2[i];
        if (lowest > G[k1][k2]){
            lowest = G[k1][k2];
            r1 = k1;
            r2 = k2;    
        }    
    }
    
    if (lowest < G[a][b]){
        g[a][b].pb(pp(r1,r2));
        g[r1][r2].pb(pp(a,b));
       // cout << a << " " << b << " -> " << r1 << " " << r2 << endl;
    }
}

void sub(int a, int b, char c){
    if (ans[a][b] != 0) return;
    ans[a][b] = c;
    for (vpi it = g[a][b].begin(); it != g[a][b].end(); it++){
        sub(it->first, it->second, c);    
    }    
}

void solve(){
    init();
    input();
    
    for (int i = 1; i <= H; i++){
        for (int j = 1; j <= W; j++){
            direct(i, j);        
        }
    }
    
    memset(ans, 0, sizeof ans);
    char letter = 'a';
    for (int i = 1; i <= H; i++){
        for (int j = 1; j <= W; j++){
            if (ans[i][j] == 0){
                sub(i,j,letter);
                letter++;    
            }        
        }
    }
    
     
    for (int i = 1; i <= H; i++){
        for (int j = 1; j <= W; j++){
            if (j != 1) cout << " ";
            cout << ans[i][j];
        }
        cout << endl;
    }
    
}

int main(){
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++){
        cout << "Case #" << i << ":" << endl;
        solve();    
    }
    return 0;    
}
