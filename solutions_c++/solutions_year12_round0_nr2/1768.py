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
	ifstream cin("B-large.in");
	ofstream cout("output.txt");
	long T;
	cin>>T;
	
	for(long q=0;q<T;q++)
	{
		long kol=0;
		long n,s,p;
		cin>>n>>s>>p;

		long t,tmp;

		for(long i=0;i<n;i++)
		{
			cin>>t;
			tmp=t/3+(t%3==0 ? 0 : 1);
			if(tmp>=p)
				kol++;
			else
				if(t!=0 && tmp==p-1 && t%3!=1 && s!=0)
				{
					kol++;
					s--;
				}
		}
	
		cout<<"Case #"<<q+1<<": "<<kol<<"\n";
	}
}
