#include<cstdio>

char tab[101][101];
double owp[100], oowp[100];
int won[100], lost[100];
int n, tests;

int main() {
  scanf("%d",&tests);
  for(int t=1;t<=tests;t++) {
    scanf("%d",&n);
    for(int i=0;i<n;i++)
      scanf("%s",&tab[i]);
    for(int i=0;i<n;i++)
      owp[i] = oowp[i] = 0.0;
    for(int i=0;i<n;i++) {
      won[i] = lost[i] = 0;
      for(int j=0;j<n;j++) {
        if(tab[i][j] == '1') won[i]++;
        if(tab[i][j] == '0') lost[i]++;
      }      
    }
    for(int i=0;i<n;i++) {
      double sum = 0.0;
      int opps = 0;
      for(int j=0;j<n;j++) {
        if(tab[i][j] != '.') opps++;
        if(tab[i][j] == '1')
          sum += (double)(won[j])/(double)(won[j]+lost[j]-1);
        else if(tab[i][j] == '0')
          sum += (double)(won[j]-1)/(double)(won[j]+lost[j]-1);
      }
      owp[i] = sum / (double)opps;
    }
    for(int i=0;i<n;i++) {
      double sum = 0.0;
      int opps = 0;
      for(int j=0;j<n;j++) {
        if(tab[i][j] != '.') {
          opps++;
          sum += owp[j];
        }
      }
      oowp[i] = sum / (double)opps;
    }
    printf("Case #%d:\n",t);
    for(int i=0;i<n;i++) {
      double wp = (double)won[i] / (double)(won[i]+lost[i]);
      //printf("%d: %lf %lf %lf\n",i,wp,owp[i],oowp[i]);
      printf("%.9lf\n",wp*0.25+owp[i]*0.5+oowp[i]*0.25);
    }
  }
  return 0;
}
        
        
    
  
