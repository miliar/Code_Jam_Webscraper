#include<stdio.h>
#include<conio.h>
FILE *fp,*fp1;


void sort(float x[200],int z)
{

 int i,j;
 for(i=0;i<z;i++)
  {
    for(j=0;j<z;j++)
    {
       if(x[i]<x[j])
	    {
		  float t=x[i];
		  x[i]=x[j];
		  x[j]=t;
		}
	}
  }






}
int  countreq(float aneed[200],float aavail[200],int ab,int ba)
{
 int j=0,c=0,i;
 for(i=0;i<ab;i++)
 {
   if(aneed[i]<aavail[j])
    c++;
    else
	 j++;
   if(j==ba)
   {
     c=c+ab-i-1;
     break;
    }
 }
 return c;
 }

void count(int *x,int *y)
{
 int ab,ba,i,xy,outtimea=0,outtimeb=0;
 float turntime;
 float aneed[200],aavail[200],bneed[200],bavail[200];

 fscanf(fp,"%f",&turntime);

 fscanf(fp,"%d%d",&ab,&ba);
 for(i=0;i<ab;i++)
 {
   fscanf(fp,"%f%f",&aneed[i],&bavail[i]);
   xy=(int)(bavail[i]*100);
   if(xy%100>=60-turntime)
   {
     bavail[i]+=1.0-(60-turntime)/(float)100;
   }

   else bavail[i]+=turntime/(float)100;
 }

  for(i=0;i<ba;i++)
 {

     fscanf(fp,"%f%f",&bneed[i],&aavail[i]);
	xy=(int)(aavail[i]*100);
   if(xy%100>=60-turntime)
   {
     aavail[i]+=1.0-(60-turntime)/(float)100;
   }
   else
    aavail[i]+=turntime/(float)100;
 }
 sort(aneed,ab);
 sort(aavail,ba);
 sort(bneed,ba);
 sort(bavail,ab);
 *x=countreq(aneed,aavail,ab,ba-outtimea);
 *y=countreq(bneed,bavail,ba,ab-outtimeb);
}
void LinkFloat()
{
 float a,*b;
 b=&a;
 a=*b;
}






void main()

{
 int n,x[200],y[200],i;

 FILE *fp2;
 char ch;
 char file[200];
 clrscr();



 printf("enter input file name and output will be stored in current directory output.txt file\n");
 scanf("%s",&file);
 fp=fopen(file,"r+");
 fp2=fopen("input.txt","w");



 while(1)
 {
  ch=fgetc(fp);
  if(ch==EOF) break;
  if(ch==':')
   ch='.';

  fputc(ch,fp2);
 }
 fclose(fp2);
 fclose(fp);
 fp=fopen("input.txt","r");

 fp1=fopen("output.txt","w");
 clrscr();
 fscanf(fp,"%d",&n);
 for(i=0;i<n;i++)
 {
 //count will store for each casegf
  count(&x[i],&y[i]);
 }
 for(i=0;i<n;i++)
 {
   fprintf(fp1,"Case #%d: %d %d\n",i+1,x[i],y[i]);
 }
 fclose(fp);
 fclose(fp1);
}
