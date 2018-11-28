#include <iostream>
#include <vector>

using namespace std;

#define p first
#define ben second

typedef pair<int,int> PII;

int main(){
    int T;
    cin >> T;
    for(int t = 1; t<=T;t++){
            cout << "Case #" << t << ": ";
            long long R,K,N;
            cin >> R >> K >> N;
            vector<long long> g(N);
            for(int i=0;i<N;i++) cin >> g[i];
            vector<PII> vis(N, PII(-1,-1));
            long long i = 0, dentro;
            long long pasos = 0, beneficio = 0;
            long long prim;
            while(R){
                     for(prim = i, dentro = 0; (dentro == 0 || prim != i) && dentro + g[i] <= K; dentro += g[i], i = (i+1)%N);
                     beneficio += dentro;
                     pasos++;
                     R--;
                     if(vis[i].p != -1) break;
                     vis[i].p = pasos;
                     vis[i].ben = beneficio;

            }

            if(!R){
                   cout << beneficio << endl;
                   continue;
            }
            
            beneficio += (beneficio - vis[i].ben) * (R / (pasos - vis[i].p));

            R = R%(pasos-vis[i].p);
            
            while(R){
                     for(prim = i, dentro = 0; (dentro == 0 || prim != i) && dentro + g[i] <= K; dentro += g[i], i = (i+1)%N);
                     beneficio += dentro;
                     pasos++;
                     R--;
            }
            
            cout << beneficio << endl;
            
            
    }
}
