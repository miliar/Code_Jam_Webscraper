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
// Code Jam B
int main(){
    int t,T;
    scanf("%d",&t);
    T=t;
    while (t-->0){
        int res=0;
        int p;
        scanf("%d",&p);
        int m[2000];
        for (int i=0;i<1<<p;i++) scanf("%d",&m[i]);
        int b;
        for (int i=0;i<(1<<p)-1;i++) scanf("%d",&b);
        int st=0;
        int a[3000];
        for (int i=0;i<1<<(p+1);i++) a[i]=0;
        int c=1<<p;
        for (int i=0;i<1<<p;i++){
             int tr=i+c;
             for (int j=1;j<=p;j++){
                 tr=tr/2;
                 if (j>m[i]) a[tr]=1;
                 }
            }
        for (int i=0;i<1<<p;i++) res=res+a[i];
        printf("Case #%d: %d\n",T-t,res);
        }
    return 0;
    }
