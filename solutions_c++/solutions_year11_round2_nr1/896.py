#include<stdio.h>
int main(){
    int T, N;
    int g, i, k;
    char a[105][105];
    double media[105];
    double WP[105][105];
    double OWP[105];
    double OOWP[105];
    double RPI[105];

    double jogos[105];
    double soma[105];
    scanf("%d ", &T);
    for(g=1; g<=T; g++){
        scanf("%d ", &N);
        for(i=0; i<N; i++)
            for(k=0; k<N; k++)
                scanf("%c ", &a[i][k]);       

        for(i=0; i<N; i++){
            jogos[i]=0;
            soma[i]=0;
            for(k=0; k<N; k++){
                if(a[i][k]=='1'){
                    jogos[i]++;
                    soma[i]++;
                }
                if(a[i][k]=='0'){
                    jogos[i]++;
                }
            }       
        }
        
        for(i=0; i<N; i++)
            media[i]=soma[i]/jogos[i];
    
        for(i=0; i<N; i++)
            for(k=0; k<N; k++){
                if(a[i][k]=='.')
                    WP[i][k] = soma[i]/jogos[i];
   
                
                
                if(a[i][k]=='1')
                    WP[i][k] = (soma[i]-1)/(jogos[i]-1);
                
                if(a[i][k]=='0')
                    WP[i][k] = soma[i]/(jogos[i]-1);
                
            }
        for(i=0; i<N; i++){
            OWP[i]=0;
            for(k=0; k<N; k++){
                if(a[i][k]!='.')
                    OWP[i]+= WP[k][i];
            }
            OWP[i] = OWP[i]/jogos[i];
        }

        for(i=0; i<N; i++){
            OOWP[i]=0;
            for(k=0; k<N; k++){
                if(a[i][k]!='.')
                    OOWP[i]+=OWP[k];
            }
            OOWP[i] = OOWP[i]/jogos[i];
        }

        for(i=0; i<N; i++)
            RPI[i] = 0.25*media[i] + 0.5*OWP[i] + 0.25*OOWP[i];

        printf("Case #%d:\n", g);
        for(i=0; i<N; i++){
            //printf("%llf -- %llf -- %llf --%llf == %llf == %llf\n", RPI[i], media[i], OWP[i], OOWP[i], soma[i], jogos[i]);
            printf("%llf\n", RPI[i]);
        }     
        /*for(i=0; i<N; i++){
            for(k=0; k<N; k++)
                printf("%llf ", WP[i][k]);
            printf("\n");
        } */  
    }
    return 0;
}
