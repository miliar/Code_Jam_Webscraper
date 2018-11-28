/*
 * Author: xg1990
 * Created Time:  2010-5-8 15:47:24
 * File Name: gcja.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

int main() {
    freopen("A-large.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    
    long long t,tt,n,k;
    scanf("%I64d",&t);
    tt=0;
    while(tt++<t){
        scanf("%I64d%I64d",&n,&k);
        printf("Case #%I64d: ",tt);
        if((k+1)%(1<<n)==0)printf("ON\n");
        else printf("OFF\n");
    }
    
    return 0;
}


