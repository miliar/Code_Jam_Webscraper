#include <string>
#include <sstream>
#include <vector>
#include <fstream>
#include <iomanip>
#include <set>
using namespace std;

int cnt, pos;
set<string> features;
double P;

struct item
{
	item(const string& name, double p) : name(name), p(p), l(-1), r(-1) {}
	int l, r;
	string name;
	double p;
};

vector<item> Tree;

int addItem(const string& str)
{
	++pos;
	int old = pos;
	while (str[pos] >= '0' && str[pos] <= '9' || str[pos] == '.') ++pos;
	string num = str.substr(old, pos-old);
	double p;
	sscanf(num.c_str(), "%lf", &p);

	if (str[pos] == ')')
	{
		item it("", p);
		if (Tree.size() == cnt)
			Tree.push_back(it);
		else 
			Tree[cnt] = it;
		++cnt;
		++pos;
		return cnt-1;
	}
	else
	{
		int old = pos;
		while (str[pos] >= 'a' && str[pos] <= 'z') ++pos;
		string s = str.substr(old, pos-old);
		item it(s, p);
		if (Tree.size() == cnt)
			Tree.push_back(it);
		else 
			Tree[cnt] = it;
		int c = cnt++;
		Tree[c].l = addItem(str);
		Tree[c].r = addItem(str);
		++pos;
		return c;
	}
}

void createTree(const string& t)
{
	stringstream str(t);
	string newt;
	string s;
	while (str >> s) newt += s;
	addItem(newt);	
}

void Go(int pos)
{
	P *= Tree[pos].p;
	if (Tree[pos].l == -1) return;
	else 
	{
		if (features.count(Tree[pos].name) > 0)
		{
			Go(Tree[pos].l);
		}
		else 
		{
			Go(Tree[pos].r);
		}
	}
}

int main()
{
	ifstream ifs("a.in");
	ofstream ofs("a.out");
	int t;
	string s;
	getline(ifs, s);
	sscanf(s.c_str(), "%d", &t);
	for (int test = 0; test < t; ++test)
	{
		int n;
		getline(ifs, s);
		sscanf(s.c_str(), "%d", &n);
		string t;
		for (int i = 0; i < n; ++i)
		{
			getline(ifs, s);
			t += s;
		}
		getline(ifs, s);
		sscanf(s.c_str(), "%d", &n);
		cnt = 0;
		pos = 0;
		createTree(t);
		ofs << "Case #" << test+1 << ":\n";
		for (int i = 0; i < n; ++i)
		{
			getline(ifs, s);
			stringstream str(s);
			string name;
			int k;
			str >> name >> k;
			features.clear();
			for (int i = 0; i < k; ++i)
			{
				string t;
				str >> t;
				features.insert(t);
			}
			P = 1;
			Go(0);
			ofs << fixed << setprecision(10) << P << endl;
		}
	}

	return 0;
}