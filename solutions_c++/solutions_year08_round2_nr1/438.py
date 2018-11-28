#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <algorithm>
#include <vector>
#include <ext/hash_map>
#include <ext/hash_set>
#include <string>

using namespace std;
using namespace __gnu_cxx;

int main(int argc, char* argv[]) {
    int debug = atoi(argv[2]);
    
    ifstream fin(argv[1]);    
    int num_cases;
    fin >> num_cases;

    int MAX_LENGTH = 100;
    char line[MAX_LENGTH];

    for (int i = 0; i < num_cases; i ++) {
        long long n, A, B, C, D, x0, y0, M;
        fin >> n;
        fin >> A;
        fin >> B;
        fin >> C;
        fin >> D;
        fin >> x0;
        fin >> y0;
        fin >> M;
        vector< vector<long long> > numbers(3, vector<long long>(3, 0));
        long long X, Y;
        X = x0;
        Y = y0;
        numbers[X%3][Y%3] ++;
        for (int j = 1; j < n; j++)
        {
          X = (A * X + B) % M;
          Y = (C * Y + D) % M;
          numbers[X%3][Y%3] ++;
        }
        long long result = 0;
        for (int j = 0; j < 9; ++j) {
            for (int k = j+1; k < 9; ++k) {
                for (int l = k+1; l < 9; ++l) {
                    if ((j/3+k/3+l/3)%3 == 0
                        && (j%3+k%3+l%3)%3 == 0) {
                       result += numbers[j/3][j%3]
                                *numbers[k/3][k%3]
                                *numbers[l/3][l%3];
                    }            
                }
            }
        }
        for (int j = 0; j < 9; ++j) {
            long long temp = numbers[j/3][j%3];
            result += temp * (temp - 1) * (temp - 2) / 6;
        }
        cout << "Case #" << i+1 << ": " << result << endl;
    }
    return 0;
}
