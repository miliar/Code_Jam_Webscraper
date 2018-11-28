#include <stdlib.h>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int T;
int ropeNum;
int *A, *B;
int intersectNum = 0;
int *results;

void findIntersects(int c) {
    int tempA = A[c];
    int tempB = B[c];
    for (int h = c + 1; h < ropeNum; h++) {
        if (tempA <= A[h] && tempB >= B[h])
            intersectNum++;

        else if (tempA >= A[h] && tempB <= B[h])
            intersectNum++;
    }
}

int main() {
    cin >> T;
    results = new int[T];
    for (int i = 0; i < T; i++) {
        cin >> ropeNum;
        A = new int[ropeNum];
        B = new int[ropeNum];

        for (int j = 0; j < ropeNum; j++) {
            cin >> A[j] >> B[j];
        }

        for (int g = 0; g < ropeNum-1; g++) {
            findIntersects(g);
        }
        results[i] = intersectNum;
        
        intersectNum = 0;
        delete[] A;
        delete[] B;
    }

    for(int u = 0; u < T; u++) {
        cout << "Case #" << u + 1 << ": " << results[u];
    }

    return 0;
}
