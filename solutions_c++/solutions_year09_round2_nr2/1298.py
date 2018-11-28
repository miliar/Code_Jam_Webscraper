#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <ctime>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <queue>
#include <utility>
#include <cstdio>
#include <cstdlib>
using namespace std;

int t,c,n;
double dp[41][41];
double com[41][41];

bool areEqual(int n, vector <int> &nums)
{
	vector<int> temp(10, 0);
	while (n > 0) {
		temp[n%10]++;
		n/=10;
	}
	for (int i=1;i<10;i++) {
		if (temp[i] != nums[i]) return false;
	}

	return true;
}

void main()
{
	string str;

	freopen("C:\\Projects\\codejam\\Release\\input.txt", "rt", stdin);
	freopen("C:\\Projects\\codejam\\Release\\output.txt", "wt", stdout);
	
	cin >> t;
	for (int z=0;z<t;z++)
	{
		int n;
		cin >> n;
		vector<int> nums(10, 0);
		int temp = n;
		while (temp > 0) {
			nums[temp%10]++;
			temp /= 10;
		}
		int i;
		for (i=n+1;;i++)
		{
			if (areEqual(i, nums)) break;
		}

		cout << "Case #" << (z+1) << ": " << i << endl;
	}
}