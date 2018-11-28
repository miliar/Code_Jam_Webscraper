//
//  main.cpp
//  GoogleCodeJam_B
//
//  Created by Witzy Huang on 12-4-14.
//  Copyright (c) 2012年 SinoSoft. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <memory.h>
#include <fstream>
#include <memory.h>
using namespace std;
#define MAXN 101
int T;
int N;
int S;
int P;

int Ti[MAXN];

bool Used[MAXN];
int solve(){
    if (P==0) {
        return N;
    }
    memset(Used, 0, sizeof(Used));
    int ngp=0;//number of goolers that score greater than p
    
    for (int i=0; i<N; i++) {
        if (Ti[i]>3*(P-1)) {//ti/3>p-1,means at least one score >=p when has no suprise
            ngp++;
            Used[i]=true;
        }
    }
    int ns=0;//number of superise
    for (int i=0; i<N && ns<S; i++) {
        if (!Used[i]) {
            if (Ti[i]>0 && Ti[i]>=3*(P-2)+2) {//ti=a+a+a+2 && a+2>=p
                ngp++;
                ns++;
            }
        }
    }
    return ngp;
}
int main (int argc, const char * argv[])
{

    ifstream fin("B-large.in");
    ofstream fout("output.txt");
    
    fin>>T;
    for (int caseIndex=1; caseIndex<=T; caseIndex++) {
        
        fin>>N>>S>>P;
        for (int i=0; i<N; i++) {
            fin>>Ti[i];
        }
        cout<<"Case #"<<caseIndex<<": "<<solve()<<endl;

        fout<<"Case #"<<caseIndex<<": "<<solve()<<endl;
    }
    return 0;
}

