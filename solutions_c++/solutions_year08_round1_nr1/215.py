#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;
ifstream fin("A-small-attempt0.in");
ofstream fout("p1.ans");

int n;
long int a[900], b[900];
void init()
{
	fin>>n;
	for (int i=0;i<n;i++) fin>>a[i];
	for (int i=0;i<n;i++) fin>>b[i];
}
void calc()
{
	sort(a,a+n);
	sort(b,b+n);
	long int sum=0;
	for (int i=0;i<n;i++) sum+=a[i]*b[n-1-i];
	fout<<sum<<endl;
}
int main()
{
	int t;
	fin>>t;
	for (int i=1;i<=t;i++)
	{
		init();
		fout<<"Case #"<<i<<": ";
		calc();
	}
}