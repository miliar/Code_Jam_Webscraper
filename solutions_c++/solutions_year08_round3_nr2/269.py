#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

string bil;
int n;
long long con;
int bils[81];
int mark;

long long abso(long long a) {return a>0?a:-a;}


void permute(int lvl){
     int i;
     long long bila,biltemp;
     
     if (lvl==bil.length()-1){
          bila=0;
          biltemp=bils[0];
          /*for (i=0;i<bil.length()-1;i++){
                printf("%d ",bils[i*2+1]);    
          }*/
          mark=-1;
          for (i=0;i<bil.length()-1;i++){
               if (bils[i*2+1]==-3){
                    biltemp*=10;
                    biltemp+=bils[(i+1)*2];
                    //printf("%d==%d ",biltemp,mark);
               }  else {
                    if (mark==-1) bila+=biltemp; else
                    if (mark==-2) bila-=biltemp;
                    biltemp=bils[(i+1)*2];
                    mark=bils[i*2+1];    
               }
          }
          if (mark==-1) bila+=biltemp; else 
          if (mark==-2) bila-=biltemp;
          //printf("%d %d\n",mark,bila);
          bila=abso(bila);
          if (bila%2==0 || bila%5==0 || bila%3==0 || bila%7==0) con++;
          return;
     }  
     bils[(lvl*2)+1]=-1;
     permute(lvl+1);
     bils[(lvl*2)+1]=-2;
     permute(lvl+1);
     bils[(lvl*2)+1]=-3;
     permute(lvl+1);
     
}

int main(){
     int i,j;
     
     scanf("%d",&n);
     for (i=0;i<n;i++){
          cin>>bil;
          con=0;
          for (j=0;j<bil.length();j++){
               bils[j*2]=int(bil[j])-48;
          }
          permute(0);
          printf("Case #%d: %lld\n",i+1,con);    
     }
     return 0;    
}
