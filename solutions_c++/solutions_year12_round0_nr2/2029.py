#include <iostream>
using namespace std;

int main(void) {
    int T, S, N, p;
    cin >> T;

    for(int i = 0; i < T; i++){
        cin >> N;
        cin >> S;
        cin >> p;
        int t[N];
        int max_p[N];
        for(int j = 0; j < N; j++){
            cin >> t[j];
            switch(t[j] % 3){
                case 0:
                    max_p[j] = t[j] / 3;
                    break;
                case 1:
                    max_p[j] = (t[j] + 2) / 3;
                    break;
                case 2:
                    max_p[j] = (t[j] + 1) / 3;
                    break;
                default:
                    break;
            }
        }
        int res = 0;
        for(int k = 0; k < N; k++){
            if(max_p[k] >= p){
                res++;
            } else if((S > 0) && (t[k] % 3 != 1) && (max_p[k] + 1 >= p) && (t[k] > 1)){
                S--;
                res++;
            }
        }
        cout << "Case #"; cout << (i + 1); cout << ": "; cout << res << endl;
    }
}
