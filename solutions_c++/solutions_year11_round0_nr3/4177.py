#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


void Go(int num)
{
	int n;
	cin >> n;
	vector<long long>v(n);
	for(int i = 0; i < n; i++)
	{
		cin >> v[i];
	}
	sort(v.begin(), v.end());
	int sumX = 0;
	long long realSum = 0;
	for(int i = n-1; i > 0; i--)
	{
		sumX ^= v[i];
		realSum += v[i];
	}
	int k = sumX ^ v[0]; 
	if(k == 0)
	{
		cout << "Case #" << num << ": " << realSum << endl;  
	}
	else
		cout << "Case #" << num << ": NO" << endl;
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int numtests;
	cin >> numtests;
	for(int i = 0; i < numtests; i++)
	{
		Go(i+1);
	}
	return 0;
}