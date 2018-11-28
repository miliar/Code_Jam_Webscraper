#include<iostream>
#include<string>
#include<map>

using namespace std;

typedef unsigned long long nat;

int main()
{
	int T;
	cin >> T;

	string msg;
	map<char, int> weight;

	for(int X = 1; X <= T; ++X)
	{
		cin >> msg;

		const int len = msg.length();

		weight.clear();

		weight[msg[0]] = 1;

		int base = 0;

		for(int i = 1; i < len; ++i)
			if(weight.find(msg[i]) == weight.end())
				if(base == 0)
				{
					weight[msg[i]] = 0;
					base = 2;
				}
				else
					weight[msg[i]] = base++;

		if(base == 0)
			base = 2;

		nat value = 0;

		for(int i = 0; i < len; ++i)
			value = value * base + weight[msg[i]];

		cout << "Case #" << X << ": " << value << '\n';
	}

	return 0;
}