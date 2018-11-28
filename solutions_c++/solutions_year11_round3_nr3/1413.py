// 3.cpp : Defines the entry point for the console application.
//

#include<math.h>
#include <iostream>
using namespace std;
int n_row,n_col;
char s[50][50];


#include<stdio.h>
#include<conio.h>
int gcd2(int a,int b)
{
   if( b==0 )
        return a;
    else
        return gcd2(b,a%b);

}
int lcm2(int a,int b)
{
   return (a*b)/gcd2(b,a%b);

}
int hcf(int a[],int n)
{
	if(n==2)
		return gcd2(a[0],a[1]);
	else
		return gcd2(a[0],hcf(a+1,n-1));
}
int lcm(int a[],int n)
{
	if(n==2)
		return lcm2(a[0],a[1]);
	else
		return lcm2(a[0],lcm(a+1,n-1));
}

void solve()
{
	int i,j;
	int n,min,max,a[10000];
	cin>>n;
	cin>>min;
	cin>>max;
	for(i=0;i<n;i++)
	{
		cin>>a[i];
	}
	int gcd=hcf(a,n);
	
	int div1=(gcd)/(min);
	while(div1>0&&gcd/div1<=max)
	{
		if(gcd%div1==0&&gcd/div1<=max)
		{
			cout<<gcd/div1;
			return;
		}
		div1--;
	}

	gcd=lcm(a,n);
	
	int least=(((int)((min-1)/gcd))+1)*gcd;
	if(least<=max)
		cout<<least;
	else
		cout<<"NO";

}
void solveBrute()
{
	int i,j;
	int n,min,max,a[10000];
	cin>>n;
	cin>>min;
	cin>>max;
	for(i=0;i<n;i++)
	{
		cin>>a[i];
	}
	for(j=min;j<=max;j++)
	{
		for(i=0;i<n;i++)
		{
			if(a[i]%j==0||j%a[i]==0) continue;
			else break;
		}
		if(i==n)
		{
			cout<<j;
			return;
		}
		else
		{
			continue;
		}
	}
		cout<<"NO";

}
int main(int argc, char* argv[])
{
	int num_test;
	cin>>num_test;
	for(int i=0;i<num_test;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		solveBrute();
		cout<<"\n";
	}

	return 0;
}