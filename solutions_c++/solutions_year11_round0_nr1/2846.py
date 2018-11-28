#include<iostream>
#include<cstdio>
#include<cmath>
#include <fstream>
using namespace std;
ifstream fin("D:\\acm\\pb\\A-large.in");
ofstream fout("D:\\acm\\pb\\A-large.out");
 
#define cin fin
#define cout fout

int _max(int x, int y)
{
	return x>y?x:y;
}

int main()
{
	int a , b ;
	int p , q ;
	int s , t;
	char ch;
	int T , n ; 
	int i , m , sum;
	cin>>T;
	sum = 0;
	while( T-- )
	{
		cin>>n;

		p =0;
		q = 0;
		a =1;
		b = 1;
		sum++;
		for(i=0;i<n;++i)
		{
			cin>>ch>>m;

			if(ch=='O')
			{
				t=abs(m-a)+1;
				if(t+p>q+1)   p=t+p;
				  else   p=q+1;
				  a=m;
			}
			else
			{ 
				s=abs(m-b)+1;
				if(s+q>p+1) 	q=s+q;
				    else	q=p+1;
				     b=m;
			}
		}
		int MAX=_max(p  ,  q);
           cout<<"Case #"<<sum<<": "<<MAX<<endl;
	}
	return 0;
}