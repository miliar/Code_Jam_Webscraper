#include <iostream>
#include <cassert>
#include <map>
#include <set>
using namespace std;
void solve_case()
{
	map<string, string> combine;
	set<string> opposed;
	int c, d, n;
	cin >> c;
	for (int i=0; i<c; i++)
	{
		string tmp;
		cin >> tmp;
		assert(tmp.size() == 3);
		assert(!combine.count(tmp.substr(0, 2)));
		combine[tmp.substr(0, 2)] = tmp.substr(2);
		swap(tmp[0], tmp[1]);
		combine[tmp.substr(0, 2)] = tmp.substr(2);
	}
	cin >> d;
	for (int i=0; i<d; i++)
	{
		string tmp;
		cin >> tmp;
		assert(tmp.size() == 2);
		opposed.insert(tmp);
		assert(tmp[1] != tmp[0]);
		swap(tmp[0], tmp[1]);
		opposed.insert(tmp);
	}
	cin >> n;
	string invoke, output;
	cin >> invoke;
	for (int i=0; i<n; i++)
	{
		output.push_back(invoke[i]);
		while (output.size() >= 2 && combine.count(output.substr(output.size() - 2)))
		{
			string tmp = output.substr(output.size() - 2);
			output.resize(output.size() - 2);
			output += combine[tmp];
		}
		for (int i=0; i<(int)output.size(); i++)
		{
			string tmp = output.substr(i, 1) + output[output.size() - 1];
			if (opposed.count(tmp))
			{
				output.clear();
			}
		}
	}
	cout << "[";
	for (int i=0; i<(int)output.size(); i++)
	{
		if (i)
			cout << ", ";
		cout << output[i];
	}
	cout << "]";
}
int main()
{
	int t;
	cin >> t;
	for (int i=0; i<t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		solve_case();
		cout << endl;
	}
	return 0;
}
