#include <iostream.h>
#include <stdio.h>
#include <fstream.h>
#include <conio.h>

ifstream fi("C-small-attempt0.in");
ofstream fo("C-small-attempt0.out");

int t;
long long R, k, N;
int *v;

int main (void) {
fi>>t;

for (int i=1; i<=t; i++) {
    long long sum=0; long long val=0;
    fi>>R>>k;
    fi>>N;
    v=new int[N+1];

    for (int j=1; j<=N; j++) fi>>*(v+j);
   
    int m=1;
    int ind=1;
    int gr=0;
    while (m<=R) {
       sum+=*(v+ind);
       gr++;
       if (sum>k || gr>N) {
            val+=sum-*(v+ind);
            m++; sum=0; 
            gr=0;
            }
       else {ind++; if (ind>N) ind=1;}
    }
    fo<<"Case #"<<i<<": "<<val<<endl;
    free(v);
}
fi.close();
fo.close();
getch();

return 1;
}

   
