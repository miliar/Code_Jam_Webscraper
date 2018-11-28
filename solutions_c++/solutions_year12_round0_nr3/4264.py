#include<iostream>
#include<cmath>

using namespace std;

int d1,d2,temp1,temp2,temp3,lp,fp,newno,A[1001][1001],ans1,a,b,t;

int noofdigits(int a)
{
  if(a<10)
    return 1;
  if(a<100)
    return 2;
  if(a<1000)
    return 3;
  else
    return 4;
}

int isrecy(int a,int b)
{
  if(a==b)
    return 0;
  d1=noofdigits(a);
  d2=noofdigits(b);
  
  if(d1!=d2)
    return 0;
  
  temp2=1;
  temp3=pow(10,d2);
  for(int i=1;i<=d2;i++)
  {
    lp=b % temp2;
    fp=b/temp2;
    newno=(lp*temp3)+fp;
    temp3/=10;
    temp2*=10;
    
    if(newno==a)
      return 1;
  }
  return 0;
}
    
    
  
  

int main()
{
  for(int i=1;i<=1000;i++)
    for(int j=1;j<=1000;j++)
    {
      if(isrecy(i,j)==1)
	A[i][j]=1;
      else
	A[i][j]=0;
    }
    
  cin>>t;
  for(int q=1;q<=t;q++)
  {
    cin>>a>>b;
    ans1=0;
    for(int i=a;i<=b;i++)
      for(int j=i+1;j<=b;j++)
      {
	if(A[i][j]==1)
	  ans1++;
      }
      cout<<"Case #"<<q<<": "<<ans1<<endl;
  }
}
  