#include<stdio.h>
#include<vector>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

#define sz size()
#define pb push_back
#define len length()
#define clr clear()

#define eps 0.0000001
#define PI  3.14159265359

int main() {

    FILE *ff=fopen("C-small-attempt0.in", "r"), *gg=fopen("C-small-attempt0.out", "w");

    int ttt,tt,n,i,res,l,a1,a2,s,j,a[55];

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {
        fscanf(ff,"%d", &n);
        for(i=0; i<n; i++) fscanf(ff,"%d", &a[i]);

        res=-1;
        l=1<<n;
        for(i=1; i<l-1; i++) {
           a1=0; a2=0; s=0;
           for(j=0; j<n; j++) if (i&(1<<j)) {
               s+=a[j];
               a1=a1^a[j];
           } else {
               a2=a2^a[j];
           }
           if (a1==a2 && s>res) res=s;
        }

        if (res==-1) fprintf(gg,"Case #%d: NO\n", tt);
        else fprintf(gg,"Case #%d: %d\n", tt, res);
    }

    fclose(ff); fclose(gg);

    return 0;
}
