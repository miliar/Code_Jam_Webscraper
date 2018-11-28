#include <stdio.h>
#include <conio.h>

int t,a,m,n;
int b[513][513];


bool revisa(int i,int j,int k){
     int ant,sal;
     ant=(b[i][j]*-1)+1;
     sal=0;
     for (int x=i;x<i+k&&sal==0;x++){
          for (int y=j;y<j+k&&sal==0;y++){
              if (b[x][y]==ant||b[x][y]==2)
                 sal=1;
              ant=b[x][y];
              }
          ant=b[x][j];          
          }
     if (sal==0)
        return true;
        else
            return false;
     }

void corta(int i,int j,int k){
     for (int x=i;x<i+k;x++)
          for (int y=j;y<j+k;y++)
              b[x][y]=2;
     }

void muestra(){
     for (int i=0;i<m;i++){
         for (int j=0;j<n;j++){
             printf("%d",b[i][j]);     
             }
         printf("\n");         
         }
     printf("\n");         
     }

int main(){
    char c;
    int s[514],st,men;
    scanf("%d",&t);
    for (int t2=1;t2<=t;t2++){
        scanf("%d %d",&m,&n);
        if (m<n)
           men=m;
           else
               men=n;
        scanf("%c",&c); 
        for (int i=0;i<m;i++){
            for (int j=0;j<n;j=j+4){
                scanf("%c",&c);                
                if (c>='0'&&c<='9')
                   a=c-'0';
                if (c>='A'&&c<='F')
                   a=c-'A'+10;                 
                for (int msk=8,k=0;msk>0;msk=msk>>1,k++){
                    if ((a&msk)>0)
                       b[i][j+k]=1;
                       else
                           b[i][j+k]=0;            
                    }
                }
            scanf("%c",&c);                
            }
        st=0;  
        for (int k=men;k>0;k--){
            s[k]=0;                
            for (int i=0;i<m;i++){
                for (int j=0;j<n;j++){
                    if (b[i][j]!=2&&revisa(i,j,k)){
                       corta(i,j,k);                
                       s[k]++;                
                       }
                    }
                }
            if (s[k]>0)
               st++;
            }
        
        printf("Case #%d: %d\n",t2,st); 
        for (int k=men;k>0;k--){
            if (s[k]>0)
               printf("%d %d\n",k,s[k]);
            }
        
        }
    getch();
    return 0;
    }

