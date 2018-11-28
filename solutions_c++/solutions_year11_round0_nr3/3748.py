#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>> t;
	for (int i = 0 ; i < t ; i++)
	{
		int n;
		cin >> n;
		vector < int > v;
		int xor = 0;		
		int sum = 0;
		for (int j = 0 ; j < n ; j++)
		{
			int k ; 
			cin>> k;
			v.push_back(k);
			xor ^= k;
			sum += k;
		}
		sort(v.begin(),v.end());
		cout << "Case #" << i + 1 << ": ";
		if (xor != 0)
			cout << "NO\n";
		else
			cout << sum - v[0] << '\n';		
	}
}