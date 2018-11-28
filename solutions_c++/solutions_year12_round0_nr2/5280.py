#include <cstdio>

int main()
{
    int t,n,surp,p,num,sum,y;
    FILE *fpin, *fpout;
    fpin = fopen("input.in", "r");
    fpout = fopen("output.txt", "w");
    fscanf(fpin,"%d\n", &t);
    for(int i=0;i<t;i++) {
             fscanf(fpin, "%d ", &n);
             fscanf(fpin, "%d ", &surp);
             fscanf(fpin, "%d ", &p);
             num=0;
             for(int j=0;j<n;j++) {
                      if(j<n-1)fscanf(fpin,"%d ",&sum);
                      else fscanf(fpin,"%d\n",&sum);
                      if(p<=sum) {
                                  y=3*p-sum;
                                  if(y<=2) num++;
                                  else if(y<=4 && surp) {num++;surp--;}
                                  else;
                                 }
                     }
             fprintf(fpout,"Case #%d: %d\n", i+1, num);
            }
    fclose(fpin);
    fclose(fpout);
}
