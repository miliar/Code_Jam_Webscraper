#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <sstream>
using namespace std;
typedef pair<int, int> ii;

vector<string> prop;
struct node
{
	string ch;
	double prob;
	node* left;
	node* right;
	void build()
	{
		string nexttok;
		cin >> nexttok;
		if (nexttok[0] != '(') cerr << "Err!\n";
		for (int i = nexttok.length()-1; i > 0 ; --i)
			cin.putback(nexttok[i]);
		cin >> prob;
		string endv;
		cin >> endv;
		if (endv[0] == ')')
		{
			for (int i = endv.length()-1; i > 0; --i)
				cin.putback(endv[i]);
			return;
		}
		else 
		{
			ch = endv;
			left = new node;
			left->build();
			right = new node;
			right->build();
		}
		cin >> endv;
		if (endv[0] == ')')
		{
			for (int i = endv.length()-1; i > 0; --i)
				cin.putback(endv[i]);
			return;
		}
		else cerr << "Err!\n";
	}
	double check(double prev)
	{
		if (ch.length() == 0) return prev*prob;
		vector<string>::iterator it = find(prop.begin(), prop.end(), ch);
		if (it != prop.end())
			return left->check(prev*prob);
		return right->check(prev*prob);
	}
};



int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int n;
		cin >> n;
		node* tree = new node;
		tree->build();
		int a;
		cin >> a;
		cout << "Case #" << t+1 << ":\n";
		for (int i = 0; i < a; ++i)
		{
			string name;
			cin >> name;
			int l;
			cin >> l;
			prop.resize(l);
			for (int j = 0; j < l; ++j)
				cin >> prop[j];
			double res = tree->check(1.0);
			cout.precision(7);
			cout << fixed << res << '\n';
		}
	}
}