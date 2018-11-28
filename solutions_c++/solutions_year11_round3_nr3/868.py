#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    int N, L, H;
    int note[200];
    int ans = 0;
    bool result = false;
    for( int t = 0; t < T; t++){
        cin >> N;
        cin >> L;
        cin >> H;
        for( int k = 0; k < N; k++){
            cin >> note[k];
        }

        ans = 0;
        int k;
        for( k = L; k <= H; k++){
            result = true;
            for( int j = 0; j < N; j++){
                result = (k > note[j]) ? (k % note[j] == 0) : (note[j] % k)==0;
                if(!result)
                    break;
            }
            if( result ){
                ans = k;
                break;
            }
        }
           
        cout << "Case #" << t+1 << ": ";
        if( k == H+1 ){
            cout << "NO" << endl;
        }
        else
            cout << ans << endl;


    }
}
