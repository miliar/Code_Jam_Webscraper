#include<stdio.h>
#include<string.h>
#include<conio.h>
#include<stdlib.h>
int main()
{
int l=0,d=0,n=0,i,j=0,in,vt=0,xx=0,flag=0,vl=0,ar,len=0,p=0,cnt=0,cnf=0,dc=0,tc=0,q=0,ik=0,jk=0;
char ls[30][15],test[15][2500],xar[300],x,y,g,ch,f[30],ms[50];
int ldn[3]={0},finlen[300]={0};
FILE *fin,*fout;
clrscr();
printf("enter input file name");
scanf("%s",f);
fin=fopen(f,"r");
while(1)
{
 ch=fgetc(fin);
 if(ch=='\n')
 {ik++;jk++;j=0;cnf++;}
 if(ch!=' '&&cnf<3)
 {
  if(flag<2){
  xx=(xx*10)+(ch-48);
  flag++;}
  if(flag==2){
  ldn[q]=xx;flag=0;xx=0;
  q++;cnf++;}
 }
 else if(ch!='\n'&&((cnf>=3)&&(cnf<=(ldn[1]+2))))
 {
  ls[ik-1][j++]=ch;
  jk=0;
 }
  else if(ch!='\n'&&((cnf>=ldn[1]+3)&&(cnf<=ldn[1]+ldn[2]+2)))
 {
  test[jk-1][j++]=ch;

 }
 if(ch==EOF) break;
}
fclose(fin);
for(i=0;i<ldn[1];i++)
printf("%s\n",ls[i]);
for(i=0;i<ldn[2];i++)
printf("%s\n",test[i]);

/*printf("enter l-length\nd-no.of words\nn-no.of test cases");
scanf("%d%d%d",&l,&d,&n);
printf("enter the %d words of length %d",d,l);
for(i=0;i<d;i++)
scanf("%s",&ls[i]);
printf("enter the %n test cases",n);
for(i=0;i<n;i++)
scanf("%s",&test[i]); */

/*for(i=0;i<ldn[2];i++)
{
cnt=0;
for(in=0;in<ldn[1];in++)
{ vl=0;vt=0;len=0;
  while(test[i][vt]!=NULL)
  {
   if(vl>ldn[0]) break;
   y=ls[in][vl];
   x=test[i][vt];
   if(x!='(')
   {
    if(x==y)
    len++;
    else break;
   }
   if(x=='(')
   {
    vt++;
    x=test[i][vt];
    ar=0;
    while(x!=')')
    {
	xar[ar]=test[i][vt];
	vt++;
	ar++;
	x=test[i][vt];
    }
    xar[ar]=NULL;
    g=xar[0];p=0;
    while(g!=NULL)
    {
	g=xar[p];
	if(y==g) len++;
	p++;
    }
   }

   vt++;
   vl++;
  }
  if(len==ldn[0])
  {
   len=0;
   cnt=cnt+1;
   finlen[i]=cnt;
  }
}
}
printf("\nOut put");
for(i=0;i<ldn[2];i++)
printf("\ncase #%d: %d",i+1,finlen[i]); */
getch();
return 0;
}