#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
using namespace std;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int Test;
	cin >> Test;
	
	for(int t=1;t<=Test;t++)
	{
		int N;
		cin >> N;
		vector<int> v;
		
		int sum = 0;
		int total = 0;
		
		for(int i=0;i<N;i++)
		{
			int tmp;
			cin >> tmp;
			v.push_back(tmp);
			sum ^= tmp;
			total += tmp;
		}
		
		sort(v.begin(), v.end());
		
		if(sum == 0)
		{
			printf("Case #%d: %d\n", t, total - v[0]);
		}
		else
		{
			printf("Case #%d: NO\n", t);
		}
	}
	
	return 0;
}

