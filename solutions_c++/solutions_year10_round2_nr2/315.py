#include <iostream>

using namespace std;

int main(){
    int NC; cin >> NC;
    for (int q = 1; q <= NC; q++){
        cerr << "Caso " << q << endl;
        long long N,K,B,T;
        cin >> N >> K >> B >> T;
        long long dx[N];
        long long v[N];
        for (int i=0;i<N;i++){
            cin >> dx[i];
        }
        for (int i=0;i<N;i++){
            cin >> v[i];
        }
        bool ok[N];
        for (int i=0;i<N;i++){
            if (dx[i]+v[i]*T >= B) ok[i] = true;
            else ok[i] = false;
        }
        int res = 0;
        int curr = 0;
        for (int i=N-1;i>=0 && curr < K;i--){
            if (ok[i]){
               curr++;
               for (int j=i+1;j<N;j++){
                   if (!ok[j]) res++;
               }
            }
        }
        cout << "Case #" << q << ": ";
        if (curr < K) cout << "IMPOSSIBLE" << endl;
        else cout << res << endl;
    }
    return 0;
}
