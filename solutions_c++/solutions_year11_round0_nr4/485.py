#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <deque>
#include <map>
#include <cmath>
#include <set>
#include <stack>
#include <sstream>

using namespace std;

string toString(int val)
{
    ostringstream oss;
    oss << val;
    return oss.str();
}

int fromString(const std::string& s) 
{
  istringstream iss(s);
  int res;
  iss >> res;
  return res;
}

int main() 
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		cout << "Case #" << t + 1 << ": ";
		int n;
		cin >> n;
		vector <int> nums(n);
		int ans = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> nums[i];
			--nums[i];
			if (nums[i] != i)
			{
				++ans;
			}
		}
		cout << ans << endl;	
	}
	return 0;
}







