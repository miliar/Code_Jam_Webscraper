/* 
 * File:   main.cpp
 * Author: paulo
 *
 * Created on 14 de Abril de 2012, 01:33
 */

#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
    return *(int *)b - *(int *)a;
}


/*
 * 
 */
int main(int argc, char** argv) {
    // REads the cases number
    int cases;
    scanf("%d", &cases);
    // The googlers vector
    int googlers[100];
    // For each case, does the test
    for(int i=0;i<cases;i++)
    {
        // The number used
        int N, S, p, temp;
        // REads the number of Googlers
        scanf("%d", &N);
        // REads the surprising scores
        scanf("%d", &S);
        // Reads the minimum score
        scanf("%d", &p);
        // Reads the Googlers scores and gets the maximum possible score for each
        for(int j=0;j<N;j++)
        {
            scanf("%d", &temp);
            // calculates the minimum score
            googlers[j] = temp/3;
            // checks if at leas a judge gave a different score than the others
            if(temp%3)
                googlers[j] += 1;
        }
        // sorts the googlers scores
        qsort(googlers, N, sizeof(int), &compare);
        // Gets the scores
        int scores=0, surprises=0;
        for(int j=0;j<N;j++)
        {
            // If the score is at least p
            if(googlers[j]>=p)
                scores++;
            else
            {
                // Otherwise, if it is smaller, tries to increase it to see if it gets there
                if(surprises<S && googlers[j] > 0)
                {
                    surprises++;
                    googlers[j]+=1;
                    if(googlers[j]>=p)
                        scores++;
                }
            }
        }
        printf("Case #%d: %d\n", i+1, scores);
    }
    return 0;
}

