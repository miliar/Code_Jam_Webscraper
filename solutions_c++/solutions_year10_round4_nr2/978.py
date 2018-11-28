#include<iostream>
using namespace std;

int main(){
    int num=0;
    int t,p,i,j,a[10][515],c[1025],min[10][515];
    cin>>t;
    while(t--){
               cin>>p;
               for(i=0;i<(1<<p);i++)cin>>c[i];
               for(i=0;i<p;i++)
                               for(j=0;j<(1<<(p-i-1));j++)cin>>a[i][j];
               for(i=0;i<(1<<(p-1));i++){
                                     min[0][i]=(c[2*i]<c[2*i+1])?c[2*i]:c[2*i+1];
                                     if(min[0][i]>0){min[0][i]--;a[0][i]--;}
                                     }
               for(i=1;i<p;i++)
                               for(j=0;j<(1<<(p-i-1));j++){
                                                          min[i][j]=(min[i-1][2*j]<min[i-1][j*2 +1])?min[i-1][2*j]:min[i-1][j*2 +1];
                                                          if(min[i][j]>0){min[i][j]--;a[i][j]--;}
                                                          }
               long ans=0;
               for(i=0;i<p;i++)
                               for(j=0;j<(1<<(p-i-1));j++)ans+=a[i][j];
                               
                 
                 cout<<"Case #"<<++num<<": "<<ans<<endl;
                 }
    
    return 0;
    }
