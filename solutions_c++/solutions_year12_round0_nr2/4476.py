#include<iostream>

using namespace std;

int main( ){

    int t, n, s, p, i, j, e;
    cin >> t;

    for( i = 0; i < t; i++ ){
        int count = 0;
        cin >> n >> s >> p;
        for( j = 0; j < n; j++ ){
            cin >> e;

            if( e < p ){
                continue;
            }else if( p*3 <= e ){
                count++;
            }else if( p*3 - e == 1 || p*3 - e == 2 ){
                count++;
            }else if( p*3 - e == 3 || p*3 - e == 4 ){
                if( s > 0 ){
                    s--;
                    count++;
                }
            }

        }
        cout << "Case #" << i+1 <<": "<< count << endl;
    }

    return 0;

}
