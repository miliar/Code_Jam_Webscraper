#include <iostream.h>
#include <fstream.h>
#include <stdio.h>
#include <math.h>
#include <conio.h>

ifstream fi("A-large.in");
ofstream fo("A-large.out");

long long t;

int main (void) {
fi>>t;
for (long long i=1; i<=t; i++) {
    int n=0; long long k=0; long long nr=0; 
    fi>>n; fi>>k;
    nr=(long long)pow(2, n);
    if (k%nr==(nr-1)) fo<<"Case #"<<i<<": ON"<<endl;
    else fo<<"Case #"<<i<<": OFF"<<endl;   
}
fi.close();
fo.close();
getch();
return 1;    
}
