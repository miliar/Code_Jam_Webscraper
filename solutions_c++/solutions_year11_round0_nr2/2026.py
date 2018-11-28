/* 
 * File:   main.cpp
 * Author: Anton Boytsov
 *
 * Created on 7 Май 2011 г., 19:54
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <stack>

using namespace std;

/*
 * 
 */

int n, c, d, len;

char comb[500][500];
bool opp[500][500];

int main() {

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    cin >> n;
    vector <char> mm;

    for (int i = 0; i < n; i++) {


        memset(opp, false, sizeof (opp));
        memset(comb, 0, sizeof (comb));
        cin >> c;
        for (int j = 0; j < c; j++) {
            string st;
            cin >> st;
            comb[st[0]][st[1]] = st[2];
            comb[st[1]][st[0]] = st[2];
        }
        cin >> d;
        for (int j = 0; j < d; j++) {
            string st;
            cin >> st;
            opp[st[0]][st[1]] = true;
            opp[st[1]][st[0]] = true;
        }
        cin >> len;
        string st;
        cin >> st;
        mm.clear();
        for (int j = 0; j < len; j++) {

            if (mm.size()) {

                bool ff = true;
                if (int(comb[st[j]][mm[mm.size() - 1]]) != 0) {
                    mm[mm.size() - 1] = comb[st[j]][mm[mm.size() - 1]];
                    for (int q = 0; q < int(mm.size()-1); q++)
                        if (opp[mm[q]][mm[mm.size()-1]]) {
                            ff = false;
                            mm.clear();
                            break;
                        }
                } else {
                    for (int q = 0; q < mm.size(); q++)
                        if (opp[mm[q]][st[j]]) {
                            ff = false;
                            mm.clear();
                            break;
                        }
                    if (ff) {
                        mm.push_back(st[j]);
                    }
                }

            } else {
                mm.push_back(st[j]);
            }

        }

        cout << "Case #" << i + 1 << ": [";
        for (int j = 0; j < int(mm.size() - 1); j++)
            cout << mm[j] << ", ";
        if (int(mm.size() - 1) >= 0)
            cout << mm[mm.size() - 1];
        cout << "]" << endl;
        mm.clear();


    }


    return 0;
}

