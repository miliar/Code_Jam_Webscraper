#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

#define MAX 10001
#define INF (MAX*2)

int M;

int gate_type[MAX];
int can_change[MAX];
int value[MAX];
int leaf[MAX];

int table[MAX][2];

int melhor(int node, int V) {
    if(table[node][V] != -1) {
        return table[node][V];
    }
    if(value[node] == V) {
        return 0;
    }
    if(leaf[node]) {
        return INF;
    }

    int resp = INF;

    for(int t=0;t<2;++t) {
        if(t != gate_type[node] and not can_change[node])
            continue;
        for(int i=0;i<2;++i) {
            for(int j=0;j<2;++j) {
                int y;
                if(t==1) {
                    y = i & j;
                } else {
                    y = i | j;
                }
                if(y == V) {
                    int a1 = melhor(node*2, i);
                    int a2 = melhor(node*2+1, j);
                    if(a1 < INF and a2 < INF) {
                        resp = min(resp, a1+a2 + (t!=gate_type[node]?1:0));
                    }
                }
            }
        }
    }

    return table[node][V] = resp;
}

int main(void) {
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;++t) {

        int V;
        scanf("%d %d", &M, &V);

        memset(table, -1,sizeof(table));

        for(int i=1;i<=(M-1)/2;++i) {
            scanf("%d%d", &gate_type[i], &can_change[i]);
            leaf[i] = 0;
        }

        for(int i=(M-1)/2+1;i<=M;++i) {
            scanf("%d", &value[i]);
            leaf[i] = 1;
            can_change[i] = 0;
        }

        for(int i=(M-1)/2;i>=1;--i) {
            if(gate_type[i]==1) {
                value[i] = value[i*2] & value[i*2+1];
            } else {
                value[i] = value[i*2] | value[i*2+1];
            }
        }


        printf("Case #%d: ", t);
        int resp = melhor(1, V);
        if(resp >= INF) {
            printf("IMPOSSIBLE");
        } else {
            printf("%d", resp);
        }

        printf("\n");
    }
    return 0;
}
