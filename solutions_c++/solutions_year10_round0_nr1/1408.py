/* 
 * File:   main.cpp
 * Author: Tim
 *
 * Created on 07 May 2010, 22:04
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "Solver.h"

/*
 * 
 */

bool Solve(int n, int k)
{
    bool bOn = true;
    while ( n > 0)
    { 
        n--;
        int mask = (1 << n);

        bOn = bOn && (mask & k) > 0;
    }
    return bOn;
}

int main(int argc, char** argv)
{
    int T = 0;
    scanf("%d", &T);

    //FILE *fout = fopen("out.txt", "w");
    for (int t = 1; t <= T; t++)
    {
        int n, k;
        scanf("%d %d", &n, &k);

        bool b = Solve(n, k);
        
        printf("Case #%d: %s\n", t, b ? "ON" : "OFF");
        //fprintf(fout, "Case #%d: %s\n", t, b ? "ON" : "OFF");
    }

    return (EXIT_SUCCESS);
}
