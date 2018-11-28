//
//  main.cpp
//  Codejam2011Cmd
//
//  Created by Jirasak Chirathivat on 5/7/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//
#include <iostream>

using namespace std;
int main (int argc, const char * argv[])
{
    FILE *fIn = fopen("in.txt", "r");
    int count;
    fscanf(fIn, "%d", &count);
    for(int i = 0; i < count; ++i)
    {
        int N;
        int sum = 0;
        int oIndex = 1;
        int lastOPeriod = 0;
        int bIndex = 1;
        int lastBPeriod = 0;
        
        fscanf(fIn, "%d ", &N);
        for(int j = 0; j < N; ++j) {
            char R;
            int P;
            fscanf(fIn, "%c %d ", &R, &P);
//            cout << R << endl;
//            cout << P << endl;
//            cout << "j is " << j << endl;
            
            if(R == 'O') {
                int rounds;
                
                if(sum == lastOPeriod)
                    rounds = abs(oIndex - P);
                else
                    rounds = (abs(oIndex - P) - (sum - lastOPeriod));
                
                if(rounds <= 0)
                    sum+=1;
                else
                    sum+=rounds+1;
                lastOPeriod = sum;
                oIndex = P;
            }
            else {
                int rounds;
                
                if(sum == lastBPeriod)
                    rounds = abs(bIndex - P);
                else
                    rounds = (abs(bIndex - P) - (sum - lastBPeriod));
                
                if(rounds <= 0) {
                    sum+=1;
                }
                else {
                    sum+=rounds+1;
                }
                lastBPeriod = sum;
                bIndex = P;
            }
        }
        printf("Case #%d: %d\n", i+1, sum);  
    }
    fclose(fIn);
    return 0;
}
