#include <iostream>
using namespace std;
int abs(int v) 
{
    return v < 0 ? -v : v;
}

int main()
{
    int T ,r = 0;
    cin >> T;
    while(r++ < T) {
        int N, ic, oldic = 0;
        int delta_t, time = 0;
        int bt[2], bb[2] = {1,1}, t[2] = {0, 0};
        cin >> N;
        char color;

        for (int i = 0; i < N; i++) {
            cin >> color;
            ic = (color == 'O') ? 0 : 1;
            cin >> bt[ic];
            if (ic != oldic) {
                time += t[oldic];
                delta_t = abs(bt[ic] - bb[ic]);
                t[ic] = delta_t > t[oldic] ? delta_t - t[oldic] : 0;
                bb[ic] = bt[ic];
            }
            t[ic] += abs(bt[ic] - bb[ic]) + 1; 

            bb[ic] = bt[ic];
            oldic = ic;
        }
        time += t[ic];
        cout << "Case #" << r << ": " << time << endl;
    }

    return 0;
}
