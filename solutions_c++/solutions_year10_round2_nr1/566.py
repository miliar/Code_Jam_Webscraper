#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

void solve(string &temp, vector<string> &exist, int &result);

int main()
{
	ifstream fin("A.in", ios_base::in);
	ofstream fout("A.out", ios_base::out);

	int t;
	fin >> t;
	for (int count = 0; count != t; ++count)
	{
		int n, m, result = 0;
		fin >> n >> m;
		vector<string> exist;

		for (int i = 0; i != n; ++i)
		{
			string temp;
			fin >> temp;
			exist.push_back(temp);
		}
		for (int i = 0; i != m; ++i)
		{
			string temp;
			fin >> temp;
			solve(temp, exist, result);
		}

		fout << "Case #" << (count + 1) << ": " << result << endl;
	}
	fin.close();
	fout.close();
	return 0;
}

void solve(string &temp, vector<string> &exist, int &result)
{
	if (temp[0] == '\0') return;
	for (size_t i = 0; i != exist.size(); ++i)
	{
		if (!exist[i].compare(temp)) return;
	}
	exist.push_back(temp);
	++result;
	temp = temp.substr(0, temp.rfind('/'));
	solve(temp, exist, result);
}
