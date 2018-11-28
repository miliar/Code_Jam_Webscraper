#include <cstdio>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

#define two(x) (1ll<<(x))

char board[16][16];

typedef long long ll;

int T, R, C, M;

struct estado_t {

    int p[5];
    int m;

    bool operator<(const estado_t& e) const {
        for(int i=0;i<M;++i) {
            if(p[i] < e.p[i]) return true;
            if(p[i] > e.p[i]) return false;
        }
        return false;
    }

    void sort() {
        ::sort(this->p, this->p+M);
    }

    int tem(int v) {
        for(int i=0;i<M;++i) if(p[i] == v) return true;
        return false;
    }

    bool fim() {
        for(int i=0;i<M;++i) {
            int x = p[i]%C;
            int y = p[i]/C;
            if(board[y][x]!='x' and board[y][x]!='w') return false;
        }
        return true;
    }

    bool valid() {
        int fila[5];
        int v[5];
        int ifila, ffila;
        ifila = 0, ffila = 0;
        fila[ffila++] = 0;
        for(int i=1;i<M;++i) v[i] = 0;
        v[0]=1;
        while(ifila != ffila) {
            int k = fila[ifila++];
            int x = p[k]%C;
            int y = p[k]/C;
            for(int i=0;i<M;++i) if(v[i] == 0) {
                int x2 = p[i]%C;
                int y2 = p[i]/C;
                if(x2-x > 1 or x2-x < -1) continue;
                if(y2-y > 1 or y2-y < -1) continue;
                if(x2!=x and y2!=y) continue;
                v[i] = 1;
                fila[ffila++] = i;
            }
        }
        return ffila == M;
    }
};

set<estado_t> visitado;

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

int main(void) {
    scanf("%d", &T);
    for(int t=0;t<T;++t) {
        scanf("%d%d", &R, &C);
        M = 0;
        estado_t inicio;
        for(int i=0;i<R;++i) {
            scanf("%s", board[i]);
            for(int j=0;j<C;++j) {
                if(board[i][j] == 'o' or board[i][j]=='w') {
                    inicio.p[M] = j+i*C;
                    ++M;
                }
            }
        }
        inicio.sort();
        inicio.m = 0;

        visitado.clear();
        queue<estado_t> fila;
        fila.push(inicio);
        visitado.insert(inicio);
        int resp = -1;
        while(not fila.empty()) {
            estado_t estado = fila.front(); fila.pop();
            bool va = estado.valid();
            if(estado.fim()) {
                resp = estado.m;
                break;
            }

            for(int i=0;i<M;++i) {
                int x = estado.p[i]%C;
                int y = estado.p[i]/C;
                for(int j=0;j<4;++j) {
                    int x2 = x + dx[j];
                    int y2 = y + dy[j];
                    int x3 = x - dx[j];
                    int y3 = y - dy[j];
                    if(x2<0 or x2>C or y2<0 or y2>=R) continue;
                    if(x3<0 or x3>C or y3<0 or y3>=R) continue;
                    if(board[y3][x3] == '#' or board[y2][x2] == '#') continue;
                    if(estado.tem(x2+y2*C) or estado.tem(x3+y3*C)) continue;
                    estado_t tmp = estado;
                    tmp.p[i] = x2+y2*C;
                    tmp.m++;
                    bool o = tmp.valid();
                    if(o or ((not o) and va)) {
                        tmp.sort();
                        if(visitado.count(tmp) == 0) {
                            visitado.insert(tmp);
                            fila.push(tmp);
                        }
                    }
                }
            }

        }

        printf("Case #%d: %d\n", t+1, resp);
    }
    return 0;
}
