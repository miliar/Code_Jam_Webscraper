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

int gcd (int a, int b) {
	return b ? gcd (b, a % b) : a;
}

int main()
{
	freopen("r1a-a.in","r",stdin);
	freopen("r1a-a.out","w",stdout);
	int t,cases=1;
	cin >> t;
	for (int q=0;q<t;++q,cases++)
	{
		long long n;
		int pd,pg;
		cin>>n>>pd>>pg;
		//cout<<gcd(100,pd);
		if ((pd!=100 && pg==100)|| (pd!=0 && pg==0))
			cout<<"Case #"<<cases<<": Broken";
		else if (100/gcd(100,pd)>n)
			cout<<"Case #"<<cases<<": Broken";
		else
			cout<<"Case #"<<cases<<": Possible";
		cout<<endl;
	}
}
