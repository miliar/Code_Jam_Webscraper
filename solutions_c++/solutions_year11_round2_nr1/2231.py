#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
    freopen("A.in","r",stdin);
    freopen("A.txt","w",stdout);
    int n,i,j,k,t,s;
    char a[100][101];
    bool b[100][100];
    float wp[100], nj[100], owp[100], oowp[100], rpi[100];
    cin>>t;
    s=t;
    while(t>0){
    cin>>n;
    for(i=0;i<n;i++){
                     wp[i]=0;
                     nj[i]=0;
                     owp[i]=0;
                     oowp[i]=0;
                     cin>>a[i];
                     for(j=0;j<n;j++){
                                      if(a[i][j]=='.'){
                                                      b[i][j]=0;
                                                      }
                                      else{
                                           b[i][j]=1;
                                           nj[i]++;
                                           if(a[i][j]=='1'){
                                                           wp[i]++;
                                                           }
                                           }
                                      }                 
                     wp[i]=wp[i]/nj[i];
                     }
    for(i=0;i<n;i++){
                     for(j=0;j<n;j++){
                                      if(b[i][j]){
                                                  if(a[i][j]=='0'){
                                                                   owp[i]=owp[i]+(wp[j]*nj[j]-1)/(nj[j]-1);
                                                                   }
                                                  else{
                                                       owp[i]=owp[i]+(wp[j]*nj[j])/(nj[j]-1);
                                                       }
                                                  }
                                      }
                     owp[i]=owp[i]/nj[i];
                     }
    printf("Case #%d: \n",s-t+1);
    for(i=0;i<n;i++){
                     for(j=0;j<n;j++){
                                      if(b[i][j]){
                                                  oowp[i]=oowp[i]+owp[j];
                                                  }                 
                                      }
                     oowp[i]=oowp[i]/nj[i];
                     rpi[i]=wp[i]/float(4)+owp[i]/float(2)+oowp[i]/float(4);
                     printf("%.8f\n",rpi[i]);
                     }
    t--;}
    }
