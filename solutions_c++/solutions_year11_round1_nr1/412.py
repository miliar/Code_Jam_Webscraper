#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

long long gcd (long long a, long long b) {
	if (b == 0)
		return a;
	else
		return gcd (b, a % b);
}

void solve()
{
	long long N,Pd,Pg;
	cin>>N>>Pd>>Pg;

	if(Pg==0)
	{
		if(Pd==0)
		{
			cout<<"Possible";
			return;
		}
		else
		{
			cout<<"Broken";
			return;
		}
	}

	if(Pg==100)
	{
		if(Pd==100)
		{
			cout<<"Possible";
			return;
		}
		else
		{
			cout<<"Broken";
			return;
		}
	}

	long long g= 100/gcd(Pd,100);
	
	if(g<=N)
	{
		cout<<"Possible";
		return;
	}
	cout<<"Broken";
	return;
}

int main()
{
	freopen("file.in","r",stdin);
	freopen("file.out","w",stdout);

	int t;
	cin>>t;

	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<(i+1)<<": ";
		solve();
		cout<<endl;
	}

	return 0;
}