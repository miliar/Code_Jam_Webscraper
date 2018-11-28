//
//  main.cpp
//  CodeJam1
//
//  Created by SETLPERV on 28/04/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>

int main (int argc, const char * argv[])
{
    int number,a,b;
    double maxprob=1.0;
    scanf("%d",&number);
    double prob[100000];
    double result,tempresult;
    double wrongprob;
    double rightprob;
    int rightkeystrokes;
    int wrongkeystrokes;
    
    for (int i=0;i<number;i++) {
        scanf("%d",&a);
        scanf("%d",&b);
        
        for (int j=0;j<a; j++) {
            scanf("%lf",&prob[j]);
            //printf("%f",prob[j]);
            maxprob = maxprob*prob[j];
        }
        
        // 1
        rightprob = maxprob;
        wrongprob = 1 - maxprob;
        rightkeystrokes = (b-a)+1;
        wrongkeystrokes = rightkeystrokes +b +1;
        result = rightkeystrokes *rightprob + wrongkeystrokes *wrongprob;
        
        //2
        int backspace=0;
        for (int k= a-1; k>=0; k--) {
            backspace++;
            rightprob = rightprob / prob[k];
            wrongprob = 1 - rightprob;
            rightkeystrokes = backspace*2 + (b-a) + 1;
            wrongkeystrokes = rightkeystrokes + b + 1;
            tempresult = rightprob *rightkeystrokes + wrongprob *wrongkeystrokes;
            if (tempresult < result) {
                result = tempresult;
            }
        }
        
    
        //3
        tempresult = b +2;
        if (tempresult < result) {
            result = tempresult;
        }
            
        printf("Case #%d: %f\n",i+1,result);
        maxprob = 1;
        
    }
    
    
}

