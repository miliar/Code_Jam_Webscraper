#include <iostream>
#include <fstream>
using namespace std;
const int maxm = 10001;
int m, v;
int sig[maxm], chg[maxm], f[maxm][2];
bool mark[maxm][2];
int workit(int op, int x, int y){
    if (op == 0) return (x | y);
    else return (x & y);
}
int calc(int node, int vv){
    if (node > (m - 1) / 2){
        if (sig[node] != vv) return -1;
        else return 0;
    }
    int tp;
    if (!mark[node][vv]){
        mark[node][vv] = true;
        f[node][vv] = -1;
            for(int i = 0; i <= 1; ++ i)
            {
                if (!chg[node] && i != sig[node]) continue;
                if (i == sig[node]) tp = 0; else tp = 1;
                for(int x = 0; x <= 1; ++ x)
                    if (calc(node * 2, x) != -1)
                    for(int y = 0; y <= 1; ++ y)
                        if (workit(i, x, y) == vv && calc(node *2 + 1, y) != -1){
                            if (f[node][vv] == -1 || calc(node*2, x) + calc(node*2+1,y) + tp < f[node][vv]){
                                f[node][vv] = calc(node*2, x) + calc(node*2+1,y) + tp;
                            }
                        }
            }
    }
    return f[node][vv];
}
int main(){
    ifstream cin ("A-large.in");
    ofstream cout("out.txt");
    int ncase;
    cin >> ncase;
    for(int tcase = 1; tcase <= ncase; ++ tcase){
        cin >> m >> v;
        memset(sig, 0, sizeof(sig));
        memset(chg, 0, sizeof(chg));
        for(int i = 1; i <= (m - 1) / 2; ++ i)
            cin >> sig[i] >> chg[i];
        for(int i = (m + 1) / 2; i <= m; ++ i)
            cin >> sig[i];
        memset(mark, false, sizeof(mark));
        cout << "Case #" << tcase << ": ";
        if (calc(1, v) == -1)
            cout << "IMPOSSIBLE" << endl;
        else cout << calc(1, v) << endl;
        //for(int i = 1; i <= m; ++ i)
        //    cout << i << " : " << calc(i, 0) << ", " << calc(i, 1) << endl;
    }
    return 0;
}
