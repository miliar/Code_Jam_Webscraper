#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {

    FILE* fin;
    FILE* fout;
    fin = fopen ("1.in","r");
    fout = fopen ("1.out","w");
    
    int n; // total number of cases
    int nc,ec,sc; // counter
    int e; // number of engines
    int s; // number of searches
    int result;
    int checks;
    int i;
    char search[110][100];
    char engine[100][100];
    int checklist[110];
    fscanf (fin,"%d",&n);
    
    for (nc=1;nc<=n;nc++) {
        fscanf (fin,"%d\n",&e);
        for (ec=0;ec<e;ec++) fgets (engine[ec],110,fin);
        fscanf (fin,"%d\n",&s);
        for (sc=0;sc<s;sc++) fgets (search[sc],110,fin);
        for (i=0;i<110;i++) checklist[i]=0;
        for (result=0,checks=0,sc=0;sc<s;sc++) {
            for (ec=0;ec<e;ec++) {
                if (strcmp(search[sc],engine[ec])==0 && checklist[ec]==0) {
                   if ((checks+
                   1)==e) {
                      result++;
                      checks=1;
                      for (i=0;i<110;i++) checklist[i]=0;
                      checklist[ec]=1;
                   }
                   else {
                        checklist[ec]=1;
                        checks++;                                     
                   }
                }
            }

        }
      
        
        
        fprintf (fout,"Case #%d: %d\n",nc,result);
    } 
    system ("pause");
}
