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
#include <memory.h>

using namespace std;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi>  vvi;


int calcResult() {
    int N;
    cin >> N;
    vvi v(N, vi(4));
    int iMaxX = 0;
    int iMaxY = 0;

    for (int i = 0; i < N; i++) {
        cin >> v[i][1];
        cin >> v[i][0];
        cin >> v[i][3];
        cin >> v[i][2];

        iMaxX = std::max(iMaxX, v[i][2]);
        iMaxY = std::max(iMaxY, v[i][3]);
    }
    iMaxX++;
    iMaxY++;

    int table[iMaxX][iMaxY];
    int table2[iMaxX][iMaxY];

    memset(table, 0, sizeof(table));

    for (int i = 0; i < N; i++) {
        for (int j = v[i][0]; j <= v[i][2]; j++) {
            for (int k = v[i][1]; k <= v[i][3]; k++) {
                table[j][k] = 1;
            }
        }
    }

    int iCnt = 0;

    while (1) {
        /*
        if (iCnt > 10) break;

        for (int i = 0; i < iMaxX; i++) {
            for (int j = 0; j < iMaxY; j++) {
                cout << (table[i][j] ? 'X' : '.');
            }
            cout << endl;
        }
        cout << endl;
*/
        bool bCorrect = true;

        for (int i = 0; i < iMaxX && bCorrect; i++) {
            for (int j = 0; j < iMaxY; j++) {
                if (table[i][j]) {
                    bCorrect = false;
                    break;
                }
            }
        }

        if (bCorrect) return iCnt;
        iCnt++;

        for (int i = 0; i < iMaxX; i++) {
            for (int j = 0; j < iMaxY; j++) {
                if (table[i][j] == 1) {
                    if (i > 0 && j > 0 && (table[i-1][j] || table[i][j-1])) {
                        table2[i][j] = 1;
                    }
                    else {
                        table2[i][j] = 0;
                    }
                }
                else if (table[i][j] == 0) {
                    if (i > 0 && j > 0 && table[i-1][j] && table[i][j-1]) {
                        table2[i][j] = 1;
                    }
                    else {
                        table2[i][j] = 0;
                    }
                }
            }
        }

        memcpy(table, table2, sizeof(table2));
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
