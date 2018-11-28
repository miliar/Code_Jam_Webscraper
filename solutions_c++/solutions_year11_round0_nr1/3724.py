#include <iostream.h>
#include <math.h>

int main() {
    unsigned int n, t;

    cin >> t;

    for(double i = 0; i < t; i++) {
        int o = 1, b = 1, s = 0;
        int dxO = 0, dxB = 0;
        cin >> n;
        for(int j = 0; j < n; j++) {
            char r;
            int p;
            cin >> r >> p;

            if(r == 'O') {
                if(p > o) {
                    o = fmin(p, o+dxO);
                } else {
                    o = fmax(p, o-dxO);
                }
                dxB += abs(o - p) + 1;
                s += abs(o - p) + 1;
                o = p;
                dxO = 0;
            } else {
                if(p > b){
                    b = fmin(p, b+dxB);
                } else {
                    b = fmax(p, b-dxB);
                }
                dxO += abs(b - p) + 1;
                s += abs(b - p) + 1;
                b = p;
                dxB = 0;
            }
            //printf("o=%d b=%d s=%d dxO=%d, dxB=%d\n", o, b, s, dxO, dxB);
        }

        cout << "Case #" << i+1 << ": " << s << "\n";
    }

    return 0;
}
