#include<conio.h>
#include<stdio.h>
int main(){
    int n,t,i,j,s,r,c,flag;
    char a[50][50];
    FILE *f1,*f2;
    f1=fopen("A-large.in","r");
    f2=fopen("output.in","w");
    fscanf(f1,"%d",&t);
    printf("%d",t);
    getch();
    for(i=1;i<=t;i++){
                      fscanf(f1,"%d%d",&r,&c);
                      fscanf(f1,"%c",&flag );
                      for(j=0;j<r;j++){
                                       for(s=0;s<c;s++){
                                                        fscanf(f1,"%c",&a[j][s]);
                                                        }
                                                        fscanf(f1,"%c",&flag);
                                                        }
                      flag=1;
                      for(j=0;j<r;j++){
                                       for(s=0;s<c;s++){
                                                        if(a[j][s]=='#'){
                                                                         if(a[j+1][s+1]=='#'&&a[j][s+1]=='#'&&a[j+1][s]=='#'&&(j+1)<r&&s+1<c){
                                                                                    // printf("hello");getch();
                                                                                     a[j][s]='/';
                                                                                     a[j+1][s+1]='/';
                                                                                     a[j+1][s]='\\';
                                                                                     a[j][s+1]='\\';
                                                                                     
                                                                                     }
                                                                         else {
                                                                              flag=0;
                                                                              break;
                                                                              }
                                                                              
                                                                         }
                                                                         }
                                       if(flag==0)break;
                                       }
                      fprintf(f2,"Case #%d: \n",i);
                      if(flag==0)fprintf(f2,"Impossible\n");
                      else {
                           for(j=0;j<r;j++){
                                            for(s=0;s<c;s++){
                                                             fprintf(f2,"%c",a[j][s]);
                                                             }
                                            fprintf(f2,"\n");
                                            }
                                            }
}
fclose(f1);
fclose(f2);
getch();
}
            
                                                        
    
