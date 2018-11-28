#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int T;


int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	cin >> T;
	for (int I = 0 ; I < T; I++)
	{
		string str;
		string res = "";
		cin >> str;
		vector<int> a;
		bool incr = true;
		int i;
		for (i = str.size() - 1; i >= 0; i--)
		{
			int b = str[i];
			if (a.size() > 0)
			{
				if (a[a.size() - 1] <= b)
					a.push_back(b);
				else
				{
					incr = false;
					break;
					
				}
			}
			else
				a.push_back(b);
		}
		if (incr)
		{
			bool m = false;
			int cnt = 0;
			int sz = str.size();
			for (cnt = 0; cnt < str.size(); cnt++)
				if (str[sz - 1 - cnt] != '0') break;
			res += str[sz - 1 - cnt];
			for (int ii = 0 ; ii < cnt + 1; ii++)
				res += '0';
			for (int ii = cnt + 1; ii < sz; ii++)
				res += str[sz - 1 - ii];

		}
		else
		{
			int j = 0;
			while (a[j]<= str[i])
				j++;
			for (int ii = 0; ii < i; ii++)
				res += str[ii];
			res += a[j];
			a[j] = str[i];
			for (int ii = 0; ii < a.size(); ii++)
				res += a[ii];
		}
		cout << "Case #" << I+1 << ": " << res <<endl;
	}

	return 0;
}