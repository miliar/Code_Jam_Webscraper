/*
Problem

The Snapper is a clever little device that, on one side, plugs its input plug into an output socket, and, on the other side, exposes an output socket for plugging in a light or other device.

When a Snapper is in the ON state and is receiving power from its input plug, then the device connected to its output socket is receiving power as well. When you snap your fingers -- making a clicking sound -- any Snapper receiving power at the time of the snap toggles between the ON and OFF states.

In hopes of destroying the universe by means of a singularity, I have purchased N Snapper devices and chained them together by plugging the first one into a power socket, the second one into the first one, and so on. The light is plugged into the Nth Snapper.

Initially, all the Snappers are in the OFF state, so only the first one is receiving power from the socket, and the light is off. I snap my fingers once, which toggles the first Snapper into the ON state and gives power to the second one. I snap my fingers again, which toggles both Snappers and then promptly cuts power off from the second one, leaving it in the ON state, but with no power. I snap my fingers the third time, which toggles the first Snapper again and gives power to the second one. Now both Snappers are in the ON state, and if my light is plugged into the second Snapper it will be on.

I keep doing this for hours. Will the light be on or off after I have snapped my fingers K times? The light is on if and only if it's receiving power from the Snapper it's plugged into.
Input

The first line of the input gives the number of test cases, T. T lines follow. Each one contains two integers, N and K.
Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is either "ON" or "OFF", indicating the state of the light bulb.
Limits

1 ¡Ü T ¡Ü 10,000.
Small dataset

1 ¡Ü N ¡Ü 10;
0 ¡Ü K ¡Ü 100;
Large dataset

1 ¡Ü N ¡Ü 30;
0 ¡Ü K ¡Ü 108; 

Input
  	
Output
 
4
1 0
1 1
4 0
4 47

Case #1: OFF
Case #2: ON
Case #3: OFF
Case #4: ON

*/

#include <iostream>
#include <string>
#include <memory>
#include <algorithm>
#include <vector>
#include <stdio.h>

using namespace std;

char* inFile = "A-large.in";
char* outFile = "xx22.txt";

int main()
{
    // read data
    FILE* in = fopen(inFile,"r");
    FILE* out = fopen(outFile,"w");

    int lineNum;
    fscanf(in,"%d",&lineNum);
    
    for(int i=0;i<lineNum;i++)
    {
        int N;
        unsigned int K;
        fscanf(in,"%d",&N);
        fscanf(in,"%ud",&K);
        unsigned int period=2<<(N-1);
        fprintf(out,"Case #%d: ",i+1);
        if((K+1)%period==0)
            fprintf(out,"ON",i+1);
        else
            fprintf(out,"OFF",i+1);
        fprintf(out,"\n",i+1);
    }

    // write data and close
    fclose(in);
    fclose(out);

    return 0;
}