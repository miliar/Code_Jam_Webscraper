/**
   File: main.cpp

   (c) Copyright Albert Graells Rovira

   $Id$
*/

#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <queue>

using namespace std;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi>  vvi;

bool isGood(int x, int y, const vvi& v) {
    int N = int(v.size());
    set<int> vPos;
    if (v[x][y] != -1) vPos.insert(v[x][y]);
    if (v[y][x] != -1) vPos.insert(v[y][x]);
    x = N - x - 1;
    y = N - y - 1;
    if (v[x][y] != -1) vPos.insert(v[x][y]);
    if (v[y][x] != -1) vPos.insert(v[y][x]);
    return vPos.size() <= 1;
}

bool isGood(const vvi& v) {
    int N = int(v.size());
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (! isGood(i, j, v)) return false;
        }
    }
    return true;
}

void create(vvi& w, const vvi& v, const vi& now) {
   int N = int(v.size());
   int iNewN =  N + (now[0] + now[1] + now[2] + now[3]) / 2;
   if (iNewN != int(w.size())) {
       w = vvi(iNewN, vi(iNewN));
   }
   for (int i = 0; i < iNewN; i++) {
       for (int j = 0; j < iNewN; j++) {
           w[i][j] = -1;
       }
   }

   for (int i = 0; i < N; i++) {
       for (int j = 0; j < N; j++) {
           w[i + now[0]][j + now[1]] = v[i][j];
       }
   }
}


int calcResult() {
    int N;
    cin >> N;
    vvi v(N, vi(N));

    int x = 0, y = 0, iDoing = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {

            if (! (0 <= x && x < N && 0 <= y && y < N)) {
                iDoing++;
                x = iDoing;
                y = 0;
                while (x >= N) {
                    x--; y++;
                }
            }

            cin >> v[x][y];
            x--; y++;
        }
    }

    set<vi> s;
    s.insert(vi(4));
    queue<vi> q;
    q.push(vi(4));

    vvi w;

    while (! q.empty()) {
        vi now = q.front();
        q.pop();
        create(w, v, now);
        if (isGood(w)) {
            /*
            for (int i = 0; i < int(w.size()); i++) {
                for (int j = 0; j < int(w.size()); j++) {
                    if (w[i][j] == -1) cout << ". ";
                    else               cout << w[i][j] << " ";
                }
                cout << endl;
            }
            */


            int iVal = (now[0] + now[1] + now[2] + now[3]) / 2;
            int iRes = 0;
            while (iVal != 0) {
                iRes += 2*N + 1;
                iVal--;
                N++;
            }
            return iRes;
        }
        else {
            for (int i = 0; i < 4; i++) {
                vi f = now;
                f[i]++;
                f[(i + 1) & 3]++;
                if (s.find(f) == s.end()) {
                    s.insert(f);
                    q.push(f);
                }
            }
        }
    }

    return 0;
}

int main()
{
    int N;
    cin >> N;
    for (int k = 1; k <= N; k++) {
        cout << "Case #" << k << ": ";
        int iResult = calcResult();
        cout << iResult << endl;
    }
    return 0;
}
