#include <iostream>
#include <vector>
#include <cstring>
#include <queue>
#include <vector>

using namespace std;

int type[2000];
int melhor[2000];
vector<int> malted[2000];
vector<int> customers[2000];

int main(void) {
    int T;
    cin >> T;
    for(int t=1;t<=T;++t) {
        int N, M;
        cin >> N >> M;
        for(int i=0;i<M;++i) {
            int k;
            cin >> k;
            customers[i].clear();
            for(int j=0;j<k;++j) {
                int a, b;
                cin >> a >> b;
                --a;
                customers[i].push_back(a + 20000*b);
            }
        }
        int resp = 20000;
        for(int m = 0; m < (1<<N); ++ m) {
            int custo = __builtin_popcount(m);
            if(custo >= resp) continue;
            for(int i=0;i<N;++i) {
                type[i] = (m>>i) & 1;
            }
            bool satisfeito = true;
            for(int i=0;i<M;++i) {
                bool s = false;
                for(int j=0;j<int(customers[i].size());++j) {
                    int m = customers[i][j];
                    if(m >= 20000) {
                        if(type[m-20000] == 1) {
                            s = true; break;
                        }
                    } else {
                        if(type[m] == 0) {
                            s = true; break;
                        }
                    }
                }
                if(s == false) {
                    satisfeito = false;
                    break;
                }
            }
            if(satisfeito) {
                resp = custo;
                memcpy(melhor, type, sizeof(type));
            }
        }
        cout << "Case #" << t << ":";
        if(resp == 20000) {
            cout << " IMPOSSIBLE";
        } else {
            for(int i=0;i<N;++i) {
                cout << " " << melhor[i];
            }
        }
        cout << endl;
    }
    return 0;
}
