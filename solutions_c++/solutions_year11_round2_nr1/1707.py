#include <stdio.h>
#include <string.h>
#include <iostream>
 
 using namespace std;
 
int m[100][100];

int win[100];
int games[100];
double owp[100];
double oowp[100];
double wp[100];
double rpi;
double wp_m[100][100];
int t,n;

int main()
{
    int teste,i,j;
    char c;
    
    scanf("%d",&t);
    for(teste=1;teste<=t;teste++){
        scanf("%d ",&n);
        memset(win, 0, sizeof(win)); memset(games, 0, sizeof(games));
        for(i=0;i<n;i++,getchar()) for(j=0;j<n;j++){
            c = getchar();
            if(c=='.')      m[i][j] = -1;
            else if(c=='0') {m[i][j] =  0; games[i]++;}
            else            {m[i][j] =  1; win[i]++;  games[i]++;}
        }
        
        for(i=0;i<n;i++) wp[i] = win[i]/(double)games[i];
        
        memset(owp, 0, sizeof(owp));
        for(i=0;i<n;i++) for(j=0;j<n;j++) if(i!=j){
            if(m[j][i] == -1)      ;
            else if(m[j][i] == 0)  owp[i] += win[j]/(double)(games[j]-1);
            else                   owp[i] += (win[j]-1)/(double)(games[j]-1);
        }
        for(i=0;i<n;i++) owp[i] = owp[i]/(games[i]);
        
        memset(oowp, 0, sizeof(oowp));
        for(i=0;i<n;i++) for(j=0;j<n;j++){
            if(m[i][j] != -1) oowp[i] += owp[j];
        }
        
        printf("Case #%d:\n",teste);
        for(i=0;i<n;i++){
          rpi =  0.25*wp[i] + 0.5*(owp[i]) + 0.25*(oowp[i]/(games[i]));
          printf("%.15lf\n",rpi);
          //~ cout << rpi << endl;
        }
    }
    return 0;
}