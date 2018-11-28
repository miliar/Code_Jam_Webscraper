#include<stdio.h>
#include<conio.h>
#define name "A-large.in"
int abs(int a){
    if(a<0)return -a;
    else 
         return a;
}
int  main()
{
     int o=1,b=1,n,n1,t=1,to=0,tb=0,f,m[100];
     char c;
     FILE *f1,*f2;
     f1=fopen(name,"r");
     f2=fopen("output","w");
     fscanf(f1,"%d",&n);
     printf("n=%d",n);
     getch();
     for(int i=1;i<=n;i++){
                       fscanf(f1,"%d",&n1);
                       printf("n1=%d",n1);                      
                       t=0;o=1;b=1,to=0;tb=0;
                       for(int j=1;j<=n1;j++){
                                              fscanf(f1,"%c",&c);
                                              fscanf(f1,"%c",&c);
                                              if(c=='O'){
                                                     fscanf(f1,"%d",&f);
                                                     if(abs(o-f)<tb){t=t+1;to=1;}
                                                     else{
                                                     t=t+abs(o-f)+1-tb;
                                                     to=to+abs(o-f)+1-tb;
                                                     }
                                                     tb=0;
                                                     o=f;
                                                    }
                                              if(c=='B'){
                                                     fscanf(f1,"%d",&f);
                                                     if(abs(b-f)<to){t+=1;tb=1;}
                                                     else {
                                                     t=t+abs(b-f)+1-to;
                                                     tb=tb+abs(b-f)+1-to;
                                                     }
                                                     to=0;
                                                     b=f;
                                                     printf("tb=%d",tb);
                                                     }
                                                     }
                                                     
                                          
                                                        
                                                        
                                                        
                       fprintf(f2,"Case #%d: %d\n",i,t);
                       printf("%d\n",t);
                       }
     fclose(f1);
     fclose(f2);
     getch();
     return 0;
}
                                                         
                                                    
                                                    
                                                    
                                                    
                                          
                                          
                       
