#include <iostream>
#include <cmath>
#include <algorithm>

#define INF 0x3f3f3f3f

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    int t, teste = 1, n, mini, sum, k, x;
    
    cin >> t;
    while(t--){   
        cin >> n;
        cin >> x;
        sum = mini = k = x;
        for(int i = 1; i < n; i++){
            cin >> x;
            sum += x;
            mini = min(mini, x);
            k ^= x;
        }
        cout << "Case #" << teste++ << ": ";
        if(k){
            cout << "NO\n";
        }
        else{
            cout << sum - mini << "\n";
        } 
    }
    return 0;
}
