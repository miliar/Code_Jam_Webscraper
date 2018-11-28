#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int q,s;
int cur,ans;
string have[2000];

ifstream fin("A-large.in");
ofstream fout("A-large.out");

void insert(string str)
{
	for (int i = 0; i < cur; ++i)
	    if (str == have[i]) return;
	have[cur++] = str;
}

void solve()
{
	fin >> s;
	fin.get();
	string junk;
	for (int i = 0; i < s; ++i)
	    getline(fin, junk);
	fin >> q;
	fin.get();
	cur = 0;
	ans = 0;
	for (int i = 0; i < q; ++i)
	{
		string word;
		getline(fin, word);
		insert(word);
		if (cur == s)
		{
			ans++;
			cur = 0;
			insert(word);
		}
	}
	fout << ans << endl;
}

int main()
{
	int tc;
	fin >> tc;
	for (int i = 1; i <= tc; ++i)
	{
		fout << "Case #" << i << ": ";
		solve();
	}
	fin.close();
	fout.close();
	return 0;
}
