#include<iostream>
#include<vector>
#include<set>
#include<string>
#include<sstream>

using namespace std;

typedef unsigned int nat;

nat ssd(nat n, nat const b)
{
	nat s = 0;

	for(nat i = n; i != 0;)
	{
		nat d = i % b;
		i /= b;
		s += d*d;
	}

	return s;
}

bool isHappy(nat n, nat b)
{
	static set<nat> ss;

	ss.clear();

	for(nat i=n; i != 1; i = ssd(i, b))
		if(ss.find(i) == ss.end())
			ss.insert(i);
		else
			return false;

	return true;
}

int main()
{
	string line;
	stringstream ss;

	nat T;

	getline(cin, line);
	ss << line;
	ss >> T;

	for(nat X=1; X <= T; ++X)
	{
		vector<nat> bases;

		getline(cin, line);
		ss.flush();
		ss.clear();
		ss << line;
		for(nat b; ss >> b; bases.push_back(b));

		for(nat i=2; ; ++i)
		{
			nat b;
			nat const s = bases.size();

			for(b = 0; b < s; ++b)
				if(!isHappy(i, bases[b]))
					break;

			if(b == s)
			{
				cout << "Case #" << X << ": " << i << "\n";
				break;
			}
		}
	}

	return 0;
}