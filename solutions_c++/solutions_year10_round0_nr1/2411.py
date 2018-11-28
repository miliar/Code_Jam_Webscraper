#include <iostream>

using namespace std;

int main()
{
    int lines;
    cin >> lines;
    int sockets,snaps;
    for (int i = 0; i < lines; i++) {
        cin >> sockets >> snaps;
        int power = 1 << sockets;
        if (snaps % power == power-1) {
            cout << "Case #" << i+1 << ": ON\n";
        } else {
            cout << "Case #" << i+1 << ": OFF\n";
        }
    }
    return 0;
}
