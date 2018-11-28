#include<iostream>
//#include<conio.h>
#include<fstream>
using namespace std;
int main()
{
 long long a,b,i,j,k,l,m,n,t,x,s,p,c1,p1,d,flag,f;
 ifstream myfile ("in1.in");
   ofstream myfile1;
  myfile1.open ("out1.txt");
  if (myfile.is_open())
  {
   myfile>>t;i=1;
   while ( myfile.good())
    {
     myfile>>a>>b;
     int count=0;
     c1=0;
  s=a;
  while(s>0)
  {
   s=s/10;
   count++;
  }
  for(j=a;j<=b;j++)
  {
   p1=0;
   x=j;
   do
   {
   	flag=0;f=0;
   	s=count;
   	p=x%10;
	x=x/10;
	while(p==0&&s>2)
	{
	 p=x%10;
	 x=x/10;
	 flag++;
	}
	while(flag>1)
	 x*=10,f=1,flag--;
	if(f==1&&j%10!=0)
	  x+=p;
	while(s>1)
	{
	 p*=10;
	 s--;
    }
	x=p+x;
	if(x==j)
	 continue;
	if(x<=b&&x>=a&&x>j)
	c1++;
   }while(x!=j);		
  }
  if(i<=t)
  myfile1<<"\nCase #"<<i++<<": "<<c1<<"\n";
 }
}
 //getch();
 return 0;
}
   
