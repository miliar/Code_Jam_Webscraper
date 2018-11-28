#include <iostream>
#include <sstream>
#include <cmath>
#include <cstring>
#include <map>
#define inf 1000000000
#define len(a) int((a).size())
#define pb push_back
using namespace std;

int main(){
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        int n, k;
        cin >> n >> k;
        bool ok = true;
        for (int i = 0; i < n; i++){
            if ((k&(1<<i)) == 0){
                ok = false;
                break;   
            }
        }       
        cout << "Case #" << t << ": ";
        if (ok){
            cout << "ON";    
        } else {
            cout << "OFF";    
        }
        cout << endl;
    }
    return 0;    
}
