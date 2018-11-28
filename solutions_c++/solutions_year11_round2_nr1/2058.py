#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

void cwp(double WP[], int j, char tab[][110], int n) {
          double n1 = 0, nt = 0;
          for(int i = 0;i < n;i++) {
                  if(tab[j][i] == '1') {
                      nt++; n1++;
                  }
                  if(tab[j][i] == '0')
                       nt++;
          }
          WP[j] = n1/nt;
       
}

void cowp(double OWP[], int j, char tab[][110], int n) {
          double n1 = 0, nt = 0;
          double aux = 0;
          for(int i = 0;i < n;i++) {
                  if(tab[j][i] == '1') {
                      nt++; n1++;                    
                  }
                  if(tab[j][i] == '0')
                       nt++;
                  if(tab[j][i] != '.') {
                  double n1a = 0, nta = 0;
                  for(int k = 0;k < n;k++) {
                          if(tab[i][k] == '1' && k != j) {
                                   nta++; n1a++; 
                               
                          }
                          if(tab[i][k] == '0' && k != j) {
                                   nta++; 
                                  
                          }
                          
                                    
                  }
                                
                  aux += n1a/nta;
                              
                  }             
          }

          OWP[j] = aux/nt;   
    

}     

void coowp(double OOWP[], int j, char tab[][110], int n, double OWP[]) {
          double n1 = 0, nt = 0;
          double aux = 0;
          for(int i = 0;i < n;i++) {
                  if(tab[j][i] == '1') {
                      nt++; n1++;
                  }
                  if(tab[j][i] == '0')
                       nt++;
                  if(tab[j][i] != '.') 
                       aux += OWP[i];    
          }
          
          OOWP[j] = aux/nt;
     
          
}

int main() {
    int t;
    scanf("%d",&t);
    for(int i = 1;i <= t;i++) {
            int n;
            char tab[110][110];
            double OWP[110];
            double WP[110];
            double OOWP[110];
            scanf("%d",&n);
            for(int j = 0;j < n;j++)
                     scanf("%s",tab[j]);          
            for(int j = 0;j < n;j++) {
                    cwp(WP,j,tab,n);
                    cowp(OWP,j,tab,n);
            }
            printf("Case #%d:\n",i);
            for(int j = 0;j < n;j++) {
                    coowp(OOWP,j,tab,n,OWP);
                    printf("%llf\n",0.25*WP[j] + 0.5*OWP[j] + 0.25*OOWP[j]); 
            }                                                                 
    }               
    return 0;
}
