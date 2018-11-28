#include <iostream>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

vector<map<string,int> > dir;

vector<string> tokenize(const string &p)
{
	stringstream buf(p);
	string tok;
	vector<string> res;
	getline(buf, tok, '/');
	while (getline(buf, tok, '/'))
		res.push_back(tok);
	return res;
}

int insert(const vector<string> &v)
{
	int res = 0;
	int pos = 0;
	for (int i = 0; i < v.size(); i++)
	{
		if (dir[pos].find(v[i]) == dir[pos].end())
		{
			int idx = dir.size();
			dir.push_back(map<string,int>());
			dir[pos][v[i]] = idx;
			res++;
//			cout << "add " << v[i] << " in " << pos << endl;
		}
		pos = dir[pos][v[i]];
	}
	return res;
}

int main()
{
	int kases, kase = 0;
	for (cin >> kases; kases; kases--)
	{
		int N, M, res = 0;
		dir.clear();
		dir.push_back(map<string,int>());
		cin >> N >> M;
		while (N--)
		{
			string path;
			cin >> path;
			insert(tokenize(path));
		}
		while (M--)
		{
			string path;
			cin >> path;
			res += insert(tokenize(path));
		}
		cout << "Case #" << ++kase << ": " << res << endl;
	}
	return 0;
}
