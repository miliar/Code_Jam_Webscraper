#include <iostream>
#include <vector>
#include <fstream>

using namespace std;


int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t;
	cin >> t;
	for (int d=1;d<=t;++d)
	{
		int n;
		cin >> n;
		int s=0;
		int sum=0;
		int m=1000000000;
		vector<int> v(n);
		for (int i=0;i<n;++i)
		{
			cin >> v[i];
			s^=v[i];
			sum+=v[i];
			m=min(m,v[i]);
		}
		if (s)
			cout << "Case #" << d << ": NO\n";
		else
			cout << "Case #" << d << ": " << sum-m << '\n';
	}
	return 0;
}