#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int powDig(int n)
{
	int powDig=1;
	while(n>0)
	{
		powDig*=10;
		n/=10;
	}
	return powDig;
}
int countDig(int n)
{
	int countDig=1;
	while(n>0)
	{
		countDig++;
		n/=10;
	}
	return countDig;
}

main()
{
	int t, i, numDig, nextPow, pow, m, n, j, a, b, count, k;
	cin>>t;
	for(i=0; i<t; i++)
	{
		cin>>a>>b;
		count=0;
		nextPow=powDig(a);
		numDig=countDig(a);
		pow=nextPow/10;
		for(j=a; j<b; j++)
		{
			n=j;
			if(j==nextPow)
			{
				pow=nextPow;
				nextPow*=10;
				numDig++;
			}	
			for(k=1; k<numDig; k++)
			{
				m=(n%10)*pow+n/10;
				if(m>j && m<=b)
					count++;
				n=m;
			}	
		}
		cout<<"Case #"<<(i+1)<<": "<<count<<endl;
	}
}
