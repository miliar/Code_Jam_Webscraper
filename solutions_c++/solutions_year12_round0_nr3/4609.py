#include<stdio.h>
#include<ctype.h>
#include<stdlib.h>
#include<string.h>
//#include<conio.h>

int main(void)
{
    //printf("%d",atoi("0945"));
    FILE *fs, *ft;
    char ch;
     fs=fopen("C-small-attempt0.in","r");
     ft=fopen("out1.out","w");
     int times=0,loc=0,count=0,n1,n2;
     char num[4]={0},s[20]={0},*p=NULL,c1,c2;
     int pairCount=0;
     
    
     fgets(num,4,fs);
     times=atoi(num);
                         //printf("%d",times);
     fseek(fs,0,SEEK_SET);
     while(fgets(s,15,fs)!=NULL)
     {
                               // printf("1");
                               pairCount=0;
                                char num1[5]={0},num2[5]={0};
                                //printf("%d\n",strlen(s));
                                p=strchr(s,' ');
                                
                                if(p!=NULL){
                                count++;
                                loc=p-s;
                                strncpy(num1,s,loc);
                                //printf("%s",num1);
                                strrev(s);
                                strncpy(num2,s,strlen(s)-loc-1);
                                strrev(num2);
                                //printf(" %s\n",num2);
                                if(num2[strlen(num2)]==10)
                                num2[strlen(s)-loc-2]=0;
                                
                                //printf("%s %s\n",num1,num2);
                                if(strlen(num1)==1 && strlen(num2)==1){
                                                   //printf("2");
                                fprintf(ft,"Case #%d: 0",count);
                                if(count<times)
                                fputc('\n',ft); 
                                }
                                
                                else{
                                     n1=atoi(num1);
                                     n2=atoi(num2);
                                     while(n1<=n2)
                                     {
                                               if(strlen(num1)==1)
                                               {
                                                                  n1++;
                                                                  itoa(n1,num1,10);
                                                                  }
                                                                  else if(strlen(num1)==2)
                                                                  {
                                                                       
                                                                       strrev(num1);
                                                                       if(atoi(num1)<=n2 && atoi(num1)>n1){
                                                                                         //printf("%s ",num1);
                                                                       pairCount++;
                                                                       }
                                                                       
                                                                       strrev(num1);
                                                                       n1++;
                                                                      itoa(n1,num1,10);
                                                                   }
                                                                   else if(strlen(num1)==3)
                                                                   {
                                                                        c1=num1[0];
                                                                        num1[0]=num1[2];
                                                                        c2=num1[1];
                                                                        num1[1]=c1;
                                                                        num1[2]=c2;
                                                                        if(atoi(num1)<=n2 && atoi(num1)>n1){
                                                                       // printf("%s ",num1);
                                                                        pairCount++;
                                                                        }
                                                                        
                                                                        c1=num1[0];
                                                                        num1[0]=num1[2];
                                                                        c2=num1[1];
                                                                        num1[1]=c1;
                                                                        num1[2]=c2;
                                                                        
                                                                        if(atoi(num1)<=n2 && atoi(num1)>n1){
                                                                       // printf("%s ",num1);
                                                                        pairCount++;
                                                                        }
                                                                        
                                                                        c1=num1[0];
                                                                        num1[0]=num1[2];
                                                                        c2=num1[1];
                                                                        num1[1]=c1;
                                                                        num1[2]=c2;
                                                                        
                                                                        
                                                                        n1++;
                                                                      itoa(n1,num1,10);
                                                                        
                                                                        
                                                                    }   
                                                  }
                                                  if(strlen(num1)!=1 || strlen(num2)!=1)
                                                  fprintf(ft,"Case #%d: %d",count,pairCount); 
                                                  
                                                  if(count<times)
                                                  fputc('\n',ft); 
                                     }
                                     
                                }
                                
                                //printf("%d",loc); 
                                }
   // getch();
    return 0;
}
