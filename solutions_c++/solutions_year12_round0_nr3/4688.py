#include<iostream>
#include<cmath>
#include<fstream>
#include<string>
using namespace std;
bool recy(int x, int y);
int digit(int x);
int main(int argc,char*argv[])
{
	freopen("inin.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int a,b,count=0,n;
	cin>>n;
	for(int k=0;k<n;k++)
	{
		count=0;
		cin>>a>>b;
		for(int i=a;i<b;i++)
		{
			//count = count +recy(i,b);
			for(int j=i+1;j<=b;j++)
			{
				if( recy(i,j) ){count++;}
			}
		}
		cout<<"Case #"<<k+1<<": "<<count<<"\n";
	}
}
int digit(int x)
{
	int count=0;
	while(x != 0)
	{
		x = x/10;
		count++;
	}
	return count;
}
bool recy(int q,int y)
{
	string s;
	int x=q,k = digit(x),tem=0,p=0;
	if(k != digit(y)){cout<<"different no of digits\n";return false;}
	for(int i=1;i<k;i++)
	{
			p = x/((int)pow(10,k-1));
			tem=x%((int)pow(10,k-1));
			tem=tem*10+p;
			if(tem==y)
				{return true;break;}
			else
				{x=tem;}

	}
	return false;
}
/*int recy(int x,int b)
{
	int k=digit(x),count = 0,q=x,tem=0,p=0;
	for(int i=1;i<k;i++)
	{
			p = x/((int)pow(10,k-1));
			tem=x%((int)pow(10,k-1));
			tem=tem*10+p;
			if(tem <= b && (tem>q && q<b ))
				{cout<<"x: "<<q<<" tem: "<<tem<<"\n";count++;}
			x=tem;

	}
	return count;
}*/