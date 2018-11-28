#include <iostream>
#include <vector>

using namespace std;

int main(){
    int t, tt = 1;
    int n, l, h;
    
    cin >> t;
    while(t--){
        vector<int> vet;
        
        cin >> n >> l >> h;
        for(int i = 0; i < n; i++){
            int aux;
            cin >> aux;
            vet.push_back(aux);
        }
        
        bool flag = false;
        int res;
        for(int i = l; i <= h && !flag; i++){
             flag = true;
            for(int j = 0; j < n; j++){
                if(i%vet[j] && vet[j]%i){
                    flag = false;
                }
            }
            if(flag) res = i;
        }
        
        cout << "Case #" << tt++ << ": ";
        if(flag){
            cout << res << endl;
        }
        else{
            cout << "NO" << endl;
        }
    }
            
    
    return 0;   
}
