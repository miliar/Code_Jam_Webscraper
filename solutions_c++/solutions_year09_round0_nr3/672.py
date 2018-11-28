#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char A[501];
char B[20];
int C[20];
int len;
main()
{
 freopen("C-large.in","r",stdin);
 freopen("C-large.out","w",stdout);
 int n;
 scanf("%d\n",&n);
 B[1]='w';
 B[2]='e';
 B[3]='l';
 B[4]='c';
 B[5]='o';
 B[6]='m';
 B[7]='e';
 B[8]=' ';
 B[9]='t';
 B[10]='o';
 B[11]=' ';
 B[12]='c'; 
 B[13]='o';
 B[14]='d';
 B[15]='e';
 B[16]=' ';
 B[17]='j';
 B[18]='a';
 B[19]='m';
 for(int i=1;i<=n;i++)
 {
  for(int j=0;j<=19;j++)
  {
   C[j]=0;	
  }
  C[0]=1;
  gets(A);
  len=strlen(A);
   for(int j=0;j<len;j++)
   {
	for(int k=1;k<=19;k++)
	{
	 if(A[j]==B[k])
	 {
		C[k]+=C[k-1];
		C[k]=C[k]%10000;
	 }
	}
   }
   
   printf("Case #%d: ",i);
    /* for(int j=0;j<=19;j++)
  {
   printf("C[%d]=%d\n",j,C[j]);
  }*/

   if(C[19]<10){printf("000");}
   else if(C[19]<100){printf("00");}
   else if(C[19]<1000){printf("0");}
   printf("%d\n",C[19]);	
 }
 return 0;
}
