#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

long long a[1000], b[1000];

long long gcd(long long a, long long b)
{
	if(a<b){a=a+b;b=a-b;a=a-b;} 
	long long r=a%b;
	while(r!=0)
	{
		a=b;
		b=r;
		r=a%b;
	}
	return b;
}


int main()
{
	int t, n, k=0;
	long long min=1, g;
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");
	fin>>t;
	for(int i=0; i<t; i++)
	{
		fin>>n;
		for(int j=0; j<n; j++){ fin>>a[j]; if(j==0 || a[j]<min) min=a[j];} 
		k=0;
		for(int j=1; j<n; j++){ if(a[j]!=a[j-1]) b[k++]=(a[j]-a[j-1])>0?a[j]-a[j-1]:a[j-1]-a[j];}
		g=b[0];
		for(int j=1; j<k; j++){g=gcd(g, b[j]);}
		if(min%g!=0) fout<<"Case #"<<i+1<<": "<<(min/g+1)*g-min<<endl;
		else fout<<"Case #"<<i+1<<": "<<0<<endl;
	}
	return 0;
}
