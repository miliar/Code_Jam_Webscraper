#include <iostream>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

typedef long long ll;

int main(){
    int Tc;
    cin >> Tc;
    for(int tc=1; tc <= Tc; tc++){
            long long L, t, N, C;
            cin >> L >> t >> N >> C;
            vector<ll> n(C);
            for(int i=0;i<C;i++) cin >> n[i];
            vector<ll> p(N);
            for(int i=0;i<N;i++) p[i] = n[i % C];
            vector<ll> d(N+1);
            d[0] = 0;
            t *= 2;
            for(int i=1;i<=N;i++) d[i] = d[i-1] + p[i-1]*4;
            
            ll solucion = 0;
            priority_queue<ll> mejoras;
            for(int i=0;i<N;i++){
                    if(d[i+1] < t);
                    else if(d[i] >= t) mejoras.push((d[i+1] - d[i])/2);
                    else mejoras.push((d[i+1] - t)/2);
            }
            while(!mejoras.empty() && L){
                  solucion += mejoras.top();
                  mejoras.pop();
                  L--;
            }
            
            cout << "Case #" << tc << ": ";
            cout << (d[N] - solucion)/2 << endl;
    }
}
