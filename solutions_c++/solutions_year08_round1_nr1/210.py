#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define MAX 800
int a[MAX];
int b[MAX];
int n;

int main()
{
	int cc;
	cin>>cc;
	for(int ci=1;ci<=cc;ci++)
	{
		cin>>n;
		int i;
		for(i=0;i<n;i++) cin>>a[i];
		for(i=0;i<n;i++) cin>>b[i];

		sort(a,a+n);
		sort(b,b+n,greater<int>());

		long long prod=0;
		for(i=0;i<n;i++) prod+=a[i]*b[i];

		cout<<"Case #"<<ci<<": "<<prod<<endl;
	}

	return 0;
}
