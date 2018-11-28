#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

char name[101][101];
int s,q;
int a[1001];
int f[1001][101];

void Input(){
     int i,j,k;
     scanf("%d",&s);
     gets(name[0]);
     for(i=1;i<=s;i++){
       gets(name[i]);
     }
     scanf("%d",&q);
     gets(name[0]);
     for(i=1;i<=q;i++){
       char ts[101];
       gets(ts);
       for(j=1;j<=s;j++){
         if(strcmp(name[j],ts)==0) break;
       }
       a[i]=j;
     } 
     return;    
}

int Solve(){
     if(q==0){
        return 0;
     }
     int i,j,k;
     memset(f,-1,sizeof(f));
     for(i=1;i<=s;i++){
       f[1][i]=0;
     }
     f[1][a[1]]=-1;
     for(i=2;i<=q;i++){
       for(j=1;j<=s;j++){
         if(j!=a[i]){
              for(k=1;k<=s;k++){
                 if(f[i-1][k]!=-1){
                    int tmp;
                    tmp=(j==k?f[i-1][k]:f[i-1][k]+1);
                    if(f[i][j]<0||tmp<f[i][j]){
                      f[i][j]=tmp;
                    }
                 }
              }
         }
       }
     }
     int mmin=-1; 
     for(i=1;i<=s;i++){
        if(f[q][i]!=-1){
          if(mmin<0||f[q][i]<mmin){
            mmin=f[q][i];
          }                
        }        
     }
     return mmin;
}

int main(int argc, char *argv[])
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tn;
    int id=1;
    scanf("%d",&tn);
    while(tn--){
        Input();
        printf("Case #%d: %d\n",id++,Solve());
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}
