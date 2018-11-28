// NOTE!!!!!
// b=0 case is solved by hand.

#include <iostream>

using namespace std;

bool sol;

typedef unsigned long long int u64;

int valid[101];
u64 D, a, b;

bool solve(){
            for(int j = 1 ; j <= D; j++){ // played j games
                for(int k = 0; k <= j; k++){ // won k
                    float tr = 100.0 * k / j;
//                    cout << j << " " << k << " " << tr << endl;
                    if((int)tr == a and tr == (int)tr){
//                        cout << j << " " << k << " " << tr << endl;
                        // checkb
                        for(int g = 0; g <= 10001; g++){ // games played not today
                            for(int gw = 0; gw <= g; gw++){ // games won not today
                                float tr2 = 100.0 * (k+gw) / (j + g);
                                if((int)tr2 == b and tr2 == (int)tr2){
//                                   cout << "XX" << g << " " << gw << " " << tr2 << endl;
                                   sol = true;
                                   return true;
                                }
                            }
                        }
                    }
                }
            }
            return false;
}

int main(){
    int N;
    cin >> N;
            for(int j = 0; j <= 50; j++){
                float x = 100.0 / j;
                if(x == (int)x){
//                    cout << j << " " << x << endl;
                    valid[j] = true;
                    valid[100-j] = true;
                }else{
                    valid[j] = false;
                    valid[100-j] = false;
                }
            }
    for(int j = 0; j <= 100; j++){
//        cout << j << " " <<valid[j]<<endl;
    }
    for(int i = 0; i < N ; i++){
        sol = false;
        cin >> D >> a >> b;
        if(false){
            sol = false;
        }else{
            // naive
        }
        cout << "Case #" << (i+1) << ": " << (solve()?"Possible":"Broken") << endl;
//        break;
    }
}

