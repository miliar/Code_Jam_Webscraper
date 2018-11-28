#include<conio.h>
#include<stdio.h>
int main(){
    char a[100][100],c;
    int t,n,i,j,s;
    float wp[100],owp[100],oowp[100],rpi[100],won,total,average,op[100];
    FILE *f1,*f2;
    f1=fopen("A-large.in","r");
    f2=fopen("output.in","w");
    fscanf(f1,"%d",&t);
    printf("%d",t);
    getch();   
    for(i=1;i<=t;i++){
                      fscanf(f1,"%d%c",&n,&j);
                      
                      for(j=0;j<n;j++){
                                       total=0;won=0;
                                       for(s=0;s<n;s++){
                                                        fscanf(f1,"%c",&a[j][s]);
                                                        //printf("%c",a[j][s]);
                                                        //getch();
                                                        if(a[j][s]==49||a[j][s]==48){
                                                                       total=total+1;
                                                                       }
                                                        if(a[j][s]==49){
                                                                 won=won+1;
                                                                 }
                                                                 
                                                        }
                                                        //printf("total=%f,won=%f",won,total);
                                                        //getch();
                                                        wp[j]=won/total;
                                                        op[j]=total;
                                                        //printf("wp=%f",wp[j]);
                                                        //getch();
                                                        fscanf(f1,"%c",&c);
                                                        }
                      for(j=0;j<n;j++){
                                       average=0;
                                       for(s=0;s<n;s++){
                                                        won=0;total=0;
                                                        if(a[j][s]==46)continue;   
                                                        for(int k=0;k<n;k++){
                                                                         if(j!=s){
                                                                                  if(a[s][k]==49&&j!=k){
                                                                                                       won++;
                                                                                                       total++;
                                                                                                       }
                                                                                  if(a[s][k]==48&&j!=k){
                                                                                                       total++;
                                                                                                       }
                                                                                                       }
                                                                                                       }
                                       
                                                        if(j!=s)    
                                                        {average+=won/total;}//printf("avg=%f",average);getch();}
                                                        
                                                        }
                                       owp[j]=average/op[j];
                                       //printf("owp=%f",owp[j]);
                                       //getch();
                                       
                                       }
                      fprintf(f2,"Case #%d: \n",i);
                     // printf("i=%d",i);
                      //getch();
                      for(j=0;j<n;j++){
                                       average=0;
                                       for(s=0;s<n;s++){
                                                        if(j!=s&&a[j][s]!=46)average+=owp[s];
                                                        }
                                      // printf("average=%f",average);
                                       //getch();
                                       oowp[j]=average/op[j];
                                       //printf("oowp=%f",oowp[j]);
                                       //getch();
                                       //printf("wp=%f,owp=%f,oowp=%f",wp[j],owp[j],oowp[j]);
                                       //getch();
                                       rpi[j]=0.25*wp[j]+0.50*owp[j]+0.25*oowp[j];
                                       fprintf(f2,"%f\n",rpi[j]);
                                       }
}
fclose(f1);
fclose(f2);
getch();
}
                      
                      
                                                                                                       

                                                                 

                                       
                      
    
