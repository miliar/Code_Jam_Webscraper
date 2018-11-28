#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <set>

using namespace std;

string tree;
set<string> feat;
char f[1024*1024];

int readk()
{
	string line;
	getline(cin, line);
	stringstream buf(line);
	int res;
	buf >> res;
	return res;
}

double tr(int &pos)
{
	double res;
	while (isspace(tree[pos]))
		pos++;
	assert(tree[pos] == '(');
	pos++;
	while (isspace(tree[pos]))
		pos++;
	sscanf(tree.c_str() + pos, "%lf", &res);
	while (!isspace(tree[pos]) && tree[pos] != ')')
		pos++;
	while (isspace(tree[pos]))
		pos++;
	if (tree[pos] == ')')
	{
		pos++;
		return res;
	}
	sscanf(tree.c_str() + pos, "%s", &f);
	bool left = (feat.find(f) != feat.end());
	while (!isspace(tree[pos]))
		pos++;
	double val1 = tr(pos);
	double val2 = tr(pos);
	while (isspace(tree[pos]))
		pos++;
	assert(tree[pos] == ')');
	pos++;
	if (left)
		res *= val1;
	else
		res *= val2;
	return res;
}

int main()
{
	int kases = readk();
	for (int kase = 1; kase <= kases; kase++)
	{
		tree = "";
		for (int lines = readk(); lines; lines--)
		{
			string line;
			getline(cin, line);
			tree += line;
			tree += " ";
		}

		printf("Case #%d:\n", kase);
		for (int animals = readk(); animals; animals--)
		{
			string line;
			getline(cin, line);
			stringstream buf(line);
			buf >> line;
			int n;
			buf >> n;
			feat.clear();
			while (n--)
			{
				buf >> line;
				feat.insert(line);
			}
			int pos = 0;
			printf("%.7lf\n", tr(pos));
		}
	}
	return 0;
}
