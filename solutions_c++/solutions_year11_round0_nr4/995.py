#include <iostream>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <iomanip>
#include <cstring>
#define MAX 1010
using namespace std;

int v[MAX];
bool used[MAX];

int main(){
    ios::sync_with_stdio(false);
    int t, n, teste = 1;
    
    cin >> t;
    while(t--){
        cin >> n;
        memset(used+1, false, n*sizeof(bool));
        for(int i = 1; i <= n; i++){
            cin >> v[i];
        }
        
        double res = 0.0;
        for(int i = 1; i <= n; i++){
            if(!used[i]){
                int x = i;
                int cont = 0;
                while(!used[x]){
                    used[x] = true;
                    x = v[x];
                    cont++;
                }
                //cout << "cont " << cont << endl;
                if(cont > 1) res += pow(2.0, cont-1);
            }
        }
        
        cout << "Case #" << teste++ << ": " << fixed << setprecision(6) << res << "\n"; 
    }
    return 0;
}
