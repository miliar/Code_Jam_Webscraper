#include<iostream>
#include<stdio.h>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("abc.out","w",stdout);
    int T, N, I, i, j, won[101], total[101];
    char s[101][101]={'\0'};
    double wp[101]={0}, owp[101]={0}, oowp[101]={0}, owpsum, oowpsum;
    cin>>T;
    for(I=1; I<=T; I++){
             cin>>N;
             
             for(i=0; i<N; i++){
                      won[i]=0;
                      total[i]=0;
                      for(j=0; j<N; j++){
                               cin>>s[i][j];
                               if(s[i][j]=='1'){
                                                won[i]++;
                                                total[i]++;
                                                }
                               else
                               if(s[i][j]=='0')
                                               total[i]++;
                      }
                      wp[i]=(double)won[i]/total[i];
             }
                                           
             for(i=0; i<N; i++){
                      owpsum=0;
                      for(j=0; j<N; j++){
                               switch(s[i][j]){
                                               case '0':
                                                    owpsum+=(double)(won[j]-1)/(total[j]-1);
                                                    break;
                                               case '1':
                                                    owpsum+=(double)won[j]/(total[j]-1);
                                                    
                               }
                      }
                      owp[i]=(double)owpsum/total[i];
                      
             }
             
             for(i=0; i<N; i++){
                      oowpsum=0;
                      for(j=0; j<N; j++){
                               if(s[i][j]!='.')
                                      oowpsum+=owp[j];
                      }
                      oowp[i]=oowpsum/total[i];
             }
                               
             
             cout<<"\nCase #"<<I<<":";
             for(i=0; i<N; i++)
                      printf("\n%14.12lf", (0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i]));
             
    }
    
    return 0;
}
                      
