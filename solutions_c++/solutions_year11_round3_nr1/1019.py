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


char mas[200][200];
int t, r, c;


int main() {

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif


    scanf("%d\n", &t);
    for (int q = 0; q < t; q++) {

        memset(mas, 0, sizeof (mas));

        scanf("%d %d\n", &r, &c);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++)
                scanf("%c", &mas[i][j]);
            scanf("\n");
        }

        int f = 0;
        while (!f) {
            f = 1;
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++)
                    if (mas[i][j] == '#') {
                        
                        if (i + 1 >= r && j + 1 >= c) {
                            f = 2;
                            break;
                        }
                        
                        if (mas[i + 1][j] != '#' || mas[i][j + 1] != '#' || mas[i + 1][j + 1] != '#') {
                            f = 2;
                            break;
                        }
                        
                        mas[i][j] = '/';
                        mas[i][j + 1] = '\\';
                        mas[i + 1][j] = '\\';
                        mas[i + 1][j + 1] = '/';
                        f = 0;

                    }
                if (f == 2)
                    break;
            }
        }
        
        printf ("Case #%d:\n", q + 1);
        if (f == 2) {
            printf("Impossible\n");
        } else {
            
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++)
                    printf ("%c", mas[i][j]);
                printf ("\n");
            }
            
        }

    }

    return 0;
}

