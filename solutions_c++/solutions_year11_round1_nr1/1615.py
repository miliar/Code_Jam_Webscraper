#include<iostream>
using namespace std;
int gcd(int a,int b)
{
 if(b>a)
{
int temp=a;
a=b;
b=temp;
}
if(b==0)return a;
else return gcd(b,a%b);
}
int gcd_hundred(long long int a)
{
a=a%100;
return gcd(a,100);
}	
int main()
{
long long int n;
int t,c=1;
int pd,pg;
cin>>t;
while(t)
{
 t--;
 cin>>n>>pd>>pg;
 int i,flag=0,solve=0;
 int v= 100/(gcd(pd,100)); 
 //cout<<v<<" ";
 for(i=1;i<=n;i++)
 {
	if(i%v==0)
	{
	flag=1;break;
	}
}
//cout<<flag<<" ";
if(flag==1)
{
// int num=pg/gcd(100,pg);
// int den=100/gcd(100,pg); 
if(pg==0)
{
if(pd==0)
solve=1;
}
if(pg==100)
{if(pd==100)solve=1;}
//cout<<pg<<" ";
if(pg!=100 && pg!=0) 
{
solve=1;//cout<<"yes";
}
}
if(solve==1)cout<<"Case #"<<c<<": "<<"Possible\n";
else cout<<"Case #"<<c<<": "<<"Broken\n";
c++;
}
return 0;
}
