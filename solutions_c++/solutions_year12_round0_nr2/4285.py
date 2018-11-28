//
//  DancingGoogle.cpp
//  
//
//  Created by Cheng Lung-Pan on 12/4/14.
//  Copyright (c) 2012年 NTU MHCI Lab. All rights reserved.
//

#include <iostream>
#include <stack>

using namespace std;

int T;
int main(){
    FILE * file;
    file = fopen ("B-large.in","r");
    fscanf(file,"%d", &T );
    for (int i=0; i<T; i++) {
        int N;
        int S;
        int p;
        fscanf(file,"%d", &N);
        fscanf(file,"%d", &S);
        fscanf(file,"%d", &p);
        int* scoles = new int[N];
        int count = 0;
        for (int j= 0; j<N; j++) {
            fscanf(file,"%d", scoles+j);
            if (scoles[j]/3>=p){
             count++;
            }
            else{
                int r = scoles[j]%3;
                switch(r){
                    case 0:
                        if (scoles[j]/3 == p-1 && scoles[j]!=0)
                        {
                            if(S>0) count++;
                            S--;
                        }
                        break;
                    case 1:
                        if (scoles[j]/3 == p-1) count++;
                        break;
                    case 2:
                        if (scoles[j]/3 == p-1) count++;
                        if (scoles[j]/3 == p-2){
                            if(S>0) count++;
                            S--;
                        }
                        break;
                    default:
                        break;
                }
            }
        }
        printf("Case #%d: %d\n",i+1, count);

        delete[] scoles;
    }
}