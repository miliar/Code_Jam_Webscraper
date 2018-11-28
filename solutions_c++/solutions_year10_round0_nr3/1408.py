/* 
 * File:   main.cpp
 * Author: Tim
 *
 * Created on 08 May 2010, 01:26
 */

#include <stdlib.h>
#include <stdio.h>

int solve(int R, // # rides per day
        int k, // Capacity
        int N, // # groups in queue
        int *g)
{
    int y = 0; // start with no money
    int i = 0; // start at beginning of queue
    
    // run each ride
    for (int r = 0; r < R; r++)
    {
        int c = 0; // # people on board

        const int i0 = i; // remember the end of the queue

        // while we can still fit the next group on, and the queue is not empty
        bool bPeopleInQueue = true;
        while (c + g[i] <= k && bPeopleInQueue)
        {
            // take payment
            y += g[i];

            // let the group on
            c += g[i];

            // move to next group
            i = (i + 1) % N;
            
            bPeopleInQueue = i != i0;
        }
    }
    return y;
}

/*
 * 
 */
int main(int argc, char** argv) {

    int Tests;
    scanf("%d", &Tests);

    int g[1024];
    for (int test = 1; test <= Tests; test++)
    {
        int R, k, N;
        scanf("%d %d %d", &R, &k, &N);
        
        for (int i = 0; i < N; i++)
        {
            scanf("%d", &g[i]);
        }
        
        int y = solve(R, k, N, g);
        
        printf("Case #%d: %d\n", test, y);
    }

    return (EXIT_SUCCESS);
}

