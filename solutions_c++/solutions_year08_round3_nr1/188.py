#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int N;
	cin>>N;
	for (int test=1; test<=N; test++)
	{
		vector<int> v;
		v.clear();
		int rez=0;
		int i, x;
		int p,k,l;
		cin>>p>>k>>l;
		for (i=0; i<l; i++)
		{
			cin>>x;
			v.push_back(x);
		}
		sort(v.begin(), v.end());
		reverse(v.begin(), v.end());
		for (i=0; i<l; i++)
			rez+=v[i]*((i/k)+1);
		cout<<"Case #"<<test<<": "<<rez<<endl;
	}
	return 0;
}
