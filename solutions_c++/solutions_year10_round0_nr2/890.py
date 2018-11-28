#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <vector>
#include <map>
#include <math.h>
#include <stdio.h>
using namespace std;
// ne da se mi
FILE *f = fopen("C:\\B-small-attempt1.in", "rt");
FILE *f1= fopen("C:\\output.txt", "wt");

int gcd(int a,int b){
    while (b!=0){
        int v=b;
        b=a%b;
        a=v;
    }
    return a;
    }
int t[1000];
int main(){
    int c;
    fscanf(f,"%d",&c);
    int C=c;
    while (c-->0){
        int n;
        fscanf(f,"%d",&n);
        for (int i=0;i<n;i++) fscanf(f,"%d",&t[i]);
        int res=abs(t[1]-t[0]);
        for (int i=2;i<n;i++) res=gcd(res,abs(t[i]-t[i-1]));
        if (t[0]%res==0) res=0; else res=((t[0]/res)+1)*res-t[0];
        fprintf(f1,"Case #%d: %d\n",C-c,res);

        }
    fclose(f);fclose(f1);
    return 0;
    }
