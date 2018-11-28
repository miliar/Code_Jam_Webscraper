#include<stdio.h>
#include<conio.h>
int main(){
    int a[10000],t,i,flag,small,n,s;
    long int l,h,j,fr;
    FILE *f1,*f2;
    f1=fopen("C-small-attempt1.in","r");
    f2=fopen("output.in","w");
    fscanf(f1,"%d",&t);
    printf("%d",t);
    for(i=1;i<=t;i++){
                      fscanf(f1,"%d%ld%ld",&n,&l,&h);
                      fprintf(f2,"Case #%d: ",i);
                      for(j=0;j<n;j++){                                       
                      fscanf(f1,"%d",&a[j]);
                      }
                      if(l==1){fprintf(f2,"%d\n",l);continue;}
                     /* while(1){
                               small=0;
                               flag=1;
                               for(j=1;j<n;j++){
                                              
                                              f(a[small]>a[j]){small=j;flag=0;}
                                                }
                               
                      if(flag==1&&a[0]==a[1])break;
                      else 
                           a[small]+=a[small];
                           printf("a=%d",a[small]);
                           getch();
                           }*/
                      flag=0;
                      fr=0;
                      printf("i=%d",i);
                      for(j=l;j<=h;j++){
                                        flag=0;//if(j%a[0]==0||a[0]%j==0){
                                        for(s=0;s<n;s++){
                                                         //printf("j=%d,s=%d",j,a[s]);
                                                        // getch();
                                                         if(j%a[s]==0||a[s]%j==0)continue;
                                                         else {
                                                              flag=1;
                                                              break;
                                                              }
                                                         }
                                        if(flag==0){fr=j;break;}
                                                         //}
                                                         }
                      if(fr==0)
                                 fprintf(f2,"NO\n");
                      else 
                           fprintf(f2,"%ld\n",fr);
}
fclose(f1);
fclose(f2);
getch();
}                    
                                   
                      
