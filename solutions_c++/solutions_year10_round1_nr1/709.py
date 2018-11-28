#include<cstdio>
#include<cstdlib>

char m[60][60];
int b[60][60];

int main(){
    int t;
    scanf("%d",&t);
    for(int c=1;c<=t;c++){
        int n,k;
        scanf("%d %d",&n,&k);
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                scanf(" %c",&m[i][j]);
                
   
        
        
        
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                b[i][j]=m[n-j-1][i];
            }
            
     
        
        
        for(int j=0;j<n;j++)
            for(int i=n-1;i>=0;i--){
                if(b[i][j]=='.'){
                    //printf("i:%d j:%d\n",i,j);
                    int cnt=0;
                    for(int l=i;l>=1;l--){
                        b[l][j]=b[l-1][j];
                        if(b[l][j]!='.')
                            cnt++;
                    }          
                    b[0][j]='.';
                    if(cnt==0)break;
                    i++;
                }
                
            }
            
    
        
        
        int blue=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                if(b[i][j]=='B'){
                    int l;
                    for(l=j;l<n && l-j+1 <=k;l++)
                        if(b[i][l]!='B')break;
                    if(l-j+1>k){
                    //    printf("achou azul pra direita no %d,%d\n",i,j);
                        blue=1;
                    }
                }
            }
       for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                if(b[i][j]=='B'){
                    int l;
                    for(l=i;l<n && l-i+1 <=k;l++)
                        if(b[l][j]!='B')break;
                    if(l-i+1>k){
                                       //     printf("achou azul pra baixo no %d,%d\n",i,j);
                        blue=1;
                    }
                }
            }
       for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                if(b[i][j]=='B'){
                    int l;
                    for(l=0;i+l<n && j+l<n && l+1 <=k;l++)
                        if(b[i+l][j+l]!='B')break;
                    if(l+1>k){
                                  //              printf("achou azul na diag descendente no %d,%d\n",i,j);
                        blue=1;
                    }
                }
            }   
                   for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                if(b[i][j]=='B'){
                    int l;
                    for(l=0;i+l<n && j-l>=0 && l+1 <=k;l++)
                        if(b[i+l][j-l]!='B')break;
                    if(l+1>k){
                        blue=1;
                    }
                }
            }  
            
                int red=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                if(b[i][j]=='R'){
                    int l;
                    for(l=j;l<n && l-j+1 <=k;l++)
                        if(b[i][l]!='R')break;
                    if(l-j+1>k){
                                        //    printf("achou vermelho pra direita no %d,%d\n",i,j);
                        red=1;
                    }
                }
            }
       for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                if(b[i][j]=='R'){
                    int l;
                    for(l=i;l<n && l-i+1 <=k;l++)
                        if(b[l][j]!='R')break;
                    if(l-i+1>k){
                                         //   printf("achou vermelho pra baixo no %d,%d\n",i,j);
                        red=1;
                    }
                }
            }
       for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                if(b[i][j]=='R'){
                    int l;
                    for(l=0;i+l<n && j+l<n && l+1 <=k;l++)
                        if(b[i+l][j+l]!='R')break;
                    if(l+1>k){
                                       //     printf("achou vermelho na diag descendente  no %d,%d\n",i,j);
                        red=1;
                    }
                }
            }  
       for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                if(b[i][j]=='R'){
                    int l;
                    for(l=0;i+l<n && j-l>=0 && l+1 <=k;l++)
                        if(b[i+l][j-l]!='R')break;
                    if(l+1>k){
                        red=1;
                    }
                }
            }  
       printf("Case #%d: ",c);
       if(red&&blue)printf("Both\n");
       else if(red)printf("Red\n");
       else if(blue)printf("Blue\n");
       else printf("Neither\n");
    }
    return 0;
}
