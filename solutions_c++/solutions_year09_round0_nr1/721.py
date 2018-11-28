#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

int L, D, N;
string ptn[5000];
bool table[15][26];

void ReadPattern()
{
	cin >> L >> D >> N;
	for (int i = 0; i < D; i ++)
	{
		cin >> ptn[i];
	}
	return;
}
bool Contain(string sz, char ch)
{
	for (int i = 0; i < sz.size(); i ++)
	{
		if (sz[i] == ch) return true;
	}
	return false;
}
bool Judge(vector <string> vecSz, string smpl)
{
	for (int i = 0; i < L; i ++)
	{
		//if (!Contain(vecSz[i], smpl[i])) return false;
		if (!table[i][smpl[i] - 'a']) return false;
	}
	return true;
}
vector <string> Parse(string sz)
{
	int pos = 0;
	vector <string> vecSz;
	for (int i = 0; i < 15; i ++)
		for (int j = 0; j < 26; j ++)
		{
			table[i][j] = false;
		}
	for (int i = 0; i < L; i ++)
	{
		string tmp;
		tmp = "";
		if (sz[pos] == '(')
		{
			pos ++;
			while (sz[pos] != ')')
			{
				tmp += sz[pos];
				table[i][sz[pos] - 'a'] = true;
				pos ++;
			}
		}
		else
		{
			tmp = sz[pos];
			table[i][sz[pos] - 'a'] = true;
		}
		vecSz.push_back(tmp);
		pos ++;
	}
	return vecSz;
}
int main()
{
	ReadPattern();
	for (int i = 0; i < N; i ++)
	{
		string sz;
		vector <string> vecSz;
		int cnt = 0;
		cin >> sz;
		vecSz = Parse(sz);
		for (int j = 0; j < D; j ++)
		{
			if (Judge(vecSz, ptn[j])) cnt ++;
		}
		cout << "Case #" << i + 1 << ": " << cnt << endl;
		vecSz.clear();
	}
	return 0;
}