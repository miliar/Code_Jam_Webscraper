
#include <iostream>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <vector>
#include <ctime>
#include <cctype>
using namespace std;


void solve(int testcase)
{
	int k;

	cin >> k;
	string s;
	cin >> s;
	
	int arr[] = {0, 1, 2, 3, 4};
	int compressed = s.size();
	do
	{
		string v = s;

		for (int i = 0; k*i < s.size(); i++)
		{
			for (int j = 0; j < k; j++)
				v[k*i+j] = s[k*i+arr[j]];
		}

		int groups = 0;
		int c = ' ';
		for (int i = 0; i < v.size(); i++)
			if (v[i] != c)
			{
				c = v[i];
				groups++;
			}
		
		compressed = min(compressed, groups);
	} while (next_permutation(arr, arr+k));

	printf("Case #%d: %d\n", testcase, compressed);

}

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
		solve(i+1);
	return 0;
}
