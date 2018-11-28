#include <iostream>

using namespace std;

bool snap_on(long n, long k) {
    return ((k & ((1 << n) - 1)) == (1 << n) - 1);
}

int main(int argc, char **argv) {
    int cnt,i;
    long n, k;

    cin >> cnt;

    for(i = 1; i <= cnt; i++) {
        cin >> n >> k;
        cout << "Case #" << i << ": ";
        if(snap_on(n, k))
            cout << "ON" << endl;
        else
            cout << "OFF" << endl;
    }
    
    return 0;
}

