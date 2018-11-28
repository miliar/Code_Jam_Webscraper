#include<stdio.h>
int a[150][150];
double wp[150], owp[150], oowp[150], rpi[150], win[150], loss[150];
int main(){
    int i, j, k, n, t, opp;
    char s[150];
    FILE *fp=fopen("input.txt","r");
    FILE *ft=fopen("output.txt","w");
    fscanf(fp, "%d", &t);
    i=0;
    while (i++<t){
          fprintf(ft, "Case #%d:\n",i);
          fscanf(fp, "%d", &n);
          for (j=0; j<n; j++){
              win[j] = loss[j] = 0;
              owp[j]=0.0;
          }
          
          for (j=0; j<n; j++){
              fscanf(fp, "%s", s);
              for (k=0; k<n; k++){
                  if(s[k]=='.')
                    a[j][k]=-1;
                  else if(s[k]=='0'){
                    a[j][k]=0;
                    loss[j]++;
                  }
                  else if(s[k]=='1'){
                    a[j][k]=1;
                    win[j]++;
                  }
              }
          }    
          for (j=0; j<n; j++){
              wp[j] = (win[j])/(win[j]+loss[j]);
              opp=0;
              for (k=0; k<n; k++){
                  if(a[j][k]>=0){
                     opp++;
                     if(a[k][j]==1)
                        owp[j]+=((win[k]-1)/(win[k]+loss[k]-1));
                     else if(a[k][j]==0)
                        owp[j]+=((win[k])/(win[k]+loss[k]-1));
                     else
                        owp[j]+=((win[k])/(win[k]+loss[k]));
                  }
              }
              owp[j]/=((double)opp);
          }
          for (j=0; j<n; j++){
              oowp[j]=0.0;
              opp=0;
              for (k=0; k<n; k++){
                  if(a[j][k]>=0){
                     oowp[j]+=owp[k];
                     opp++;
                  }
              }
              oowp[j]/=((double)(opp));
              rpi[j]=(wp[j]+oowp[j])*0.25+owp[j]*0.5;
              fprintf(ft, "%lf\n", rpi[j]);
          }
    }
    return 0;
}
