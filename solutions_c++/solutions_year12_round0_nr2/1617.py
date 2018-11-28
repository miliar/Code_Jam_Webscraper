#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
    int nTests;
    cin >> nTests;
    for (int testNo = 1; testNo <= nTests; ++testNo) {
        int N, S, p;
        cin >> N >> S >> p;
        vector<int> tscores(N);
        for (int i = 0; i < N; i++)
            cin >> tscores[i];
        vector< vector<int> > ma(N+1, vector<int>(S+1, -10000));
        ma[0][0] = 0;
        for (int i = 0; i < N; i++) {
            bool canHaveStrange, canHaveNormal;
            canHaveStrange = canHaveNormal = false;
            for (int j1 = 0; j1 <= 10; j1++) {
                for (int j2 = j1; j2 <= 10; j2++) {
                    if (j2 - j1 > 2)
                        break;
                    for (int j3 = j1; j3 <= j2; j3++) {
                        if (j1 + j2 + j3 == tscores[i] && j2 >= p) {
                            if (j2 - j1 == 2)
                                canHaveStrange = true;
                            else
                                canHaveNormal = true;
                        }
                    }
                }
            }
            for (int j = 0; j <= S; j++) {
               if (canHaveNormal) {
                   ma[i+1][j] = max(ma[i+1][j], ma[i][j]+1);
               } else {
                   ma[i+1][j] = max(ma[i+1][j], ma[i][j]);
               }
               if (j == 0)
                   continue;
               if (canHaveStrange) {
                   ma[i+1][j] = max(ma[i+1][j], ma[i][j-1] + 1);
               } else {
                   ma[i+1][j] = max(ma[i+1][j], ma[i][j-1]);
               }
            }
        }
        cout << "Case #" << testNo << ": " << ma[N][S] << endl;
    }
    return 0;
}
