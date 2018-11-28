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

string bin(int n)
{
	string ans = "";
	while (n > 0)
	{
		if (n % 2 == 0)
		{
			ans += '0';
		}
		else
		{
			ans += '1';
		}
		n /= 2;
	}
	return ans;
}

string summ(string a, string b)
{
	int length = min(a.length(), b.length());
	string res = "";
	for (int i = 0; i < length; ++i)
	{
		if (a[i] == b[i])
		{
			res += '0';
		}
		else
		{
			res += '1';
		}
	}
	if ((int) a.length() > length)
	{
		for (int i = length; i < (int) a.length(); ++i)
		{
			res += a[i];
		}
	}
	if ((int) b.length() > length)
	{
		for (int i = length; i < (int) b.length(); ++i)
		{
			res += b[i];
		}
	}
	return res;
}

bool good(string s)
{
	for (int i = 0; i < (int) s.length(); ++i)
	{
		if (s[i] == '1')
		{
			return false;
		}
	}
	return true;
}

int main() 
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		cout << "Case #" << t + 1 << ": ";
		int n;
		cin >> n;
		vector <int> pieces(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> pieces[i];
		}
		string Summ = summ (bin(pieces[0]), bin(pieces[1]));
		for (int i = 2; i < n; ++i)
		{
			Summ = summ(Summ, bin(pieces[i]));
		}
		if (good(Summ))
		{
			int ans = 0;
			sort(pieces.begin(), pieces.end());
			for (int i = 1; i < n; ++i)
			{
				ans += pieces[i];
			}
			cout << ans << endl;
		}
		else
		{
			cout << "NO" << endl;
		}	
	}
	return 0;
}







