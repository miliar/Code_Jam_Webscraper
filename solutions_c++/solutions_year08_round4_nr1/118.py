#include <cstdio>
#include <cstdlib>

#include <iostream>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

int M, V;
int interiorNodes;
int isAnd[10024];
int isChangeable[10024];
int value[10024];

void read_one()
{
    int i;

    cin >> M >> V;
    interiorNodes = (M - 1) / 2;
    for (i = 1; i <= (M - 1) / 2; i++)
        cin >> isAnd[i] >> isChangeable[i];
    for (; i <= M; i++) {
        cin >> value[i];
    }
}

int minChanges[10024][2];

void solve_one()
{
    int i, j, k, l;

    const int INF = 10024;
    for (i = M; i >= 1; i--) {
        if (i > interiorNodes) {
            minChanges[i][value[i]] = 0;
            minChanges[i][1 - value[i]] = INF;
        } else {
            if (isAnd[i]) {
                value[i] = value[2*i] & value[2*i + 1];
            } else {
                value[i] = value[2*i] | value[2*i + 1];
            }
            minChanges[i][value[i]] = 0;
            minChanges[i][1 - value[i]] = INF;
            for (k = 0; k <= 1; k++)
            for (l = 0; l <= 1; l++) {
                int cvalue =  (isAnd[i] ? (k & l) : (k | l));
                if ((cvalue == (1 - value[i])) && (minChanges[2*i][k] + minChanges[2*i + 1][l] < minChanges[i][1 - value[i]])) { 
                    minChanges[i][1 - value[i]] = minChanges[2*i][k] + minChanges[2*i + 1][l];
                }
                if (! isChangeable[i]) continue;
                cvalue =  (isAnd[i] ? (k | l) : (k & l));
                if ((cvalue == (1 - value[i])) && (minChanges[2*i][k] + minChanges[2*i + 1][l] + 1 < minChanges[i][1 - value[i]])) { 
                    minChanges[i][1 - value[i]] = minChanges[2*i][k] + minChanges[2*i + 1][l] + 1;
                }
            }
        }
    }


    if (minChanges[1][V] >= INF) {
        cout << "IMPOSSIBLE";
    } else {
        cout << minChanges[1][V];
    }
}

int main(void)
{
    int T, i;

    for(scanf("%d\n", &T), i = 1; i <= T; i++) {
        read_one();
        printf ("Case #%d: ", i);
        solve_one();
        printf ("\n");
    }
}

