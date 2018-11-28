#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;


int main()
{
	ifstream cin("C-large.in");
	ofstream cout("output.txt");
	long T;
	cin>>T;
	
	for(long q=0;q<T;q++)
	{
		long long kol=0;
		long a,b;
		cin>>a>>b;
		long st=0;
		{
			long aa=a;
			while(aa!=0)
			{
				st++;
				aa/=10;
			}
		}
		long ch=1;
		for(long i=1;i<st;i++)
			ch*=10;

		vector <bool> mass(b+1,false);

		for(long i=a;i<=b;i++)
		{
			if(mass[i]==false)
			{
				mass[i]=true;
				long long koll=1;
				long ii=i;
				for(long j=1;j<st;j++)
				{
					ii=(ii%10)*ch+ii/10;
					if(ii<=b && ii>=a && mass[ii]==false)
					{
						koll++;
						mass[ii]=true;
					}
				}
				kol+=koll*(koll-1)/2;
			}
		}
	
		cout<<"Case #"<<q+1<<": "<<kol<<"\n";
	}
}
