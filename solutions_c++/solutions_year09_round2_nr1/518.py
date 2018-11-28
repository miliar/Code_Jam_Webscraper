// A.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>

using namespace std;

ifstream in ("A.in");
ofstream out ("A.out");

int T, L, A;

struct node
{
	double w;
	string f;
	node *left;
	node *right;
	node(double _w)
	{
		w = _w;
		f = "";
		left = right = NULL;
	}
	node(double _w, const string &_f)
	{
		w = _w;
		f = _f;
		left = right = NULL;
	}

};

string buf = "";

node* read(int &start)
{
	while (isspace(buf[start]))
	{
		++start;
	}
	string r = "";
	while (isdigit(buf[start]) || buf[start] == '.')
	{
		r += buf[start];
		++start;
	}
	while (isspace(buf[start]))
	{
		++start;
	}
	if (buf[start] == ')')
	{
		node *n = new node(atof(r.c_str()));
		++start;
		return n;
	}
	string f = "";
	while (isalpha(buf[start]))
	{
		f += buf[start];
		++start;
	}
	while (buf[start] != '(')
	{
		++start;
	}
	++start;
	node * left = read(start);
	while (buf[start] != '(')
	{
		++start;
	}
	++start;
	node * right = read(start);
	while (buf[start] != ')')
	{
		++start;
	}
	++start;
	node *n = new node(atof(r.c_str()), f);
	n->left = left;
	n->right = right;
	return n;
}

double calc(node *n, double p, const set <string> &f)
{
	/*double res = p;
	res *= n->w;*/
	if (n->f == "")
	{
		return p*n->w;
	}
	string x = n->f;
	if (f.find(x) != f.end())
	{
		return calc(n->left, p*n->w, f);
	}
	else
	{
		return calc(n->right, p*n->w, f);
	}
}

int main()
{
	in >> T;
	node *tree = NULL;
	for (int t = 0; t < T; ++t)
	{
		in >> L;
		buf = "";
		for (int i = 0; i < L; ++i)
		{
			string x = "";
			while (x == "")
				getline(in, x);
			buf += x;
		}
		int x = 0;
		while (buf[x] != '(')
		{
			++x;
		}
		++x;
		tree = read(x);

		in >> A;
		out << "Case #" << t + 1 << ": \n"; 
		out.setf(ios::fixed);
		out.precision(7);
		for (int i = 0; i < A; ++i)
		{
			string s;
			in >> s;
			int n;
			in >> n;
			set <string> f;
			for (int j = 0; j < n; ++j)
			{
				string x;
				in >> x;
				f.insert(x);
			}
			double res = calc(tree, 1.0, f);
			out << res << "\n";
		}

	}
	return 0;
}

