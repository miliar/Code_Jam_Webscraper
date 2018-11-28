#include <iostream>

using namespace std;

#define INF 10000000

int main(){
    int T;
    cin >> T;
    for ( int i = 0; i < T; i++ ){
        int N;
        int min = INF;
        int value = 0;
        int sum = 0;
        cin >> N;
        for ( int j = 0; j < N; j++){
            int ci;
            cin >> ci;
            if ( min >= ci )
                min = ci;
            value = value ^ ci;
            sum = sum + ci;
        }
        if ( value != 0 )
            cout << "Case #" << i + 1 << ": NO" << endl;
        else
            cout << "Case #" << i + 1 << ": " << sum - min << endl;
    }

}
