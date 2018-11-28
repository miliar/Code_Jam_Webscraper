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

    FILE *ff=fopen("B-large.in", "r"), *gg=fopen("B-large.out", "w");

    int n,s,p,q,w,i,x,tt,ttt,res;

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {

        fscanf(ff,"%d%d%d", &n, &s, &p);

        q=0; w=0; res=0;
        for(i=0; i<n; i++) {
            fscanf(ff,"%d", &x);
            if ((x+2)/3 >= p) res++;
            else if ((x+4)/3 >= p && x>0) q++;
        }

        res+=min(q,s);

        fprintf(gg,"Case #%d: %d\n", tt, res);
    }

    fclose(ff); fclose(gg);

    return 0;
}
