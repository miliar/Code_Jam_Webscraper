//operator system:windows xp
//environment:vc++6.0
#include<stdio.h>
#include<string.h>
int switchnumber;

void switchto(char S[100][100],char Q[1000][100],int snumber,int qnumber,int nextbegin)
{
int max=0;
int count;
int i,j;
for(i=0;i<snumber;i++)
{
   count=0;
   for(j=nextbegin;j<qnumber;j++)
	   if(strcmp(S[i],Q[j])==0)break;
	   else count++;
   if(max<count)max=count;
}
if(max!=0)
{
nextbegin=max+nextbegin;
switchnumber++;
switchto(S,Q,snumber,qnumber,nextbegin);}
}
int main()
{
FILE *fp;
fp=fopen("c:\\out.txt","w");
char S[100][100];
char Q[1000][100];
int i,j;
int snumber,qnumber;
int N;
scanf("%d",&N);
for(i=0;i<N;i++)
{
   scanf("%d\n",&snumber);
   for(j=0;j<snumber;j++)
      gets(S[j]);
   scanf("%d\n",&qnumber);
   for(j=0;j<qnumber;j++)
	  gets(Q[j]);
   switchnumber=0;
if(qnumber!=0)
switchto(S,Q,snumber,qnumber,0);
else
switchnumber=1;
fprintf(fp,"Case #%d: %d\n",i+1,switchnumber-1);
}
fclose(fp);
return 0;
}