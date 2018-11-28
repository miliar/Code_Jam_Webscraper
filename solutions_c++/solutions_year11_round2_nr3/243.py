#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int n, x, s, N, M, U[10], V[10], ok;
int c[10];

int nv;
int v[10][10];


bool verif(){

    int i, j;
    int q[10];
    for(i = 1; i <= x; i++)
        q[i] = 0;

    for(i = 1; i <= n; i++)
        q[c[i]] = 1;

    for(i = 1; i <= x; i++)
        if(q[i] == 0)
            return false;

    for(i = 0; i < nv; i++){
        for(j = 1; j <= x; j++)
            q[j] = 0;

        for(j = 1; j <= v[i][0]; j++)
            q[c[v[i][j]]] = 1;

        for(j = 1; j <= x; j++)
            if(q[j] == 0)
                return false;
    }

    return true;

}


void gen(int k){

    int i;
    if(k == n+1){

            if(ok && verif()){

                ok = 0;
            }
            //else { ok = 0; return; }

    }
    else{
        for(i = 1; i <= x && ok; i++){
            c[k] = i;
            gen(k+1);
        }
     if(!ok) return;
    }


}

int main()
{
    ifstream f("3.in");
    ofstream g("3.out");

    int t, T, i, C, aux[10], lx, j;
    f >> T;
    for(t = 1; t <= T; t++){
        f >> N >> M;
        for(i = 0; i < M; i++)
            f >> U[i];
        for(i = 0; i < M; i++)
            f >> V[i];
        n = N;

        nv = 0; lx = 1;
        for(i = 0; i <= n; i++)
            aux[i] = 0;
        for(C = 2; C <= N; C++)
            for(i = 0; i < M; i++)
                if(V[i] - U[i] == C){
                    lx = 1;
                    v[nv][lx++] = V[i];
                    v[nv][lx++] = U[i];
                    for(j = U[i] + 1; j < V[i]; j++){
                        if(aux[j] == 0)
                            v[nv][lx++] = j, aux[j] = 1;

                    }
                    v[nv++][0] = lx-1;
                }
        lx = 1;
        for(i = 1; i <= n; i++)
            if(aux[i] == 0)
                v[nv][lx++] = i, aux[i] = 1;
        v[nv++][0] = lx - 1;

        for(C = N; C >= 1; C--){
            n = N;
            x = C;
            ok = 1;
            c[0] = 1;
            gen(1);
            if(!ok){
                g << "Case #" << t << ": " << C;
                g << "\n";
                for(i = 1; i <= n; i++)
                    g << c[i] << " ";
                g << "\n";
                break;
        }
    }
    }
    return 0;
}
