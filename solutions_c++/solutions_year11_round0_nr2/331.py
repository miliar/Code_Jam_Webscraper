/*
 * b.cpp
 *
 *  Created on: 2011-5-7
 *      Author: acer
 */

#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <map>

using namespace std;

char combe[256][256];
bool opp[256][256];

bool Combe(string &str)
{
	if (str.size() <= 1) return false;
	char c1 = *str.rbegin();
	char c2 = *(str.rbegin() + 1);
	if (combe[c1][c2] != '\0')
	{
		str.erase(str.size() - 2, 2);
		str.push_back(combe[c1][c2]);
		return true;
	}
	return false;
}

bool Opp(string &str)
{
	if (str.size() <= 1) return false;
	char last = *str.rbegin();
	for (string::iterator it = str.begin(); it < str.end(); ++it)
	{
		if (opp[*it][last])
		{
			str.clear();
			return true;
		}
	}
	return false;
}

int main()
{
	int tn;
	cin >> tn;
	for (int ti = 1; ti <= tn; ++ti)
	{
		int c, d, n;
		memset(combe, '\0', sizeof(opp));
		memset(opp, false, sizeof(opp));

		cin >> c;
		for (int i = 0; i < c; ++i)
		{
			string in;
			cin >> in;
			combe[in[0]][in[1]] = in[2];
			combe[in[1]][in[0]] = in[2];
		}

		cin >> d;
		for (int i = 0; i < d; ++i)
		{
			string in;
			cin >> in;
			opp[in[0]][in[1]] = true;
			opp[in[1]][in[0]] = true;
		}

		string magic;
		cin >> n >> magic;
		string result("");
		for (int i = 0; i < n; ++i)
		{
			result.push_back(magic[i]);
			Combe(result);
			Opp(result);
		}
		cout << "Case #" << ti << ": ";
		cout << "[";
		for (string::iterator it = result.begin(); it != result.end(); ++it)
		{
			if (it == result.begin())
			{
				cout << *it;
			}
			else
			{
				cout << ", " << *it;
			}
		}
		cout << "]" << endl;
	}
	return 0;
}
