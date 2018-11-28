#include <iostream>

using namespace std;

int t, tt, n,kb,ko,poso,posb,steps,i,ans,j,kk;
char c[100];
int p[100];
int o[100];
int b[100];

int abs(int a){
    if (a<0) return -a; else return a;    
}

int main(){
    freopen("c:/input.txt","r",stdin);
    freopen("c:/output.txt","w",stdout);
    cin>>t;
    while (t--){
          tt++;
          cout<<"Case #"<<tt<<": ";
          cin>>n;
          for (i=0;i<n;i++){
              cin>>c[i];
              cin>>p[i];
          }
          posb=1;
          poso=1;
          ans=0;
          for (i=0;i<n;i++){
              if (c[i]=='B'){
                 steps=abs(p[i]-posb)+1;
                 ans+=steps;
                 posb=p[i];
                 for (j=i+1;j<n;j++)
                     if (c[j]=='O'){
                        kk=p[j];
                        if (abs(kk-poso)<=steps){
                           poso=kk;                  
                        } else
                        {
                              if (kk>poso){
                                 poso+=steps;
                              } else
                                 poso-=steps;
                        }
                        break;               
                     }    
              }else
              {
                 steps=abs(p[i]-poso)+1;
                 ans+=steps;
                 poso=p[i];
                 for (j=i+1;j<n;j++)
                     if (c[j]=='B'){
                        kk=p[j];
                        if (abs(kk-posb)<=steps){
                           posb=kk;                  
                        } else
                        {
                              if (kk>posb){
                                 posb+=steps;
                              } else
                                 posb-=steps;
                        }
                        break;               
                     }      
              } 
          }
          cout<<ans<<endl;
    }
    //system("pause");
    return 0;    
}
