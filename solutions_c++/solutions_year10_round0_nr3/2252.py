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
int g[3000];
int c[3000];
int d[3000];
int p[3000];
int b[3000][2]; // b[i][0]... pove èe je že bila najdena b[i][1]... pove ob katerm èasu je bila najdena
FILE *f = fopen("C:\\C-small-attempt0.in", "rt");
FILE *f1= fopen("C:\\output.txt", "wt");
int main(){
    int t1;
    fscanf(f,"%d",&t1);
    int t2=t1;
    while (t1-->0){
       int r,k,n;
       fscanf(f,"%d %d %d",&r,&k,&n);
       for (int i=0;i<n;i++) fscanf(f,"%d",&g[i]);
       //za vsako lokacijo naraèunamo koliko po njej uzamemo
       for (int i=0;i<n;i++){
           int d1=0;
           c[i]=0;
           while (c[i]<=k&&d1<n){
               if (c[i]+g[(i+d1)%n]<=k) c[i]+=g[(i+d1)%n]; else { d1++; break;}
               d1++;
               }
           d[i]=d1-1;
           //printf("%d %d %d\n",i,c[i],d[i]);
           //pri debugiranju izpisi d[i] in c[i]
           }
        //simuliramo dokler se ne ponovi
        int t=-1;
        int pos=0;
        for (int i=0;i<n;i++) {b[i][0]=0; b[i][1]=0;}

        while (b[pos][0]==0){
            t++;
            p[t]=pos;
            b[pos][0]=1;
            b[pos][1]=t;
            pos=(pos+d[pos])%n;
            }
         //printf("%d %d\n",pos,t);
         int C=0;
         for (int i=0;i<b[pos][1];i++) C+=c[p[i]];
         //printf("%d\n",C);
         int C1=0;
         for (int i=b[pos][1];i<t+1;i++) C1+=c[p[i]];
         C=C+((r-b[pos][1])/(t-b[pos][1]+1))*C1;
        //printf("%d\n",C);
         for (int i=b[pos][1];i<t+1;i++){
             if (i-b[pos][1]==(r-b[pos][1])%(t-b[pos][1]+1)) break;
             C+=c[p[i]];
             }
         //for (int i=0;i<n;i++) printf("%d\n",p[i]);
         fprintf(f1,"Case #%d: %d\n",t2-t1,C);
        }
     fclose(f);fclose(f1);
    return 0;
    }
