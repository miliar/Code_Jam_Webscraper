#include<stdio.h>
//#include<conio.h>
#include<stdlib.h>
int main(void)
{
    FILE *fs, *ft;
    char ch;
    int flag=0,count=0,flag1=0,flag2=0,times=0;;
    fs=fopen("A-small-attempt4.in","r");
    ft=fopen("out.out","w");
    char map[]="yhesocvxduiglbkrztnwjpfmaq",num[4]={0};
    
                         fgets(num,4,fs);
                         times=atoi(num);
                         //printf("%d",times);
                         fseek(fs,0,SEEK_SET);
    while(1)
    {
            
            ch=fgetc(fs);
            if(ch==EOF)
            break;
            else{
                 
                 if(flag1==1)
                 {
                       fprintf(ft,"Case #%d: ",count);
                       flag1=0;      
                            }
                 if(ch>=97 && ch<=122){
                 putc(map[ch-97],ft);
                 flag2=0;
                 }
                 else if(ch>=48 && ch<=57){
                      //printf("1");
                       //fgets(num,4,fs);
                       //times=atoi(num);
                       //printf("%d",times);
                      flag=1;
                      flag2=1;
                      }
                 //putc(,ft);
                 else if((ch=='\n' || ch=='\r') && flag2==0)
                 {
                      count++;
                      if(count<=times)
                      putc(ch,ft);
                      flag1=1;
                      //fprintf(ft,"Case #%d:",count);
                  }
                 else{
                 if(flag==0)
                 putc(ch,ft);
                 flag=0;
                 if((ch=='\n' || ch=='\r') && flag2==1){
                 count++;
                 flag1=1;}
                 }
                 }
            }
            fclose(fs);
            fclose(ft);
   // getch();
    return 0;
}
