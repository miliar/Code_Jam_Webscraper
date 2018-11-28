#include<iostream>
#include<stdio.h>
using namespace std;
int dot,t;
int cr(char ss[4][4],int j){
    t=0;
    int i,X=0,O=0;
    char p;
    for(i=0;i<4;i++){
                     p = ss[j][i];
                     if(p=='X')
                     X++;
                     if(p=='O')
                     O++;
                     if(p=='T')
                     t = 1;
                     if(p=='.'){
                                dot = 1;
                                return 3;
                                }

                     }
    if((X==3 && t==1) || (X==4))
    return 1;
    if((O==3 && t==1) || (O==4))
    return 2;
    else
    return 3;
    }

int cc(char ss[4][4],int j){
    t=0;
    int i,X=0,O=0;
    char p;
    for(i=0;i<4;i++){
                     p = ss[i][j];
                     if(p=='X')
                     X++;
                     if(p=='O')
                     O++;
                     if(p=='T')
                     t = 1;
                     if(p=='.'){
                                dot = 1;
                                return 3;
                                }

                     }
    if((X==3 && t==1) || (X==4))
    return 1;
    if((O==3 && t==1) || (O==4))
    return 2;
    else
    return 3;
    }

int cd(char ss[4][4],int k){
    if(k==1){
             t=0;
             int i,j,X=0,O=0;
             char p;
             for(i=0,j=0;i<4;i++,j++){
                                      p = ss[i][j];
                                      if(p=='X')
                                      X++;
                                      if(p=='O')
                                      O++;
                                      if(p=='T')
                                      t = 1;
                                      if(p=='.'){
                                                 dot = 1;
                                                 return 3;
                                                 }

                                      }
             if((X==3 && t==1) || (X==4))
             return 1;
             if((O==3 && t==1) || (O==4))
             return 2;
             else
             return 3;

             }
    else{
         t=0;
             int i,j,X=0,O=0;
             char p;
             for(i=3,j=0;i>=0 && j<4;i--,j++){
                                      p = ss[i][j];
                                      if(p=='X')
                                      X++;
                                      if(p=='O')
                                      O++;
                                      if(p=='T')
                                      t = 1;
                                      if(p=='.'){
                                                 dot = 1;
                                                 return 3;
                                                 }

                                      }
             if((X==3 && t==1) || (X==4))
             return 1;
             if((O==3 && t==1) || (O==4))
             return 2;
             else
             return 3;

         }
    }

int main(){
    int T,i,j=0,sn,s=0,f=0,w;
    char rr[4][4];
    scanf("%d",&T);
    int soln[T];
    for(w=0;w<T;w++){
                     dot = 0;
               for(i=0;i<4;i++){
                                for(j=0;j<4;j++)
                                cin>>rr[i][j];
                                }
               for(i=0;i<4;i++){
                                sn = cr(rr,i);
                                switch(sn){
                                            case 1:
                                                   soln[s]=1;
                                                   s++;
                                                   f = 1;
                                                   break;
                                            case 2:
                                                   soln[s]=2;
                                                   s++;
                                                   f = 1;
                                                   break;
                                            case 3:
                                                   f = 0;
                                                   break;

                                            }
                                if(f==1)
                                           break;
                                else{
                                    continue;
                                    }
                               }
               if(f==0){
                           for(i=0;i<4;i++){
                                            sn = cc(rr,i);
                                            switch(sn){
                                            case 1:
                                                 soln[s]=1;
                                                 s++;
                                                 f = 1;
                                                 break;
                                            case 2:
                                                   soln[s]=2;
                                                   s++;
                                                   f = 1;
                                                   break;
                                            case 3:
                                                   f = 0;
                                                   break;

                                            }
                           if(f==1)
                                      break;
                           else{
                                continue;
                                }
                           }

                           }
               if(f==0){
                           for(i=0;i<2;i++){
                                            sn = cd(rr,i);
                                            switch(sn){
                                            case 1:
                                                 soln[s]=1;
                                                 s++;
                                                 f = 1;
                                                 break;
                                            case 2:
                                                   soln[s]=2;
                                                   s++;
                                                   f = 1;
                                                   break;
                                            case 3:
                                                   f = 0;
                                                   break;

                                            }
                           if(f==1)
                                      break;
                           else{
                                continue;
                                }
                           }
                           }
               if(f==0){
                           if(sn==3 && dot==1){
                                                   soln[s]=3;
                                                   s++;
                                                   }
                           if(sn==3 && dot!=1){
                                                   soln[s]=4;
                                                   s++;
                                                   }
                           }

               }
               for(i=0;i<T;i++){
                                switch(soln[i]){
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
