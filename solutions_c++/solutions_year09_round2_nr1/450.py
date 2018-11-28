#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

string inName;
string outName;

#define cin fin
#define cout fout

char buff[85];

struct node
{
	double w;
	string f;
	node* r, *l;
	node()
	{
		r = l = 0;
	}
};

void readNode(istream& in, node* n)
{
	char c;
	in >> c;
	while(c != '(')
		in >> c;
	in >> n->w;
	in >> n->f;
	if(n->f[0] == ')')
	{
		in.seekg((-1)*(n->f.length()-1), ios::cur);
		n->f = "";
	}
	else
	{
		n->l = new node;
		n->r = new node;
		readNode(in, n->l);
		readNode(in, n->r);
		in >> c;
		while(c != ')')
			in >> c;
	}
}

int main()
{
//	inName = "A-small.in";
	inName = "A-large.in";
//	outName = "A-small.out";
	outName = "A-large.out";

	int tc;
	ifstream fin(inName.c_str());
	ofstream fout(outName.c_str());
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		int l;
		cin >> l;
		node* root = new node;
		readNode(cin, root);
		int a;
		cin >> a;
		string** an = new string*[a];
		int* n = new int[a];
		for(int i = 0; i < a; i++)
		{
			string name;
			cin >> name;
			cin >> n[i];
			n[i]++;
			an[i] = new string[n[i]];
			an[i][0] = name;
			for(int j = 1; j < n[i]; j++)
			{
				cin >> an[i][j];
			}
		}
		double *res = new double[a];
		for(int i = 0; i < a; i++)
		{
			node* cur = root;
			double p = cur->w;
			while(cur->r != 0)
			{
				bool flag = false;
				for(int j = 1; j < n[i]; j++)
					if(cur->f == an[i][j])
					{
						cur = cur->l;
						flag = true;
						break;
					}
				if(flag == false)
				{
					cur = cur->r;
				}
				p *= cur->w;
			}
			res[i] = p;
		}
		cout<<"Case #"<<Case+1<<":"<<endl;
		for(int i = 0; i < a; i++)
			cout << res[i] << endl;
	}
	fout.close();
	fin.close();

	return 0;
}