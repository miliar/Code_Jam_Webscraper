#include<iostream>
#include<stdio.h>
long p[8]={1,10,100,1000,10000,100000,1000000,10000000};
int map[2000001]={0};
int main()
{
 long int count,sum=0,num1,num,upper,A,B,k,j=0,T,orig,len=0;
 int cas,digit;
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 scanf("%ld",&T);
 for(cas=1; cas<=T; cas++)
 {

  count=0;
  sum=0;
  scanf("%ld%ld",&A,&B);
  for(j=A; j<=B; j++)
   map[j]=0;
  for(j=A; j<=B; j++)
  {
   count=1;
   if(map[j]==0)
   {
	//printf("\n%ld--",j);
    map[j]=-1;
    orig=j;
    len=0;
    while(orig!=0)
    {
      orig=orig/10;
      len++;
    }//end while
    num=j;
    upper=len-1;
    for(k=0; k<upper; k++)
    { 
     digit=num%p[k+1];
     digit=digit*p[upper-k];
     num1=num/p[k+1];
     digit+=num1;
     if(digit==j)
	;
     else if(digit<=B && digit/p[upper]!=0 && digit>=A && map[digit]==0 )
     {
	//printf("%ld,",digit);
	map[digit]=-1;
	count++;
     }//endif
    }//end for
    sum+=(count*(count-1))/2;
   }//end if  
  }//end for A B
  printf("Case #%ld: %ld\n",cas,sum);
 }
 return 0;
}