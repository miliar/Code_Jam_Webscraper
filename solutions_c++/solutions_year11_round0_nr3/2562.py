#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{
	size_t tests;
	cin>>tests;
	for (size_t testn = 0; testn<tests; ++testn)
	{
		size_t n;
		cin>>n;
		unsigned long long x = 0, sum = 0, mn;
		for (size_t i = 0; i<n; ++i)
		{
			unsigned long long a;
			cin>>a;
			if (!i || mn>a)
				mn = a;
			x^=a;
			sum+=a;
		}
		cout<<"Case #"<<testn+1<<": ";
		if (x)
		{
			cout<<"NO";
		}
		else
		{
			cout<<sum-mn;
		}
		cout<<endl;
	}
}

