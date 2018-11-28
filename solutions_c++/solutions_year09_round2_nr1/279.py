#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

struct Node
{
	double p;
	string name;
	Node* l;
	Node* r;
};

char line[128];

int FindPair(const string& s, int p)
{
	int q = 0;
	while (true)
	{
		if (s[p] == '(')
			q++;
		if (s[p] == ')')
		{
			q--;
			if (q == 0)
				return p;
		}
		p++;
	}
	return 0;
}

void BuildTree(const string& s, Node* root)
{
	int lb = s.find_first_of('(');
	int lw = lb+1;
	while (s[lw] == ' ') lw++;
	int rw = lw;
	while (s[rw] != ' ' && s[rw] != ')') rw++;
	sscanf(s.substr(lw, rw-lw).c_str(), "%lf", &root->p);
	int lf = rw;
	while (s[lf] == ' ') lf++;
	if (s[lf] == ')')
		return;
	int rf = lf;
	while (s[rf] != ' ' && s[rf] != '(') rf++;
	root->name = s.substr(lf, rf-lf);

	int ls = rf;
	while (s[ls] == ' ') ls++;
	int rs = FindPair(s, ls);
	root->l = new Node();
	BuildTree(s.substr(ls, rs-ls+1), root->l);

	int lt = rs+1;
	while (s[lt] == ' ') lt++;
	int rt = FindPair(s, lt);
	root->r = new Node();
	BuildTree(s.substr(lt, rt-lt+1), root->r);
}

double Count(Node* u, const vector<string>& fs)
{
	double p = u->p;
	if (u->name != "")
	{
		vector<string>::const_iterator q = find(fs.begin(), fs.end(), u->name);
		if (q != fs.end())
			p *= Count(u->l, fs);
		else
			p *= Count(u->r, fs);
	}
	return p;
}

void Solve()
{
	int k;
	scanf("%d", &k);
	gets(line);
	string s = "";
	for (int i=0; i<k; i++)
	{
		gets(line);
		s += line;
		s += " ";
	}
	Node* root = new Node();
	BuildTree(s, root);
	scanf("%d", &k);
	for (int i=0; i<k; i++)
	{
		int l;
		scanf("%*s %d", &l);
		vector<string> fs;
		for (int j=0; j<l; j++)
		{
			scanf("%s", &line);
			fs.push_back(line);
		}
		double p = Count(root, fs);
		printf("%.7lf\n", p);
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i=1; i<=t; i++)
	{
		printf("Case #%d:\n", i);
		Solve();
	}
	return 0;
}
