#include <cstdlib>
#include<iostream>
#include<time.h>
#include<stdlib.h>
#include<vector>
#include<limits.h>
#include<float.h>
#include <iostream>
#include <fstream>
#include <map>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int T;
    int S;
    int N;
    int P;

    FILE * pFile;
    FILE * wFile;
    pFile = fopen ("B-small-attempt0.in","r");
    wFile = fopen ("out2.txt","w");

    fscanf (pFile, "%d", &T);
    
    for(int i=0;i<T;i++){
        fscanf (pFile, "%d %d %d ", &N,&S,&P);
        int t[N];
        for(int j=0;j<N;j++){
            fscanf(pFile,"%d ",&t[j]);
        }

    int cnt=0;
    int div, rem;
    for(int j=0;j<N;j++){
        div = t[j]/3;
        rem = t[j]%3;
        if(div>=P){
            cnt++;
        }
        else if (div==P-1){
            if(rem==0 ){
                if (S>0 && div-1>=0 &&div+1<=10){
                    S--;
                    cnt++;
                }
            } else {
                cnt++;
            }
        } else if (div==P-2){
            if (rem==2){
                if (S>0 && div-1>=0 &&div+1<=10 ){
                    S--;
                    cnt++;
                }
            }
        }
        
    }

    fprintf(wFile,"Case #%d: %d\n",i+1,cnt);
    } // for each test case
fclose(pFile);
fclose(wFile);

}


