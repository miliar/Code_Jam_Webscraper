#include<iostream.h>
#include<stdio.h>
#include<conio.h>
int isdot,ist;
int check_rows(char b[4][4],int j){
    ist=0;
    int i,X=0,O=0;
    char p;
    for(i=0;i<4;i++){
                     p = b[j][i];
                     if(p=='X')
                     X++;
                     if(p=='O')
                     O++;
                     if(p=='T')
                     ist = 1;
                     if(p=='.'){
                                isdot = 1;
                                return 3;
                                }
                     
                     }
    if((X==3 && ist==1) || (X==4))
    return 1;
    if((O==3 && ist==1) || (O==4))
    return 2;
    else
    return 3;
    }

int check_cols(char b[4][4],int j){
    ist=0;
    int i,X=0,O=0;
    char p;
    for(i=0;i<4;i++){
                     p = b[i][j];
                     if(p=='X')
                     X++;
                     if(p=='O')
                     O++;
                     if(p=='T')
                     ist = 1;
                     if(p=='.'){
                                isdot = 1;
                                return 3;
                                }
                     
                     }
    if((X==3 && ist==1) || (X==4))
    return 1;
    if((O==3 && ist==1) || (O==4))
    return 2;
    else
    return 3;
    }
    
int check_di(char b[4][4],int k){
    if(k==1){
             ist=0;
             int i,j,X=0,O=0;
             char p;
             for(i=0,j=0;i<4;i++,j++){
                                      p = b[i][j];
                                      if(p=='X')
                                      X++;
                                      if(p=='O')
                                      O++;
                                      if(p=='T')
                                      ist = 1;
                                      if(p=='.'){
                                                 isdot = 1;
                                                 return 3;
                                                 }
                                      
                                      }
             if((X==3 && ist==1) || (X==4))
             return 1;
             if((O==3 && ist==1) || (O==4))
             return 2;
             else
             return 3;
             
             }
    else{
         ist=0;
             int i,j,X=0,O=0;
             char p;
             for(i=3,j=0;i>=0 && j<4;i--,j++){
                                      p = b[i][j];
                                      if(p=='X')
                                      X++;
                                      if(p=='O')
                                      O++;
                                      if(p=='T')
                                      ist = 1;
                                      if(p=='.'){
                                                 isdot = 1;
                                                 return 3;
                                                 }
                                      
                                      }
             if((X==3 && ist==1) || (X==4))
             return 1;
             if((O==3 && ist==1) || (O==4))
             return 2;
             else
             return 3;
             
         }
    }

int main(){
    int T,i,j=0,soln,s=0,flag=0,w;
    char **b;
    char a[4][4];    
    scanf("%d",&T);
    int sol[T];
    for(w=0;w<T;w++){
                     isdot = 0;
               for(i=0;i<4;i++){
                                for(j=0;j<4;j++)
                                cin>>a[i][j];
                                }
               for(i=0;i<4;i++){
                                soln = check_rows(a,i);                                
                                switch(soln){
                                            case 1:
                                                   sol[s]=1;
                                                   s++;
                                                   flag = 1;
                                                   break;
                                            case 2:
                                                   sol[s]=2;
                                                   s++;
                                                   flag = 1;
                                                   break;
                                            case 3:
                                                   flag = 0;
                                                   break;
                                                   
                                            }
                                if(flag==1)
                                           break;
                                else{
                                    continue;
                                    }
                               }
               if(flag==0){
                           for(i=0;i<4;i++){
                                            soln = check_cols(a,i); 
                                            switch(soln){
                                            case 1:
                                                 sol[s]=1;
                                                 s++;
                                                 flag = 1;
                                                 break;
                                            case 2:
                                                   sol[s]=2;
                                                   s++;
                                                   flag = 1;
                                                   break;
                                            case 3:
                                                   flag = 0;
                                                   break;
                                                   
                                            }
                           if(flag==1)
                                      break;
                           else{
                                continue;
                                }
                           }

                           }
               if(flag==0){
                           for(i=0;i<2;i++){
                                            soln = check_di(a,i); 
                                            switch(soln){
                                            case 1:
                                                 sol[s]=1;
                                                 s++;
                                                 flag = 1;
                                                 break;
                                            case 2:
                                                   sol[s]=2;
                                                   s++;
                                                   flag = 1;
                                                   break;
                                            case 3:
                                                   flag = 0;
                                                   break;
                                                   
                                            }
                           if(flag==1)
                                      break;
                           else{
                                continue;
                                }
                           }
                           }
               if(flag==0){
                           if(soln==3 && isdot==1){
                                                   sol[s]=3;
                                                   s++;
                                                   }
                           if(soln==3 && isdot!=1){
                                                   sol[s]=4;
                                                   s++;
                                                   }
                           }
               
               }
               for(i=0;i<T;i++){
                                switch(sol[i]){
                                             case 1:
                                                    printf("Case #%d: X won\n",i+1);
                                                    break;
                                             case 2:
                                                    printf("Case #%d: O won\n",i+1);
                                                    break;
                                             case 3:
                                                    printf("Case #%d: Game has not completed\n",i+1);
                                                    break;
                                             case 4:
                                                    printf("Case #%d: Draw\n",i+1);
                                                    break;
                                             }
                                }
               return 0;
    }
