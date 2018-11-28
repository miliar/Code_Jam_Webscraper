#include <iostream>
#include <cmath>

#define ON true
#define OFF false

using namespace std;

int main() {

    int rounds, size, snaps;
    
    cin >> rounds;
    for (int r = 0; r < rounds; r++) {
        cin >> size >> snaps;
        bool on = true;
        if (snaps == 0) on = false;
        if ( ((snaps+1) % (1<<size)) != 0 ) on = false;
        cout << "Case #" << (r+1) << ": " << ( on ? "ON" : "OFF") << endl;
    }

    return 0;
}
