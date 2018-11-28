#include<stdio.h>
#include<iostream.h>
int main()
{
int i,m,temp;
cin>>m;
int x=0;
while(m--)
{
x++;
int K;
cin>>K;
int J;
cin>>J;
int L;
cin>>L;
int countL=0,JcountL=0;
int m1,m2;
for(int s=0;s<K;s++)
{
cin>>temp;
m1=temp%3;
m2=temp/3;
if((m2)>=L)
{
countL++;
}
else
{
if(((m2)==(L-1)))
{
if(m1==0 && JcountL<J && (m2)-1>=0)
{
JcountL++;
countL++;
}
else if(m1>0)
countL++;

}
else
{
if((((m2)==(L-2)) && (m1==2)) && (JcountL<J))
{
JcountL++;
countL++;
}
}
}
}
cout<<"Case #"<<x<<": "<<countL<<"\n";
}
return 0;
}
