#include <iostream>
using namespace std;
int d,k,n;
char s[1000][1000];
int poin[1000][1000];
void hajar(char c,int pos){
     
     for (int ii=1;ii<=d;ii++){
         if(s[ii][pos-1]==c) poin[ii][pos]=1;    
         }
     
     }
void itung(int nomor){
     int ans=0;
     for (int i=1;i<=d;i++){
         int tmp=1;
         for (int j=1;j<=k;j++)
         if (poin[i][j]==0) tmp=0;
         
         ans+=tmp;    
         }
     printf("Case #%d: %d\n",nomor,ans);
     }
void reset(){
     for (int i=0;i<=999;i++)
     for (int j=0;j<=999;j++)
     poin[i][j]=0;
     }

void sedot(int y){
     char buff;
     scanf("%c",&buff);
     while (buff!=')'){
           hajar(buff,y);
           scanf("%c",&buff);
          
           }
     
     }
     
int main(){
    freopen("alien.in","r",stdin);
    freopen("alien.out","w",stdout);
    scanf("%d%d%d",&k,&d,&n);
    for (int i=1;i<=d;i++)
    scanf("%s",s[i]);
   // scanf("\n");
    char tmpc;
    for (int i=1;i<=n;i++){
    scanf("\n");
     
      reset();
        int x=1;
        while (x<=k){scanf("%c",&tmpc);
             if (tmpc!='('){
                           hajar(tmpc,x);
                           x++;
                           }   
                  else{sedot(x); x++;}  
                  }
        itung(i);
        
        
        }
    //system("pause");
    }
