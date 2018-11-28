#include<iostream>
#include<stdio.h>
int main()
{
 int T,S,p,t,j,cas,N,min,mins,count,countmin;
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 scanf("%d",&T);
 for(cas=1; cas<=T; cas++)
 {
  scanf("%d%d%d",&N,&S,&p);

  if(p==0)
  {
   for(j=0; j<N; j++)
	scanf("%d",&t);
   printf("Case #%d: %d\n",cas,N);
  }
    
  else if(p==1)
  {
    count=0;
    countmin=0;
    min=p+2*(p-1);
    mins=0;
    for(j=0; j<N; j++)
    {
     scanf("%d",&t);
     if(t>=min && t>=p)
	count++;
     else if(t>=mins && t>=p)
	countmin++;
    }//end for
    if(countmin<=S)
	count+=countmin;
    else if(countmin>S)
	count+=S;
   printf("Case #%d: %d\n",cas,count);
  }//end elseif
  else if(p>=2)
  {
    min=p+2*(p-1);
    mins=p+2*(p-2);
    count=0;
    countmin=0;
    for(j=0; j<N; j++)
    {
     scanf("%d",&t);
     if(t>=min&& t>=p)
	count++;
     else if(t>=mins&& t>=p)
	countmin++;
    }
    if(countmin<=S)
	count+=countmin;
    else if(countmin>S)
	count+=S;
   printf("Case #%d: %d\n",cas,count);
  }//end else if
 }//end for
 return 0;
}