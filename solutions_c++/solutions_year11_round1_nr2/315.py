#include <fstream>
#include <string>
#include <cstring>
#include <iostream>

using namespace std;

const int maxn = 10000;
const int maxm = 100;

fstream fin, fout;
string s[maxn];
string l[maxm];
int sts[maxn][26];

int hasChar(int index, char ch)
{
	int at = ch - 'a';
	if (sts[index][at] != -1)
		return sts[index][at];
	
	sts[index][at] = 0;
	int len = s[index].size();
	for (int i = 0; i < len; ++i)
		if (s[index][i] == ch)
			sts[index][at]++;
	return sts[index][at];
}

bool same(int a, int b, char ch)
{
	for (int i = 0; i < s[a].size(); ++i)
	{
		if (s[a][i] == ch && s[b][i] != ch)
			return false;
		if (s[b][i] == ch && s[a][i] != ch)
			return false;
	}
	return true;
}

void process()
{
	int n, m;
	fin >> n >> m;
	for (int i = 0; i < n; ++i)
	{
		fin >> s[i];
		for (int j = 0; j < 26; ++j)
			sts[i][j] = -1;
	}
	for (int i = 0; i < m; ++i)
		fin >> l[i];

	for (int list = 0; list < m; ++list)
	{
		int answer = -1;
		string sanswer = "";
		for (int i = 0; i < n; ++i)
		{
			bool flag[maxn];
			int wrong = 0;
			memset(flag, 0, sizeof flag);
			for (int k = 0; k < n; ++k)
				if (s[k].size() != s[i].size())
				{
					flag[k] = true;
					++wrong;
				}

			int count = 0;
			int len = s[i].size();
			int cost = 0;
			
			
			for (int j = 0; j < 26; ++j)
			{
				if (wrong == n - 1)
					break;
				bool use = false;
				for (int k = 0; k < n; ++k)
					if (!flag[k] && hasChar(k, l[list][j]))
					{
						use = true;
						break;
					}
				if (use)
				{
					if (hasChar(i, l[list][j]))
					{
						count += hasChar(i, l[list][j]);
						if (count == len) break;

						for (int k = 0; k < n; ++k)
							if (!flag[k] && k != i && !same(i, k, l[list][j]))
							{
								flag[k] = true;
								++wrong;
								if (wrong == n - 1)
									break;
							}
					}
					else
					{
						cost++;
						for (int k = 0; k < n; ++k)
							if (!flag[k] && hasChar(k, l[list][j]))
							{
								flag[k] = true;
								++wrong;
								if (wrong == n - 1)
									break;
							}
					}
				}
			}

			if (cost > answer)
			{
				answer = cost;
				sanswer = s[i];
			}
		}
		fout << " " << sanswer;
		//cout << answer;
	}
}

int main()
{
	fin.open("in.txt", fstream::in);
	fout.open("out.txt", fstream::out);

	int testcase;
	fin >> testcase;
	for (int i = 1; i <= testcase; ++i)
	{
		fout << "Case #" << i << ":";
		process();
		fout << endl;
	}

	fin.close();
	fout.close();
}