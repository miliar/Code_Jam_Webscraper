/* 
 * File:   main.cpp
 * Author: Anton Boytsov
 *
 * Created on 7 Май 2011 г., 16:04
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

using namespace std;

/*
 * 
 */

int n;

vector < pair <string, int> > ar;
vector <int> orn, bl;

int step(int cpos, int nxpos) {


    return (abs(cpos - nxpos) + 1);

}

int solve(vector < pair <string, int> > ar) {

    int time = 0, cur = 0;
    int posorn = 1, exorn = 0;
    int posbl = 1, exbl = 0;

    while (cur < ar.size()) {

        int sm1 = 0, sm2 = 0;
        while (cur < ar.size() && (cur == 0 || ar[cur].first == ar[cur - 1].first)) {

            if (ar[cur].first == "O") {
                sm1 += step(posorn, ar[cur].second);
                posorn = ar[cur].second;
            } else {
                sm1 += step(posbl, ar[cur].second);
                posbl = ar[cur].second;
            }
            cur++;

        }
        if (cur == ar.size())
            time += sm1;
        else {
            if (ar[cur].first == "O") {
                sm2 = step(posorn, ar[cur].second);
                posorn = ar[cur].second;
                if (sm2 - exorn > sm1) {
                    time += (sm2 - exorn);
                    exbl = sm2 - exorn - sm1 + 1;
                } else {
                    time += (sm1 + 1);
                    exbl = 1;
                }
                exorn = 0;
            } else {
                sm2 = step(posbl, ar[cur].second);
                posbl = ar[cur].second;
                if (sm2 - exbl > sm1) {
                    time += (sm2 - exbl);
                    exorn = sm2 - exbl - sm1 + 1;
                } else {
                    time += (sm1 + 1);
                    exorn = 1;
                }
                exbl = 0;
            }
        }
        cur++;


    }



    return time;

}

void go(int & pos, int & nx) {
    if (pos > nx)
        pos--;
    else if (pos < nx)
        pos++;
}

int solve2(vector < pair <string, int> > ar, vector <int> orn, vector <int> bl) {

    int posorn = 1, posbl = 1;
    int corn = 0, cbl = 0, car = 0;
    int time = 0;


    while (corn < orn.size() || cbl < bl.size()) {

        if (ar[car].first == "O") {

            if (ar[car].second == posorn) {
                car++;
                corn++;
                if (cbl < bl.size())
                    go(posbl, bl[cbl]);
            } else {
                if (corn < orn.size())
                    go(posorn, orn[corn]);
                if (cbl < bl.size())
                    go(posbl, bl[cbl]);
            }

        } else {

            if (ar[car].second == posbl) {
                car++;
                cbl++;
                if (corn < orn.size())
                    go(posorn, orn[corn]);
            } else {
                if (corn < orn.size())
                    go(posorn, orn[corn]);
                if (cbl < bl.size())
                    go(posbl, bl[cbl]);
            }

        }

        time++;

    }

    return time;

}

int main() {

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    cin >> n;
    for (int i = 0; i < n; i++) {

        int k;
        cin >> k;
        ar.clear();
        ar.resize(k);
        orn.clear();
        bl.clear();
        for (int i = 0; i < k; i++) {
            cin >> ar[i].first;
            cin >> ar[i].second;
            if (ar[i].first == "O")
                orn.push_back(ar[i].second);
            else
                bl.push_back(ar[i].second);
        }
        cout << "Case #" << (i + 1) << ": " << solve2(ar, orn, bl) << endl;

    }

    return 0;
}

