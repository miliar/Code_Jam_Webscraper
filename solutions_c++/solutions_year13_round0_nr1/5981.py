#include<stdio.h>
#include<conio.h>
#include<string.h>

int main()
{
 int i,j,k,flag,z1,z2,f;
 char a[4][5];
 char b[5];
 FILE *f1,*f2;
 f1=fopen("input1.txt","r");   
 f2=fopen("out1.txt","w");    
 
 fscanf(f1,"%d",&k);   
    
    for(i=1;i<=k;i++)
    {
                     
                     
                     flag=0;
                     for(j=0;j<4;j++)
                   {
                                       fscanf(f1,"%s",a[j]);
                     if(!strcmp(a[j],"XXXT") ||!strcmp(a[j],"XXTX") ||!strcmp(a[j],"XTXX") ||!strcmp(a[j],"TXXX") || !strcmp(a[j],"XXXX"))
                     {
                                             fprintf(f2,"Case #%d: X won\n",i);
                                             flag=1;
                     }
                     else if(!strcmp(a[j],"OOOT") ||!strcmp(a[j],"OOTO") ||!strcmp(a[j],"OTOO") ||!strcmp(a[j],"TOOO")|| !strcmp(a[j],"OOOO"))
                     {
                          fprintf(f2,"Case #%d: O won\n",i);
                          flag=1;
                          }
                           
                     }  
                     
                     if(flag==0){         
    for(j=0;j<4;j++)
    b[j]=a[j][j];
    b[4]='\0';
    if(!strcmp(b,"XXXT") ||!strcmp(b,"XXTX") ||!strcmp(b,"XTXX") ||!strcmp(b,"TXXX")|| !strcmp(b,"XXXX"))
{                     fprintf(f2,"Case #%d: X won\n",i);flag=1;
}
                     else if(!strcmp(b,"OOOT") ||!strcmp(b,"OOTO") ||!strcmp(b,"OTOO") ||!strcmp(b,"TOOO")|| !strcmp(b,"OOOO"))
{                     fprintf(f2,"Case #%d: O won\n",i);flag=1;
}
}
if(flag==0)
{
    for(j=0;j<4;j++)
    b[j]=a[j][3-j];
    b[4]='\0';
    if(!strcmp(b,"XXXT") ||!strcmp(b,"XXTX") ||!strcmp(b,"XTXX") ||!strcmp(b,"TXXX")|| !strcmp(b,"XXXX"))
{                     fprintf(f2,"Case #%d: X won\n",i);flag=1;}
                     else if(!strcmp(b,"OOOT") ||!strcmp(b,"OOTO") ||!strcmp(b,"OTOO") ||!strcmp(b,"TOOO")|| !strcmp(b,"OOOO"))
                     {fprintf(f2,"Case #%d: O won\n",i);flag=1;}
}
if(flag==0)
{                    
                     
for(z1=0;z1<4;z1++)
{
 for(z2=0;z2<4;z2++)
  b[z2]=a[z2][z1];                     
    b[5]='\0';
                     
                      if(!strcmp(b,"XXXT") ||!strcmp(b,"XXTX") ||!strcmp(b,"XTXX") ||!strcmp(b,"TXXX")|| !strcmp(b,"XXXX"))
{                     
                      fprintf(f2,"Case #%d: X won\n",i);flag=1;
                      }
                     else if(!strcmp(b,"OOOT") ||!strcmp(b,"OOTO") ||!strcmp(b,"OTOO") ||!strcmp(b,"TOOO")|| !strcmp(b,"OOOO"))
{                     fprintf(f2,"Case #%d: O won\n",i);flag=1;
}
                     
}                     
}                  
 if(flag==0)
 {
            f=0;
            for(z1=0;z1<4;z1++)
            {
            for(z2=0;z2<4;z2++)
            if(a[z1][z2]=='.')
            f=1;
            
            } 
                       
            
            if(f==1)
 fprintf(f2,"Case #%d: Game has not completed\n",i);   
  else
  fprintf(f2,"Case #%d: Draw\n",i);
}

}

getch();
}
