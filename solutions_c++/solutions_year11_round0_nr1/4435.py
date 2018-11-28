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

    FILE *ff=fopen("A-large.in", "r"), *gg=fopen("A-large.out", "w");

    int i,p1,p2,t,res,n,tt,ttt,a[555];
    char cc,o[555];

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {

        fscanf(ff,"%d ", &n);
        for(i=0; i<n; i++) {
            if (i>0) fscanf(ff," ");
            fscanf(ff,"%c %d", &o[i], &a[i]);;
        }
        cc=o[0];
        p1=1; p2=1;
        i=0; res=0; t=0;
        while( i<n ) {
            //printf("-> %d %d %d\n", res, t, abs(a[i]-p1));

            if ( abs(a[i]-p1) > t ) {
                //res+=abs(a[i]-p1)-t;
                t=abs(a[i]-p1)-t;
            } else t=0;
            p1=a[i]; i++;
            //printf("~%d\n", t);

            t++;
            while( i<n && o[i]==cc ) {
               t+=abs(a[i]-p1);
               p1=a[i];
               t++;
               i++;
            }
            res+=t;

            //printf("---> %d\n", res);

            if (i<n) {
               if( abs(a[i]-p2) > t ) {
                   //res=res+(abs(a[i]-p2))-t;
                   t=(abs(a[i]-p2))-t;
               } else t=0;
               p2=a[i]; i++;

                t++;
                while( i<n && o[i]!=cc ) {
                    t+=abs(a[i]-p2);
                    p2=a[i];
                    t++;
                    i++;
                }
                res+=t;
            }
        }

        fprintf(gg,"Case #%d: %d\n", tt, res);

    }

    fclose(ff); fclose(gg);

    return 0;
}
