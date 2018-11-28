// B.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <string>
#include <algorithm>
int T;
std::string res;
std::string str;
std::ifstream in("b.in");
std::ofstream out("b.out");

void solve()
{
	bool good = false;
	for (int i = (int)str.size() - 2; i >= 0; i--)
	{
		int min = '0' + 10;
		int ind = -1;
		for (int j = i + 1; j < (int)str.size(); j++)
		{
			if (str[j] > str[i])
			{
				if (str[j] < min)
				{
					min = str[j];
					ind = j;
				}
			}
		}
		if (ind != -1)
		{
			good = true;
			std::swap(str[i], str[ind]);
			std::sort(str.begin() + i + 1, str.end());
			break;
		}
	}
	if (!good)
	{
		std::sort(str.begin(), str.end());
		res += str[0];
		res += '0';
		res += str.substr(1, str.size() - 1);
		int ind = 0;
		while (res[ind] == '0')
		{
			ind++;
		}
		std::swap(res[ind], res[0]);
	}
	else
	{
		res = str;
	}
}
int main()
{
	in >> T;
	for (int t = 0; t < T; t++)
	{
		std::string str2;
		res.clear();
		in >> str;
		str2 = str;
		solve();
		out << "Case #" << t + 1 << ": " << res << std::endl;
	}
	return 0;
}

