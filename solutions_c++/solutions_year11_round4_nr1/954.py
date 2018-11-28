#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

typedef struct{
        int dist;
        int speed;
} n;

vector<n> v;

bool operator < (n a, n b){
     return a.speed < b.speed;
}

main() {
       int T,tc,X,S,R,N,B,E,w,extra,sp;
       n s;
       double t;
       FILE *in = fopen("A-large.in","r");
       FILE *out = fopen("A-large.out","w");
       fscanf(in,"%d",&T);
       for(int tc=1;tc<=T;tc++) {
               v.clear();
               fscanf(in,"%d %d %d %lf %d",&X,&S,&R,&t,&N);
               double tot = 0;
               int without = X;
               for(int i=0;i<N;i++){
                       fscanf(in,"%d %d %d",&B,&E,&w);
                       without -= (E-B);
                       s.dist = (E-B);
                       s.speed = w+S;
                       tot += ((double)(E-B)/(double)(S+w));
                       v.push_back(s);
               }
               s.dist = without;
               s.speed = S;
               v.push_back(s);
               sort(v.begin(),v.end());
               tot +=(double)(without)/(double)S; 
               for(int i=0;i<v.size()&&t;i++){
                       sp = v[i].speed-S+R;
                       if(sp*t<v[i].dist){
                              tot -= (double)((double)(t*sp)/(double)v[i].speed)-(double)t;
                              t = 0;
                       } else {
                              tot -= ((double)v[i].dist/(double)v[i].speed)-((double)v[i].dist/(double)sp);
                              t -= (double)v[i].dist/(double)sp;
                       }
               }
               fprintf(out,"Case #%d: %0.12lf\n",tc,tot);
               fprintf(stdout,"Case #%d: %0.12lf\n",tc,tot);
       }
       fclose(out);
       system("PAUSE");
}
