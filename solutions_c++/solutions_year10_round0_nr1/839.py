#include <iostream>
#include <cstdio>

using namespace std;

#define ll long long

FILE *fin = fopen ("A-large.in","r");
FILE *fout = fopen ("A-large.out","w");
int main () {
    int T,N,K;
    ll power2[31]; 
    power2[0] = 1;
    for (int i = 1;i<31;++i)
        power2[i]=power2[i-1]*2;
    fscanf (fin,"%d",&T);
    for (int i = 0;i<T;++i) {
        fscanf (fin, "%d %d", &N,&K);
        bool res = (K%power2[N]) == power2[N]-1;
        if (res) fprintf (fout,"Case #%d: ON\n",i+1);
        else fprintf (fout, "Case #%d: OFF\n",i+1);
    }
    return 0;   
}
