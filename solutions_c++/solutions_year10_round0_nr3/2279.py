#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <stdlib.h>
#include <list>

using namespace std;

int main(){
    list<int> l;
    FILE *out,*in;
    in=fopen("C-small-attempt1.in","r");
    out=fopen("sal.txt","w");
    int t,r,k,n,g,i,j,e,t2,z,g2;
    fscanf(in,"%d",&t);
    t2=1;
    while (t2<=t){
          fscanf(in,"%d %d %d",&r,&k,&n);          
          e=0;
          l.clear();
          for (i=0;i<n;i++){
              fscanf(in,"%d",&g);                        
              l.push_back(g);
              }
          
          for (i=0;i<r;i++){
              g=0;
              g2=0;
              while (l.front()+g<=k&&g2<n){
                    g+=l.front();
                    l.push_back(l.front());
                    l.pop_front();
                    g2++;
                    }
              e=e+g;                            
              }
          fprintf(out,"Case #%d: %d\n",t2,e);
          t2++;
          }    
    fclose (in);
    fclose (out);
    return 0;
    }
