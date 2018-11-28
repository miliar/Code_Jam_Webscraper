#include <iostream>
#include <stdint.h>
#include <fstream>
#include <set>

using namespace std;

int main()
{
    ifstream in("a.in",ifstream::in);
    ofstream out("a.out",ofstream::out);
    int T = 0;
    in >> T;
    for(int t = 0; t< T;t++) {
        bool on = false;
        uint32_t N, K;
        in >> N >> K;
        uint32_t target = (1<<N) - 1;
        if( (K & target) == target )
            on = true;
        cout << target << " " << (K & target) << endl;
        cout << "Case #" << t+1 << ": " << (on ? "ON" : "OFF") << endl;
        out << "Case #" << t+1 << ": " << (on ? "ON" : "OFF") << endl;
    }
}
