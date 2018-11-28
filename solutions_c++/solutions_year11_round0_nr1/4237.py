#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char s[500];
long str[500],n;

long find_next_pos(long c,long pos) //pos means current position in input string s
{
 long ret,i;
 if(c==0)
 {
  for(i=pos+1;i<n*4;i++)
  {
   if(str[i]==0)
   {
    ret=str[i+2];
    break;
   }
  }
 }
 else
 {
 for(i=pos+1;i<n*4;i++)
  {
   if(str[i]==1)
   {
    ret=str[i+2];
    break;
   }
  }
 }
 return ret;
}

long power(long n)
{
 long ret=1,i;
 for(i=0;i<n;i++) ret*=10;
 return ret;
}

int main()
{
  freopen("A-small-attempt1.in","r",stdin);
  freopen("aSmall.out","w",stdout);
 long f[200],i,j,t,cas=1,o[200],b[200],po,pb,value,need,next,cost,index,pr;
 scanf("%ld",&t);
 while(t--)
 {
  scanf("%ld",&n);
  gets(s);
  
  po=1;
  pb=1;
  cost=0;
  for(i=0;i<200;i++) str[i]=-1;
  index=n;
  
  for(i=strlen(s)-1;i>0;)
  {
  // printf("\n%ld ||",i);
   value=0;j=i;pr=0;
   while(1)
   {
    if(s[j]==' ') {
               //printf("%ld ",j);
               break;
               }
    value+=(s[j]-48)*power(pr);
    pr++;
    j--;
   }
   str[index*4-1]=value;
   if(s[j-1]=='O') str[index*4-3]=0;
   else str[index*4-3]=1;
   index--;
   i=j-3;
  }
  //for(i=1;i<n*4;i++) if(str[i]!=-1) printf("%ld ",str[i]);
  for(i=1;i<n*4;i+=4)
  {
   //printf("Pos org- %ld\n",po);
   //printf("Pos blue- %ld\n\n",pb);
   
   if(str[i]==0)
   {
    value=str[i+2];
    need=abs(value-po)+1;
    po=value;
    cost+=need;
    
    next=find_next_pos(1,i);
    
    if(next>pb)  
    {
     if(next<=pb+need) pb=next;
     else pb=pb+need;
    }
    else if(next<pb)
    {
     if(pb-need<=next) pb=next;
     else pb=pb-need;
    }
    
   }   //end of if s[i]=='0'
   
   else
   {
    value=str[i+2];
    need=abs(value-pb)+1;
    pb=value;
    cost+=need;
    
    next=find_next_pos(0,i);
    
    if(next>po)  
    {
     if(next<=po+need) po=next;
     else po=po+need;
    }
    else if(next<po)
    {
     if(po-need<=next) po=next;
     else po=po-need;
    }
    
   }
   
  }  
  printf("Case #%ld: %ld\n",cas++,cost);
 }
 return 0;
}
