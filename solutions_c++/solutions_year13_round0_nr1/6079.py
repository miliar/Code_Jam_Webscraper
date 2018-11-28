#include<stdio.h>
#include<conio.h>
#include<iostream.h>

int check(char t1,char t2,char t3,char t4)
{

    if((t1==t2 && t2==t3 && t3==t4) || (t1==t2 && t2==t3 && t4=='T') || (t1==t2 && t2==t4 && t3=='T') || (t1==t3 && t3==t4 && t2=='T') || (t2==t3 && t3==t4 && t1=='T')){
                      return(1);
    }
    else
        return(0);
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,flag,i,x=1,blank=0;
    char a[5][5];
    scanf("%d",&t);
    while(x<=t){
                blank=0;
                 printf("Case #%d: ",x);
               for(i=0;i<4;i++){
                                scanf("%s",a[i]);
                                if(blank==0){
                                             if(a[i][0]=='.' || a[i][1]=='.' || a[i][2]=='.' || a[i][3]=='.')
                                                             blank=1;
                                }
               }
               flag=0;
               for(i=0;i<4;i++){
                                flag=check(a[i][0],a[i][1],a[i][2],a[i][3]);
                                if(flag==1){
                                            if(a[i][0]!='T' && a[i][0]!='.'){
                                                             printf("%c won\n",a[i][0]);
                                                             break;
                                            }
                                            else if(a[i][1]!='.'){
                                                 printf("%c won\n",a[i][1]); break;
                                            }
                                            else{
                                                 flag=0;
                                            }
                                            
                                }
               }
               if(flag==0){
                    for(i=0;i<4;i++){
                                flag=check(a[0][i],a[1][i],a[2][i],a[3][i]);
                                if(flag==1){
                                            if(a[0][i]!='T' && a[0][i]!='.'){
                                                             printf("%c won\n",a[0][i]); break;
                                            }
                                            else if(a[1][i]!='.'){
                                                 printf("%c won\n",a[1][i]);break;
                                                 
                                            }
                                            else{
                                                 flag=0;
                                            }
                                }
                    }
               }
               if(flag==0){
                           flag=check(a[0][0],a[1][1],a[2][2],a[3][3]);
                           if(flag==1){
                                       if(a[0][0]!='T' && a[0][0]!='.'){
                                                        printf("%c won\n",a[0][0]);
                                                        
                                       }
                                       else if(a[1][1]!='.'){
                                            printf("%c won\n",a[1][1]);
                                            
                                       }
                                       else{
                                                 flag=0;
                                       }
                           }
                           else{
                                flag=check(a[0][3],a[1][2],a[2][1],a[3][0]);
                                if(flag==1){
                                            if(a[0][3]!='T' && a[0][3]!='.'){
                                                        printf("%c won\n",a[0][3]);
                                                        
                                            }
                                            else if(a[1][2]!='.'){
                                                 printf("%c won\n",a[1][2]);
                                                
                                            }
                                            else{
                                                 flag=0;
                                            }
                                }    
                           }
               }
               if(flag==0){
                           if(blank==1)
                                       printf("Game has not completed\n");
                           else
                                       printf("Draw\n");
               }
    x++;
    }
    return 0;
}
