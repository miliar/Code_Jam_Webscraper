#include<stdio.h>
#include<string.h>
#include<math.h>
void main()
{
 char str[100],*p;
 int t,t1,arr[100];
 int b,i,j;
 double ans;
 printf("Enter input file name:");
 scanf("%s",str);
 FILE *readf=fopen(str,"r");
 printf("Enter output file name:");
 scanf("%s",str);
 FILE *writef=fopen(str,"w");
 fscanf(readf,"%d",&t);
 fgets(str,100,readf);
 t1=t;
 while(t)
 {
  t--;
  fgets(str,100,readf);
  b=0;
  i=1;
  arr[0]=1;
  while(str[i]!='\n')
  {
   p=strchr(str,str[i]);
   if(p==str+i)
   {
    arr[i]=b;
    if(b==0)
     b++;
    b++;
   }
   else
    arr[i]=arr[p-str];
   i++;
  }
  ans=0;
  if(b==0)
   b=2;
  for(j=i-1;j>=0;j--)
   ans+=(pow(b,j)*arr[i-j-1]);

  fprintf(writef,"Case #%d: %.0lf\n",t1-t,ans);
 }
}