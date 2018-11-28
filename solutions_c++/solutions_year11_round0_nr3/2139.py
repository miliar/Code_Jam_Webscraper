/* 
 * File:   main.cpp
 * Author: Anton Boytsov
 *
 * Created on 7 Май 2011 г., 19:10
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

const int MAXA = 1000 * 1000;

int n;

int main() {

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    cin >> n;

    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        int mn = MAXA + 1;
        int sum = 0, xsum = 0, a = 0;
        for (int j = 0; j < k; j++) {
            cin >> a;
            if (a < mn)
                mn = a;
            sum = sum + a;
            xsum = xsum ^ a;
        }
        if (!xsum)
            cout << "Case #" << (i + 1) << ": " << sum - mn << endl;
        else
            cout << "Case #" << (i + 1) << ": NO" << endl;
    }

    return 0;
}

