#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

#define D(x) 

using namespace std;

int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
        int k;
        cin >> k;

        int grid[k][k];

        for (int ij = 0; ij < 2*k-1; ij++) {
            for (int i = max(0, ij-k+1); i <= ij && i < k; i++) {
                int j = ij - i;
                cin >> grid[i][j];
                D(cerr << "grid[" << i << "][" << j << "] = " << grid[i][j] << endl);
            }
        }

        int minK = 9999;

        int low = -k/2-1, high = 3*k/2+1;
        for (int x = low; x < high; x++) {
            for (int y = low; y < high; y++) {
                for (int d = 0; d < 2; d++) {
                    D(cerr << "testing x=" << x << (d?".5":"") << ", y=" << y << (d?".5":"") << endl);
                    // try (x,y)
                    bool ok = true;
                    for (int i = 0; i < k && ok; i++) {
                        for (int j = 0; j < k && ok; j++) {
                            int i2 = x+y+d-j, j2 = x+y+d-i;
                            if (i2 >= 0 && i2 < k && j2 >= 0 && j2 < k && grid[i][j] != grid[i2][j2]) {
                                D(cerr << "\tmismatch of (" << i << "," << j << ") with (" << i2 << "," << j2 << ")" << endl);
                                ok = false; continue;
                            }
                            i2 = x-y+j; j2 = y-x+i;
                            if (i2 >= 0 && i2 < k && j2 >= 0 && j2 < k && grid[i][j] != grid[i2][j2]) {
                                D(cerr << "\tmismatch of (" << i << "," << j << ") with (" << i2 << "," << j2 << ")" << endl);
                                ok = false; continue;
                            }
                        }
                    }
                    if (ok) {
                        int newX = max(2*x+d+1, 2*k-2*x-d-1);
                        int newY = max(2*y+d+1, 2*k-2*y-d-1);
                        int newK = max(newX, newY);
                        D(cerr << "\t*** symmetry with k=" << newK << endl);
                        if (newK < minK) {
                            minK = newK;
                        }
                    }
                }
            }
        }
        int minCost = minK*minK - k*k;
        cout << "Case #" << testCase << ": " << minCost << endl;        
    }
}
