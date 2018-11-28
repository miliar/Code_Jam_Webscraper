#include<conio.h>
#include<stdio.h>
#define name "B-small-attempt3.in"
int main(){
     int a[27],c,d,n,t,l=0,j,s;
     char f;
     char combine[100][3], reject[100][2], e[100];
     FILE *f1,*f2;
     f1=fopen(name,"r");
     f2=fopen("output","w");
     fscanf(f1,"%d",&t);
     for(int i=1;i<=t;i++){
             l=0;
             for(int j=0;j<=26;j++){
                     a[j]=0;
                     } 
             fscanf(f1,"%d",&c);
             fscanf(f1,"%c",&f);
             for( j=0;j<c;j++){
                     fgets(combine[j],4,f1);
                     }
             fscanf(f1,"%d",&d);
             fscanf(f1,"%c",&f);
             for(j=0;j<d;j++){
                     fgets(reject[j],3,f1);
                     }
                     fscanf(f1,"%d",&n);
                     fscanf(f1,"%c",&e[l]);
                     fscanf(f1,"%c",&e[l]);
                     l++;
                     a[e[l-1]-64]++;
             for(j=1;j<n;j++){
                     fscanf(f1,"%c",&e[l++]);
                     printf("\n%c",e[l-1]);
                     a[e[l-1]-64]++;
                     for( s=0;s<c;s++){
                          if((e[l-1]==combine[s][0]&&e[l-2]==combine[s][1])||(e[l-1]==combine[s][1]&&e[l-2]==combine[s][0])){
                                                                                                                         a[e[l-1]-64]--;
                                                                                                                         a[e[l-2]-64]--;
                                                                                                                         l=l-2;

                                                                                                                         e[l++]=combine[s][2];
                                                                                                                         break;
                                                                                                                         }
                                                                                                                         }
                                                                                                                        
                     for(s=0;s<d;s++){
                                      if(a[reject[s][0]-64]>0&&a[reject[s][1]-64]>0){
                                      
                                                                           for(int k=0;k<=26;k++)a[k]=0;
                                                                           l=0;
                                                                           break;
                                                                           }
                                                                           }
                                                                           }
                                                                           
             
             fprintf(f2,"Case #%d: [",i);
             for(j=0;j<l-1;j++){
                              fprintf(f2,"%c, ",e[j]);
                              }
             if(l==0)fprintf(f2,"]\n");
             else
             fprintf(f2,"%c]\n",e[l-1]);
             }
     fclose(f1);
     fclose(f2);
     return 0;
             }
             
             
                     
                     
                     
                     
                     
                     
