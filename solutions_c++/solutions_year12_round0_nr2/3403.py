#include <iostream>
#include <fstream>

using namespace std;

int d [35][2];

int main()
{
    ifstream in ("input.txt");
    ofstream out ("output.txt");

    for (int i=0; i <= 10; i++)
        for (int j=0; j <= 10; j++)
            for (int k=0; k <= 10; k++) {
                int Max = max (max (i, j), k);
                int Min = min (min (i, j), k);
                int type = (Max - Min <= 2);
                if (type) {
                    if (Max - Min < 2) type = 0;
                    d [i+j+k][type] = max (d [i+j+k][type], Max);
                }
            }
    int T;
    in >> T;

    for (int it = 1; it <= T; it++) {
        int N, S, p;
        in >> N >> S >> p;

        int c1 = 0, c2 = 0;

        for (int i=1; i <= N; i++) {
            int x;
            in >> x;
            if (d [x][0] >= p) c1++; else if (d [x][1] >= p) c2++;
        }

        out << "Case #" << it << ": " << c1 + min (S, c2) << endl;
    }

    return 0;
}
