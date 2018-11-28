#include<iostream>
#include<stdlib.h>
using namespace std;
 
int check(int A , int i ,  int B , int digits)
{
int j,k,mark1,count=0,*a,*b,p=i,mark2=digits;
                                
a=new int[digits+1];
b=new int[digits+1];
for(j=digits;j>0;j--)
{
a[j]=p%10;
p=p/10;
}
while(mark2>0)
{
int h=1,value=0,l=1;
if(!a[mark2])
goto mark;
for(j=mark2;j<=digits;j++)
{
b[h]=a[j];
h++;
}
for(j=1;j<mark2;j++)
{
b[h]=a[j];
h++;
}
for(j=digits;j>0;j--)
{
value=value+b[j]*l;
l=l*10;
}
if(value>i && value<=B)
count++;
mark:
mark2--;
}
free(a);
free(b);
return count;
}
int main()
{
int k=1,t;
scanf("%d" , &t);
while(t--)
{
int A,B,i,j,p=10,count=0,digits=1;
scanf("%d" , &A);
scanf("%d" , &B);
while(A/p)
{
digits++;
p*=10;
}
for(i=A;i<B;i++)
{
count=count+check(A,i,B,digits);
}
printf("Case #%d: %d\n" , k , count);
k++;
}
return 0;
}