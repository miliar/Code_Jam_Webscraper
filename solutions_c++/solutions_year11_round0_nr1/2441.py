#include <iostream>
#include <vector>
#include <cmath>
#include <boost/foreach.hpp>

using namespace std;

int main(int argc, const char* argv[])
{
    size_t T, N;
    cin >> T;

    for (size_t test = 1; test <= T; ++test) {
        cin >> N;
        unsigned long time = 0;
        unsigned long sinceO = 0;
        unsigned long sinceB = 0;
        long posO = 1;
        long posB = 1;
        for (size_t order = 0; order < N; ++order) {
            int target;
            char robot;
            cin >> robot >> target;
            if (robot == 'O') {
                unsigned long need = abs(posO - target);
                unsigned long used = 1 + (sinceB < need ? need - sinceB : 0);
                sinceO += used;
                posO = target;
                time += used;
                sinceB = 0;
            } else {
                unsigned long need = abs(posB - target);
                unsigned long used = 1 + (sinceO < need ? need - sinceO : 0);
                sinceB += used;
                posB = target;
                time += used;
                sinceO = 0;
            }
        }
        cout << "Case #" << test << ": " << time << endl;
    }
    return 0;
}
