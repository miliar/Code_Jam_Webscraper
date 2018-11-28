#include <iostream>
#include <string>
#include <map>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ifstream cin("b.in");
	ofstream cout("b.out");
	int t;
	cin  >> t;
	for(int tc=1;tc<=t;tc++)
	{
		int n,s,p,sum=0;
		cin >> n >> s >> p;
		vector<int> arr(n);
		for(int i=0;i<n;i++)
			cin >> arr[i];
		if(p == 0)
		{
			cout << "Case #" << tc << ": " << n << "\n";
			continue;
		}
		sort(arr.rbegin(),arr.rend());
		for(int i=0;i<n;i++)
		{
			if(arr[i] >= 3*p-2)
			{
				sum++;
				//cout << arr[i] << ",";
			}
			if(arr[i] < 3*p-2 && s && arr[i]>=3*p-4&&p>1)
			{
				sum++,s--;
				//cout << arr[i] << "^";
			}
		}
		cout << "Case #" << tc << ": " << sum << "\n";
	}
}
