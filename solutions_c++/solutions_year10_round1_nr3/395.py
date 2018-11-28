#include<iostream>
#include<fstream>
using namespace std;

int T;
int A1,A2,B1,B2;
int count;

/*
int fun(int a,int b,int n)	//n为循环轮数 从0开始
{
	int k;
	if((a<=0 || b<=0)&& n%2==0)
	{
		count++;
		return 0;
	}
	if((a<=0 || b<=0)&& n%2==1)
	{
		return 0;
	}

	if(a>b)
	{
		for(k=1;b*k<a;k++)
		{
			fun(a-b*k,b,n+1);
		}
	}
	else if(a==b)
		fun(0,b,n+1);
	else
	{
		for(k=1;a*k<b;k++)
		{
			fun(b-a*k,a,n+1);
		}
	}
	return 0;

}

*/
int fun(int a,int b,int n)	//n为循环轮数 从0开始
{
	if((a<=0 || b<=0)&& n%2==0)
	{
		count++;
		return 0;
	}
	if((a<=0 || b<=0)&& n%2==1)
	{
		return 0;
	}

	if(n%2==1 && (a/b>=2 || b/a>=2))
		return 0;

	if(a>b)
	{
		if(a%b!=0)
		{
			fun(a%b,b,n+1);
			if(a%b+b<a)
				fun(a%b+b,b,n+1);
		}
		if(a%b==0)
		fun(b,b,n+1);
	}
	else if(a==b)
		fun(0,b,n+1);
	else
	{
		if(b%a!=0)
		{
			fun(b%a,a,n+1);
			if(b%a+a<b)
				fun(b%a+a,a,n+1);
		}
		if(b%a==0)
		fun(a,a,n+1);
	}
	return 0;

}
/*
int fun(int a,int b,int n)
{
	int turn=0;
	while(a>0 && b>0)
	{
		if(turn % 2==0)
		{
			if(a>b && a%b!=0)
				a=a%b;
			else if(a>b && a%b==0)
				a=b;
			else if(a==b)
				a=0;
		}
		else
		{
			if(b>a && b%a!=0)
				b=b%a;
			else if(b>a && b%a==0)
				b=a;
			else if(b==a)
				b=0;
		}
		turn ++;

		if(a<=0)
			return 0;
		if(b<=0)
			return 1;
	}
}
*/

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("3.out");
	fin>>T;
//	int A,B;
	int i,j;
	for(int n=1;n<=T;n++)
	{
		count=0;
		fin>>A1>>A2>>B1>>B2;
		for(i=A1;i<=A2;i++)
		{
			for(j=B1;j<=B2;j++)
			{
				if(i>j)
					fun(i,j,0);
				else
					fun(j,i,0);
			}
		}
		fout<<"Case #"<<n<<":"<<" "<<count<<endl;
		cout<<"Case #"<<n<<":"<<" "<<count<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}