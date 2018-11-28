#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstdlib>

using namespace std;

typedef pair<string,int> INS;
INS seq[200];
INS O[200];
INS B[200];
int sign(int n)
{
    return n<0?(-1):(1);
}
int ABS(int n)
{
    return n*sign(n);
}
int MIN(int a,int b)
{
    return (ABS(a)<ABS(b))?(a):(b);
}
int main(int argc, char** argv) 
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int TC;
    cin>>TC;
    for(int tc = 1; tc<=TC; ++tc)
    {
        int N;
        cin>>N;
        int io=0,ib=0;
        for(int i = 0; i < N; ++i)
        {
            cin>>seq[i].first>>seq[i].second;
            if(seq[i].first=="O")
                O[io++] = seq[i];
            else
                B[ib++] = seq[i];
        }
        int nio = 0, nib = 0;
        int po = 1, pb = 1;
        int S = 0;
        for(int i = 0; i < N; ++i)
        {
            int dO = O[nio].second - po;
            int dB = B[nib].second - pb;
            if(seq[i]==O[nio])//move the orange
            {
                pb += MIN(dB,sign(dB)*(ABS(dO)+1));
                po += dO;
                S += ABS(dO)+1;
                nio++;
            }else{//move the blue one
                pb += dB;
                po += MIN(dO,sign(dO)*(ABS(dB)+1));
                S += ABS(dB)+1;
                nib++;
            }
        }
        printf("Case #%d: %d\n",tc,S);
    }
    
    return 0;
}



/* 
 * File:   A.cpp
 * Author: Carlos
 *
 * Created on May 6, 2011, 10:22 PM
 */
