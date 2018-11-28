#include<stdio.h>
#include<iostream.h>

long count,n,cas,cas1;
char temp[109];
void make(long p,long long q,long long r,long s)
{
if(p==n)     
{
if(s==0)
q=q+r;
else
q=q-r;
long flag=0;
if(q%2==0)
flag=1;
if(q%3==0)
flag=1;
if(q%5==0)
flag=1;
if(q%7==0)
flag=1;
if(flag==1)
count++;            
}     
else
{

if(r>0)
make(p+1,q,r*10+temp[p]-48,s);
else
make(p+1,q,r*10-(temp[p]-48),s);    
if(p!=0)
{
if(s==0)
{
make(p+1,q+r,temp[p]-48,0);    
make(p+1,q+r,(temp[p]-48),1);
}
else
{
make(p+1,q-r,temp[p]-48,0);    
make(p+1,q-r,(temp[p]-48),1);
    
}
}
}     
}

int main()
{
 ////////  freopen("b.in.txt","r",stdin);
 /////////  freopen("b_small_out.in","w",stdout);    
 
cin>>cas;

for(cas1=1;cas1<=cas;cas1++)
{
scanf("%s",temp);                            
n=strlen(temp);
count=0;
make(0,0,0,0);

printf("Case #%ld: %ld\n",cas1,count);                            
                            
                            
}    
    
    

return 0;    
}
