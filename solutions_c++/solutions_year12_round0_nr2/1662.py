#include <fstream>
#include <iostream>
using namespace std;
int main(int argc, char *argv[]) {
    fstream f(argv[1]);
    int count;
    f >> count;
    for (int i = 1; i <= count; ++i) {
        int r = 0, n, s, p;
        f >> n >> s >> p;
        for (int j = 0; j < n; ++j) {
            int t;
            f >> t;
            switch (p) {
            case 0:
            case 1:
                if (t >= p)
                    ++r;
                break;
            default:
                if (t >= p * 3 - 2) {
                    ++r;
                } else if (t >= p * 3 - 4 && s > 0) {
                    ++r;
                    --s;
                }
                break;
            }
        }
        cout << "Case #" << i << ": " << r << endl;;
    }
}
