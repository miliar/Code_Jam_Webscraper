#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int a[1000];

int main()
{
	int t, r, n, k;
	int p=0,sum=0, count=0;
	int money=0;
	bool find=true;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	fin>>t;
	for(int i=0; i<t; i++) // case i
	{
		fin>>r>>k>>n;
		count=money=sum=p=0;
		for(int j=0; j<n; j++) fin>>a[j];

		for(int j=0; j< r; j++)
		{
			while(count<n && sum+a[p%n]<=k){sum+=a[(p++) %n]; count++;}
			money+=sum;
			count=sum=0;
		}
		fout<<"Case #"<<i+1<<": "<<money<<endl;
	}
	return 0;
}
