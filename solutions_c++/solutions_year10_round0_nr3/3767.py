#include<fstream>
#include<iostream>
using namespace std;

int main()
{
	ifstream f("12.in");
	int t;
	f>>t;
	ofstream g("12.out");
	for(int q=1;q<t+1;q++)
	{
		long long r, k, n;
		f>>r>>k>>n;
		long long poz=0, sol=0, a[2005];
		for(int i=0;i<n;i++)
			f>>a[i];
		while(r>0)
		{
			long long temp=0, pozst=poz;
			if((temp+a[poz]<k+1))
			{
				temp=temp+a[poz];
				poz++;
				poz=poz%n;
				while ((temp+a[poz]<k+1)&&(poz!=pozst))
				{
					temp=temp+a[poz];
					poz++;
					poz=poz%n;
				};
			};
			sol=sol+temp;
			r--;
		};
		g<<"Case #"<<q<<": "<<sol<<endl;
	};
}