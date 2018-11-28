#include <iostream>
using namespace std;

#define MAX 3000
int flag[10010][MAX][2];
int mark[10010];

typedef struct{
    int gate, change, value;
}NODE;
NODE node[10010];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large-out.txt", "w", stdout);
    int i, j, k, w ,t, h, kase, l, r, M, V;
    cin >> kase;
    for(i = 1; i <= kase; i++){
        cin >> M >> V;
        memset(flag, 0, sizeof(flag));
        memset(mark, 0, sizeof(mark));
        for(j = 1; j <= M; j++){
            if(j <= (M-1)/2 ){
                cin >> node[j].gate >> node[j].change;
                mark[j] = node[j].change;
            }
            else { // leaf
                cin >> node[j].value;
                flag[j][0][node[j].value] = 1;
            }
        }
        //int my = 0;
        for(j = (M-1)/2; j >= 1; j--){
            mark[j] += mark[j*2] + mark[j*2+1];   
            //if(mark[j] > my)  my = mark[j];
        }
        for(j = (M-1)/2; j >= 1 ; j--){
            int l = 2*j;
            int r = 2*j+1;
            for(k = 0; k <= mark[l]; k++){
                for(w = 0; w <= mark[r]; w++){
                    for(t = 0; t < 2; t++){
                        for(h = 0; h < 2; h++){
                            if(flag[l][k][t] && flag[r][w][h]){
                                int tmp = node[j].gate;
                                int res;
                                if(tmp == 1) res = t&h;
                                else res = t|h;
                                flag[j][k+w][res] = 1;
                                if(node[j].change){
                                    if(node[j].gate == 1) tmp = 0;
                                    else tmp = 1;
                                    if(tmp == 1) res = t&h;
                                    else res = t|h;
                                    flag[j][k+w+1][res] = 1;
                                }
                            }
                        }
                    }
                }
            }
        }
        for(k = 0; k < MAX; k++)
            if(flag[1][k][V] == 1) break;
        if(k == MAX) cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        else cout << "Case #" << i << ": " << k << endl;
        //cout << my << endl;
    }
    return 0;
}
