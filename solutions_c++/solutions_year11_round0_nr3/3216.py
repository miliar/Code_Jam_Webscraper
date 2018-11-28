#include <iostream>
#include <cmath>
#include <vector>
#include <iterator>
#include <numeric>
#include <cstdio>
#include <string>
#include <algorithm>

template <class T>
T abs (T a)
{
    if (a<0)
        return -a;
    return a;
}

using namespace std;

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int tests;
	cin>>tests;
	for (int q=0;q<tests;++q)
	{
		int n;
		cin>>n;
		long long res=0;
		vector<long long> v(n);
		for (int i=0;i<n;++i)
			cin>>v[i];
		for (int i=0;i<n;++i)
		{
			res^=v[i];
		}
		if (res)
			cout<<"Case #"<<q+1<<": NO"<<endl;
		else
		{
			sort(v.begin(), v.end());
			res=accumulate(v.begin()+1,v.end(),0);
			cout<<"Case #"<<q+1<<": "<<res<<endl;
		}
	}
}
