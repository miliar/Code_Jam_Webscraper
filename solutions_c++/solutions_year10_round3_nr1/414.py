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
FILE *f = fopen("C:\\A-large(3).in", "rt"); //A-small-attempt2.in
FILE *f1= fopen("C:\\output.txt", "wt");
int main(){
    int t,T;
    fscanf(f,"%d",&t);
    T=t;
    while (t-->0){
        int n;
        fscanf(f,"%d",&n);
        int a[2000];
        int b[2000];
        for (int i=0;i<n;i++){
            fscanf(f,"%d %d",&a[i],&b[i]);
            }
        int st=0;
        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++) if (a[i]>a[j]&&b[i]<b[j]) st++;
            }
         fprintf(f1,"Case #%d: %d\n",T-t,st);
         }
     fclose(f);fclose(f1);
    return 0;
    }
