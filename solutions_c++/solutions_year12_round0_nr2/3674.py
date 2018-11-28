#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int main() {

    int T, N, S, p;
    int y;

    cin >> T;

    for (int i=0; i<T; ++i) {
        cin >> N >> S >> p;
        y = 0;

        int pass = max(p*3 - 2, p);
        int surprisePass = max(p*3 - 4, p);

        for (int j=0; j<N; ++j) {
            int t;
            cin >> t;


            if (t >= pass) {
                y++;
            } else if (t >= surprisePass && S != 0) {
                S--;
                y++;
            }
        }



        cout << "Case #" << i+1 << ": " << y << endl;
    }

    return 0;
}
