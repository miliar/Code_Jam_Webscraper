#include <iostream>
#include <vector>

using namespace std;


int main(){
    int Tc;
    cin >> Tc;
    for(int tc=1; tc <= Tc; tc++){
            int N, L, H;
            cin >> N >> L >> H;
            vector<int> n(N);
            for(int i=0;i<N;i++) cin >> n[i];
            
            int i;
            for(i=L; i <= H; i++){
                    int j;
                    for(j=0;j<N;j++) if((n[j] % i) != 0 && (i % n[j]) != 0) break;
                    if(j == N) break;
            }
            cout << "Case #" << tc << ": ";
            if(i == H+1) cout << "NO" << endl;
            else cout << i << endl;
    }
}
