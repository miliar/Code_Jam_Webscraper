#include <algorithm>
#include <iostream>
#include <sstream>
#include <string.h>
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
int t;

int main(){
    scanf("%d",&t);
    for (int c=0;c<t;c++){
        int n;
        char b[1000];
        int p[1000];
        scanf("%d",&n);
        for (int i=0;i<n;i++){
            scanf(" %c %d",&b[i],&p[i]);
            }
        int prevto=0;
        int prevlo=1;
        int prevlb=1;
        int prevtb=0;
        int fint=0;
        for (int i=0;i<n;i++){
            if (b[i]=='O'){
                int t=abs(prevlo-p[i]);
                fint=max(t+prevto,fint)+1;
                prevlo=p[i];
                prevto=fint;
                }
            if (b[i]=='B'){
                int t=abs(prevlb-p[i]);
                fint=max(t+prevtb,fint)+1;
                prevlb=p[i];
                prevtb=fint;
                }
            }
        printf("Case #%d: %d\n",c+1,fint);
        }
    return 0;
    }
