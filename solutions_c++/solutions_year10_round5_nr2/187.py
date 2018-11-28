

#include <iostream>
using namespace std;

typedef long long int64;

const int
    MAX = 1000000;

int T, tc;
int64 N, K;
int64 vals[200];
int dp[MAX];

int main(){

    cin >> T;
    
    for (tc = 1; tc <= T; tc++){
    
        int64 sol = -1;
        
        cin >> N >> K;
        
        int64 max = -1;
        
        for (int i = 0; i < K; i++){
            cin >> vals[i];
            if (vals[i] > max) max = vals[i]; 
        }
        
        for (int i = 1; i < MAX; i++){
            dp[i] = 100 * MAX;
            for (int j = 0; j < K; j++)
                if (i - vals[j] >= 0 && dp[i] > dp[i - vals[j]] + 1)
                    dp[i] = dp[i - vals[j]] + 1;
        }
        
        for (int i = 0; i < MAX; i++)
            if ((N - i) % max == 0 && dp[i] != 100 * MAX){
            
                int64 cant = (N - i) / max + dp[i];
                
                //if (cant > N){
                  //  cout << "ERROR\n";
                //}
        
                //cout << "cant = " << cant << "\n";
                
                if (sol == -1 || cant < sol) sol = cant;
                
            
            }
    
        cout << "Case #" << tc << ": ";
        
        if (sol == -1) cout << "IMPOSSIBLE\n";
        else cout << sol << "\n";
    
    }

    return 0;
}
