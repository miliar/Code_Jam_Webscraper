#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

void main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	long long T;
	cin >> T;
	for (long long t = 0; t < T; t++)
	{
		string str;
		cin >> str;
		vector<char> dict;
		for (long long i = 0; i < str.size(); i++)
		{
			bool exist = false;
			for (long long j = 0;j < dict.size(); j++)
			{
				if (dict[j] == str[i])
				{
					exist = true;
					break;
				}
			}
			if (!exist)
			{
				dict.push_back(str[i]);
			}
		}

		long long base;
		if (dict.size() == 1)
			base = 2;
		else
			base = dict.size();

		map<char, long long> quantity;
		for (long long i = dict.size() - 1; i >= 0; i--)
		{
			if (i >= 2)
				quantity[dict[i]] = i;
			else if (i == 1)
				quantity[dict[i]] = 0;
			else if (i == 0)
				quantity[dict[i]] = 1;
		}

		long long sum = 0;
		long long tmp = 1;
		for (long long i = str.size() - 1; i >= 0 ; i--)
		{
			long long product = quantity[str[i]] * tmp;
			sum += product;

			tmp *= base;
		}

		cerr << "Case #" << t + 1 <<": " << sum<< endl;
		cout << "Case #" << t + 1 <<": " << sum<< endl;
	}

}