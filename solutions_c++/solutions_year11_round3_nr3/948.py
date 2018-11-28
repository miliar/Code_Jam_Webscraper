/* 
 * File:   main.cpp
 * Author: Anton Boytsov
 *
 * Created on 21 Май 2011 г., 21:34
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <new>

using namespace std;

/*
 * 
 */

int t, n, l, h;
vector <int> mas;

int main() {

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    scanf("%d\n", &t);
    for (int q = 0; q < t; q++) {

        mas.clear();
        scanf("%d %d %d\n", &n, &l, &h);
        mas.resize(n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &mas[i]);
        }
        scanf("\n");
        
        int note = -1;
        for (int i = l; i <= h; i++) {
            bool f = true;
            for (int j = 0; j < n; j++)
                if (mas[j] % i != 0 && i % mas[j] != 0) {
                    f = false;
                    break;
                }
            if (f) {
                note = i;
                break;
            }
        } 
        printf ("Case #%d: ", q + 1);
        if (note == -1)
            printf ("NO\n");
        else
            printf ("%d\n", note);

    }


    return 0;
}

