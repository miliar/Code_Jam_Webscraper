#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
long long a[1000],b[1000];
int main()
{
	int n,nn,ii,i,j;
	ifstream cin("a-large.in");
	ofstream cout("a-large.out");
	cin >>nn;
	long long s;
	for (ii=1;ii<=nn;ii++)
	{
		cin >>n;
		for (i=1;i<=n;i++)
			cin >>a[i];
		for (i=1;i<=n;i++)
			cin >>b[i];
		sort(a+1,a+n+1);
		sort(b+1,b+n+1);
		s=0;
		for (i=1;i<=n;i++)
			s=s+a[i]*b[n+1-i];
		cout <<"Case #" <<ii <<": ";
		cout <<s <<endl;
	}
	return 0;
}

