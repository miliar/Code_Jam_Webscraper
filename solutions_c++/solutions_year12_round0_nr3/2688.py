/* 
 * File:   main.cpp
 * Author: paulo
 *
 * Created on 13 de Abril de 2012, 23:26
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

/*
 * 
 */
int main(int argc, char** argv) {

    // Gets the number of cases
    int cases;
    scanf("%d", &cases);
    for(int i=0;i<cases;i++)
    {
        int A, B;
        // Gets the numbers
        scanf("%d %d", &A, &B);
        // Count the number of recycled numbers
        int count=0;
        // Tests the interval
        for(int n=A;n<B;n++)
        { 
            int digits[7];
            // How many digits number n has
            int cd = 0;
            int temp=n;
            // Which was the las last digit different than 0
            int last=-1;
            // Gets the digits the quick'n'dirty way
            for(int j=0;j<7;j++)
            {
                // Gets the last digit
                digits[j] = temp%10;
                if(digits[j])
                    last=j+1;
                // Removes the last digit and rotates the number to the right
                temp/=10;
                //printf("%d ", digits[j]);
            }
            //printf("\n");
            // Now gets the first j digits and move them to the end of the number to find m
            int used[7];
            int numUsed=0;
            for(int j=0;j<last;j++)
            {
                int m=0;
                for(int k=0;k<last;k++)
                    m+=(int)pow(10,k)*digits[(j+k)%last];
                // Checks if m was already used for this number
                int wasUsed=0;
                for(int i=0;i<numUsed;i++)
                    if(used[i]==m)
                        wasUsed=-1;
                if(m>n && A <= n && m <= B && !wasUsed)
                {
                    used[numUsed++]=m;
                    //printf("(%d, %d)\n", n,m);
                    count++;
                }
            }
            
            
        }
        printf("Case #%d: %d\n", i+1, count);
    }
    return 0;
}

