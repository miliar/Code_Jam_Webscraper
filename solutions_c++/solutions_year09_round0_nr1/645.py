#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char A[5001][16];
char B[5001];
int C[16][27];
int at;
int ans;
int p;
main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
 int len,n,m;
 scanf("%d%d%d\n",&len,&n,&m);
 for(int i=1;i<=n;i++)
 {
 gets(A[i]);
 }

 for(int i=1;i<=m;i++)
 {
	 gets(B);
	at=0;
	ans=0;
	for(int j=0;j<=len;j++)
	{
	 for(int k=0;k<=26;k++)
	 {
	 C[j][k]=0;	
	 }
	}
	p=strlen(B);
  for(int j=0;j<p;)
  {
   if(B[j]=='(')
   {
//	printf("At j = %d is (\n",j,B[j]);
	j++;
    while(B[j]!=')')
    {
	// printf("At j = %d is %c\n",j,B[j]);
	 C[at][B[j]-'a']=1;
	 j++;
	}
	//printf("At j = %d is )\n",j,B[j]);
	j++;
   }	
   else
   {
   C[at][B[j]-'a']=1;
   j++;	
   }
   at++;
  }
  for(int j=1;j<=n;j++)
  {
   for(int k=0;k<len;k++)
   {
	if(C[k][A[j][k]-'a']==0){k=len;}
	else if(k==len-1){ans++;}
   }
  }
  printf("Case #%d: %d\n",i,ans);
  /*for(int j=0;j<len;j++)
  {
  	for(int k=0;k<26;k++)
  	{
	 printf("%d ",C[j][k]);	
	}
	printf("\n");
  }*/
 }
 return 0;
}
