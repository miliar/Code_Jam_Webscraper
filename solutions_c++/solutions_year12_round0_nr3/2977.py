//
//  main.cpp
//  GoogleCodeJam_C
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
int A;
int B;


int DigitsB[7];
int Digits[7];
int Digitst[7];
int move(int val,int moveCount){
    int ls=0,ft=0;
    int base=1;
    for (int i=0; i<moveCount; ++i) {
        ft+=val%10*base;
        val/=10;
        base*=10;
    }
    base=1;
    while (val>0) {
        ls+=val%10*base;
        val/=10;
        ft*=10;
        base*=10;
    }
    return ft+ls;
}
int solve(){
    if (A>B) {
        return 0;
    }
    int bi=0;
    int tmp=B;
    int bh=1;
    while (tmp>0) {
        DigitsB[bi++]=tmp%10;
        tmp/=10;
        bh*=10;
    }
    bh/=10;

    int i=0;
    int cnt=bh-A;
    if (cnt>0) {
        A=bh;
    }else{
        cnt=0;   
    }
    
    for (int val=A; val<=B; val++) {
        i=0;
        tmp=val;
        while (tmp>0) {
            Digits[i++]=tmp%10;
            tmp=tmp/10;
        }
        for (int j=1; j<i; j++) {
            for (int l=0; l<i; l++) {
                Digitst[l]=Digits[(j+l)%i];
            }
            bool lessThanB=false;
            for (int l=i-1; l>=0; --l) {
                if (Digitst[l]<DigitsB[l]) {
                    lessThanB=true;
                    break;
                }else if(Digitst[l]>DigitsB[l]){
                    lessThanB=false;
                    break;
                }
            }
            bool greaterThanVal=false;
            for (int l=i-1; l>=0; --l) {
                if (Digitst[l]>Digits[l]) {
                    greaterThanVal=true;
                    break;
                }else if(Digitst[l]<Digits[l]){
                    greaterThanVal=false;
                    break;
                }
            }
            if (lessThanB && greaterThanVal) {
                cnt++;
            }
        }
    }
    return cnt;
}

int dgt(int val){
    int d=0;
    while (val>0) {
        val/=10;
        d++;
    }
    return d;
}
int solve1(){
    if (A>=B) {
        return 0;
    }
    int cnt=0;

    for (int i=A; i<B; i++) {

        int dgct=dgt(i);
        int val=0;
        for (int j=1; j<dgct; ++j) {
            val=move(i, j);
            if (val>i && val<=B) {
                cnt++;
            }
        }
        
    }
    return cnt;
}
int main (int argc, const char * argv[])
{

    
    ifstream fin("C-small-attempt0.in");
    ofstream fout("output.txt");
    
    fin>>T;
    
    for (int caseIndex=1; caseIndex<=T; caseIndex++) {
        
        fin>>A>>B;
        fout<<"Case #"<<caseIndex<<": "<<solve1()<<endl;
    }
    
    return 0;
}

