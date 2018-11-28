#include <iostream>
#include <sstream>
#include <cmath>
#include <cstring>
#include <map>
#define inf 1000000000
#define len(a) int((a).size())
#define pb push_back
#define maxn 1010
using namespace std;
typedef long long int64;

int G[maxn], R, N;
int nextg[maxn];
int64 profit[maxn], C;

void input(){
    cin >> R >> C >> N;    
    for (int i = 0; i < N; i++){
        cin >> G[i];    
    }
}

int64 solve(){
    for (int i = 0; i < N; i++){
        profit[i] = 0;
        for (int j = i; j < i+N; j++){
            int g = j%N;
            nextg[i] = g;
            if ((g == i && j != i) || profit[i]+int64(G[g]) > C) break;
            profit[i] += G[g];
        }    
    }
    
    int cur = 0;
    int64 res = 0;
    for (int i = 0; i < R; i++){
        //cout << cur << " " << profit[cur] << " " << nextg[cur] << endl;
        res += profit[cur];
        cur = nextg[cur];
    }
    return res;
}

int main(){
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        input();    
        cout << "Case #" << t << ": " << solve() << endl;        
    }
    return 0;    
}
