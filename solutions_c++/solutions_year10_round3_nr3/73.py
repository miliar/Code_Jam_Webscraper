/**
   File: main.cpp

   (c) Copyright Albert Graells Rovira

   $Id$
*/

#include <iostream>
#include <vector>
#include <cmath>
#include <map>

using namespace std;

typedef pair<int,int> pii;

bool inside(int x1, int y1, int x2, int y2, int px, int py) {
    return (x1 <= px && px <= x2 && y1 <= py && py <= y2);
}

bool used(int x, int y, int m, const vector<pair<pii, int> >& vDone) {
    for (int i = 0; i < int(vDone.size()); i++) {
        int n = vDone[i].second;
        int x1 = vDone[i].first.first;
        int y1 = vDone[i].first.second;
        int x2 = x1 + n;
        int y2 = y1 + n;
        if (inside(x1, y1, x2 - 1, y2 - 1, x,     y))     return true;
        if (inside(x1, y1, x2 - 1, y2 - 1, x+m-1, y))     return true;
        if (inside(x1, y1, x2 - 1, y2 - 1, x+m-1, y+m-1)) return true;
        if (inside(x1, y1, x2 - 1, y2 - 1, x,     y+m-1)) return true;
    }
    return false;
}

int calcResult() {
    int N, M;
    cin >> N >> M;
    int v[N][M];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M/4; j++) {
            char c; cin >> c;
            if (isdigit(c)) c = c - '0';
            else            c = c - 'A' + 10;
            v[i][j * 4 + 0] = (c >> 3) & 1;
            v[i][j * 4 + 1] = (c >> 2) & 1;
            v[i][j * 4 + 2] = (c >> 1) & 1;
            v[i][j * 4 + 3] = (c >> 0) & 1;
        }
    }

    std::map<int, int> mapDone;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if ((i + j) & 1) v[i][j] = 1 - v[i][j];
        }
    }

    int vInt[N+1][M+1];
    for (int i = 0; i < M+1; i++) vInt[0][i] = 0;
    for (int i = 0; i < N+1; i++) vInt[i][0] = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            vInt[i+1][j+1] = vInt[i][j+1] + vInt[i+1][j] - vInt[i][j] + v[i][j];
        }
    }

    vector<pair<pii, int> > vDone;
    int iArea = N*M;

    for (int i = std::min(N, M); i > 1; i--) {
        for (int j = 0; j + i <= N; j++) {
            for (int k = 0; k + i <= M; k++) {
                int iCurrentArea = vInt[j][k] + vInt[j+i][k+i] - vInt[j][k+i] - vInt[j+i][k];
//                cout << i << " " << j << " " << k << " " << iCurrentArea << endl;
                if (iCurrentArea == 0 || iCurrentArea == i*i) {
                    if (! used(j, k, i, vDone)) {
                        iArea -= i*i;
                        vDone.push_back(make_pair(pii(j,k), i));
                        mapDone[i]++;
                    }
                }
            }
        }
    }

    if (iArea) mapDone[1] += iArea;

    cout << mapDone.size() << endl;

    for (map<int,int>::reverse_iterator it = mapDone.rbegin(); it != mapDone.rend(); it++) {
        cout << it->first << " " << it->second << endl;
    }

    return 0;
}

int main()
{
    int N;
    cin >> N;
    for (int k = 1; k <= N; k++) {
        cout << "Case #" << k << ": ";
        calcResult();
    }
    return 0;
}
