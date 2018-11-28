#include<stdio.h>
#include<conio.h>
#include<process.h>
#include<fstream.h>
int main()
{
FILE *ifp, *ofp;
int arr[10000],brr[10000],i,j,n,k,t;
long int c=0;
 char outputfilename[]="asmall1.out";
  ifp=fopen("A5.in","r");

  if(ifp== NULL)
  {fprintf(stderr,"cant open the input file %s\n",ifp);
   exit(1);
  }

  ofp=fopen(outputfilename, "w");

  if(ofp == NULL)
  {
   fprintf(stderr,"cant open the output file %s\n", outputfilename);
   exit(1);
  }
  fscanf(ifp,"%d",&t);


for(k=0;k<t;k++)
{
fscanf(ifp,"%d",&n);
for(i=0;i<n;i++)
{
fscanf(ifp,"%d%d",&arr[i],&brr[i]);
}
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if(arr[i]<arr[j])
{
 if(brr[i]>brr[j])
 c++;
}
}
}
fprintf(ofp,"Case #%d: %d\n",k+1,c);
c=0;
}
printf("Enter");
getch();
return 0;
}