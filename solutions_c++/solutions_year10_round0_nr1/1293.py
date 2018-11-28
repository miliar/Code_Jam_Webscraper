#include <iostream>

using namespace std;

int test;
int n, k;


int main()
{
    cin >> test;
    for ( int i = 0 ; i < test ; i ++ ){
        cin >> n >> k;
        cout << "Case #" << i + 1 << ": ";
        k ++;
        int temp = 1, mu = 0;
        while ( mu < n && temp <= k ){
            temp *= 2;
            mu ++;
        }
        if ( mu < n )
            cout << "OFF" << endl;
        else {
            if ( k % temp == 0 )
                cout << "ON" << endl;
            else cout << "OFF" << endl;
        }
    }
    return 0;
}
