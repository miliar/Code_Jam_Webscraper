#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int t, test, p, k, c, l, i;
	int f[1000000];
	long long ret;
	cin>>t;
	for(test=1; test<=t; test++)
	{
		cin>>p>>k>>l;
		for(i=0; i<l; i++)
			cin>>f[i];
		if((int)ceil(l/k)>p)
		{
			cout<<"impossible"<<endl;
			continue;
		}
		sort(f, f+l);
		ret=0;
		i=l-1;
		c=1;
		while(i>=0)
		{
			for(int j=0; j<k && i>=0; j++, i--)
				ret+=f[i]*c;
			c++;	
		}
		cout<<"Case #"<<test<<": "<<ret<<endl;
	}
	return 0;
}
