#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
using namespace std;
struct c
{
int pos;
int value;
int sum;
};
int main()
{
int n,i,j;int count1=0;
cin>>n;
char a1;
scanf("%c",&a1);
while(n--)
{ count1++;
  char a[501],b[19]; c b1[19][501];int counta[19];
  gets(a);
  
  strcpy(b,"welcome to code jam\0"); 
  for(i=0;i<19;i++)counta[i]=0;
  for(i=0;i<strlen(b);i++)
   for(j=0;j<strlen(a);j++)
    if(a[j]==b[i])
    {
     b1[i][counta[i]++].pos=j;
     if(i==0)
       {b1[0][counta[i]-1].value=1;
        b1[0][counta[i]-1].sum=counta[i];}
    }
  for(i=1;i<=18;i++)
   {
 for(j=0;j<counta[i];j++)
      {
       
       int k=0;
       while (b1[i-1][k].pos<b1[i][j].pos && k<counta[i-1])k++;
       if(k!=0)
       b1[i][j].value=b1[i-1][k-1].sum;
       else
       b1[i][j].value=0;
       if(j!=0)
       b1[i][j].sum=(b1[i][j-1].sum+b1[i][j].value)%10000;
       else
       b1[i][j].sum=(b1[i][j-1].sum+b1[i][j].value)%10000;
  //     cout<<b1[i][j].sum<<" ";
     } 
// cout<<endl;
}
   if(b1[18][counta[18]-1].sum==0)
   cout<<"Case #"<<count1<<": 0000"<<endl;
   else if(b1[18][counta[18]-1].sum<10)
   cout<<"Case #"<<count1<<": 000"<<b1[18][counta[18]-1].sum<<endl;
   else if(b1[18][counta[18]-1].sum<100)
   cout<<"Case #"<<count1<<": 00"<<b1[18][counta[18]-1].sum<<endl;
   else if(b1[18][counta[18]-1].sum<1000)
   cout<<"Case #"<<count1<<": 0"<<b1[18][counta[18]-1].sum<<endl;
   else if(b1[18][counta[18]-1].sum<10000)
   cout<<"Case #"<<count1<<": "<<b1[18][counta[18]-1].sum<<endl;
}
return 0;
}
