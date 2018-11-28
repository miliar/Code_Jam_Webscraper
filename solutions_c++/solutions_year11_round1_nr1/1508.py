#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    long long N;
    long long PD, PG;
    for( int i = 0; i < T; i++){
        bool result = false;
        cin >> N;
        cin >> PD;
        cin >> PG;
        for( int j = 1; j <= N; j++){
            if( j * PD % 100 == 0){
                result = true;
            }
        }
        if(PD != 100 && PG == 100)
            result = false;
        if(PD != 0 && PG == 0)
            result = false;


        if(result)
            cout << "Case #" << i+1 << ": Possible" << endl;
        else
            cout << "Case #" << i+1 << ": Broken" << endl;

    }
}

