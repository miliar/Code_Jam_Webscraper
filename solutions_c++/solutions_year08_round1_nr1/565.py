#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[])
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int d;
		cin >> d;
		vector<int> v1(d);
		for (int j = 0; j < d; j++)
		{
			cin >> v1[j]; 
		}
		vector<int> v2(d);
		for (int j = 0; j < d; j++)
		{
			cin >> v2[j];
		}

		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		long long c = 0;
		for (int j = 0; j < d; j++)
		{
			long long t = v1[j];
			t *= v2[d-j-1];
			c += t;
		}

		cout << "Case #" << (i+1) << ": " << c << endl;
	}
	return 0;
}
