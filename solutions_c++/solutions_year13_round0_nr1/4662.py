#include <cmath>
#include <ctime>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <queue>

using namespace std;

const int BRRED = 4;

int check (string a) {
    for (int i = 0; i < BRRED; i++) {
        if (a[i] == '.') {
            return 1;
        }
    }
    if (a == "XXXX") {
        return 2;
    }
    if (a == "OOOO") {
        return 3;
    }
    return 0;
}

int main() {
	int T;
	scanf ("%d", &T);
	char a[BRRED][BRRED + 1];
	for (int t = 1; t <= T; t++) {
        vector <string> all;
        for (int i = 0; i < BRRED; i++) {
            scanf ("%s", &a[i]);
        }
        string tmp3 = "", tmp4 = "";
        for (int i = 0; i < BRRED; i++) {
            string tmp1 = "", tmp2 = "";
            for (int j = 0; j < BRRED; j++) {
                tmp1 = tmp1 + a[i][j];
                tmp2 = tmp2 + a[j][i];
            }
            all.push_back (tmp1);
            all.push_back (tmp2);
            tmp3 = tmp3 + a[i][i];
            tmp4 = tmp4 + a[i][BRRED - i - 1];
        }
        all.push_back (tmp3);
        all.push_back (tmp4);
        int result = 0;
        for (int i = 0; i < all.size (); i++) {
            int nemaT = 1;
            for (int j = 0; j < BRRED; j++) {
                if (all[i][j] == 'T') {
                    nemaT = 0;
                    all[i][j] = 'X';
                    result = max (result, check (all[i]));
                    all[i][j] = 'O';
                    result = max (result, check (all[i]));
                }
            }
            if (nemaT) {
                result = max (result, check (all[i]));
            }
        }
        printf ("Case #%d: ", t);
        if (result == 1) {
            printf ("Game has not completed\n");
        } else if (result == 0) {
            printf ("Draw\n");
        } else if (result == 2) {
            printf ("X won\n");
        } else {
            printf ("O won\n");
        }
	}
	return 0;
}
