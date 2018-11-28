#include <iostream>
using namespace std;

int r,k,n,t;
long long income=0;
int g[10000];
int main()
{
	int c,i,p,q,time,summan;
	cin>>t;
	for (c=1; c<=t; c++)
	{
		bool flag=false;
		cin>>r>>k>>n;
		for (i=0; i<n; i++)
			cin>>g[i];
		p=0;
		for (time=0; time<r; time++)
		{
			q=p;
			summan=0;
			do
			{
				if (summan+g[q]<=k)
				{
					summan+=g[q];
					q++;
					if (q==n) q=0;
				}
				else break;
			} while (p!=q&&summan<k);
			income+=summan;
			p=q;
			if (p==0) 
			{
				flag=true;
				break;
			}
		}
		if (flag)
		{
		int multiply,left;
		time++;
		multiply=r/time;
		left=r%time;
		income*=multiply;
		for (time=0; time<left; time++)
		{
			q=p;
			summan=0;
			do
			{
				if (summan+g[q]<=k)
				{
					summan+=g[q];
					q++;
					if (q==n) q=0;
				}
				else break;
			} while (p!=q&&summan<k);
			income+=summan;
			p=q;
		}
		}
		cout<<"Case #"<<c<<": "<<income<<endl;
		income=0;
	}
	return 0;
}


