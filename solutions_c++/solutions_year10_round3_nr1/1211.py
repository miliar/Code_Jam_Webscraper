#include <iostream>
#include <fstream>
#include <string>

using namespace std;

inline int between(int x, int y, int z) {
//    cout << x << ", " << y << ", " << z << endl;
    return ((z >= x && z <= y) || (z <= x && z >=y));
}

int main()
{
    

    ifstream ifile("input_large.txt");

    int T;
    ifile >> T;

    for (int i = 0; i < T; ++i) {
        int N;
        ifile >> N;
        int A[10000];
        int B[10000];
        for (int j = 0; j < N; ++j) {
            ifile >> A[j] >> B[j];
        }

        int count = 0;
        for (int j = 0; j < N; ++j) {
            for (int k = 0; k < N; ++k) {
                if (j == k)
                   continue;
                if ((between(A[j], B[j], A[k]) && between(A[j], B[j], B[k])) ||
                    (between(1, A[j], A[k]) && between(B[j], 20000, B[k])) ||
                    (between(A[j], 20000, A[k]) && between(1, B[j], B[k]))) {
                                   count++;
                    }
            }
        }
        cout << "Case #" << (i+1) << ": " << count/2 << endl;
    }

    cin.get();
}
