#include<iostream>
using namespace std;
int T, N, i, k, kase;
char str[100][101];
int oppCtr[100];
int win[100];
int lose[100];
double wp[100], owp[100], oowp[100], rip[100];
double wpo[100][100];
int main(){
    freopen("Alarge.in","r",stdin);
    freopen("Alarge.out","w",stdout);
    scanf("%d",&T);
    for(kase=1;kase<=T;kase++){
        scanf("%d",&N);
        for(i=0;i<N;i++){
            lose[i] = win[i] = oppCtr[i] = 0;                   
            scanf("%s",str[i]);
            for(k=0;k<N;k++){
                switch(str[i][k]){
                  case '0':
                       lose[i]++;
                       oppCtr[i]++;
                       break;
                  case '1':
                       win[i]++;
                       oppCtr[i]++;
                       break;
                }
            }
        }
        for(i=0;i<N;i++){
            if(oppCtr[i] !=0)
                        wp[i] = (1.0*win[i])/oppCtr[i];
        }
        for(i=0;i<N;i++){
            double tmp =0;             
            for(k=0;k<N;k++){
                if(str[i][k] != '.')
                   if(oppCtr[k] != 1)          
                                tmp += (str[k][i] == '1')? (1.0*(win[k] -1))/(oppCtr[k] -1) : (1.0*win[k])/(oppCtr[k]-1);
                   
                    
            }
            
            owp[i] = tmp/oppCtr[i];
        }
        
        for(i=0;i<N;i++){
            double tmp =0;             
            for(k=0;k<N;k++){
                if(str[i][k] != '.')
                   tmp += owp[k];
            }
            oowp[i] = tmp/oppCtr[i];
        }
        for(i=0;i<N;i++){
            rip[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
        }

        printf("Case #%d:\n",kase);
        //for(i=0;i<N;i++)
        //   cout<<oppCtr[i]<<" "<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<endl;
        for(i=0;i<N;i++)
                        printf("%.6lf\n",rip[i]);
    }
    return 0;

}
                                        

                                 
        
            
                                  
                                                        
