#include <iostream>
#include <set>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <fstream>
using namespace std;

int main() {
    ifstream cin("B-small-attempt2 (1).in");
    ofstream cout("out.txt");
    int T;
    cin >> T;
    for(int tt = 1; tt <= T; tt++) {
        int R,C,D;
        cin >> R >> C >> D;
        vector<vector<int> > w(R, vector<int>(C));
        for(int i = 0; i < R; i++)
            for(int j = 0; j < C; j++) {
                char c;
                cin >> c;
                w[i][j] = D+c-'0';
            }
        int res = 0;
        int maxK = min(R,C);
        for(int K = 3; K <= maxK; K++) {
            double ci = 0;
            double cj = 0;
            for(int i = 0; i <= R-K; i++) {
                vector<double> wx(R);
                vector<double> wy(K);
                for(int l = 0; l < R; l++) {
                    for(int j = 0; j < K; j++) {
                        wx[l] += w[j+i][l];
                        if(l < K)
                            wy[j] += w[j+i][l];
                    }
                }
                for(int j = 0; j <= C-K; j++) {
                    ci = i + K/2. - 0.5;
                    cj = j + K/2. - 0.5;
                    double smx = 0;
                    double smy = 0;
                    for(int l = 0; l < K; l++) {
                        smx += (j+l-cj)*wx[l+j];
                        smy += (i+l-ci)*wy[l];
                    }
                    smx -= (j-cj)*(w[i][j]+w[i+K-1][j]) + (j+K-1-cj)*(w[i][j+K-1] + w[i+K-1][j+K-1]);
                    smy -= (i-ci)*(w[i][j]+w[i][j+K-1]) + (i+K-1-ci)*(w[i+K-1][j] + w[i+K-1][j+K-1]);
                    //cout << K << " " << i << " " << j << " " << smx << " " << smy << endl;
                    if(fabs(smx) < 1e-6  && fabs(smy) < 1e-6)
                        res = K;
                    if(res == K)
                        break;
                    if(j < (C-K))
                        for(int l = 0; l < K; l++)
                            wy[l] += -w[i+l][j] + w[i+l][j+K];
                }
                if(res == K)
                    break;
            }
        }
        cout << "Case #" << tt << ":";
        cout << " ";
        cout.precision(15);
        if(res == 0)
            cout << "IMPOSSIBLE";
        else
            cout << res;
        cout << endl;
    }
}
