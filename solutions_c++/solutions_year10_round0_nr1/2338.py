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
FILE *f = fopen("C:\\A-large.in", "rt"); //A-small-attempt2.in
FILE *f1= fopen("C:\\output.txt", "wt");
int main(){
    int t;
    fscanf(f,"%d",&t);
    int T=t;
    while (t-->0){
    long long s;
    int n,k;
    fscanf(f,"%d %d",&n,&k);
    k=k%(1<<n);

    if ((k+1==(1<<n))) fprintf(f1,"Case #%d: ON\n",T-t); else fprintf(f1,"Case #%d: OFF\n",T-t);
    }
    fclose(f);fclose(f1);
    return 0;
    }
