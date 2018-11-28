#include <string>
#include <iostream> 
#include <fstream>
#include <math.h>
#include <vector>
#include <time.h>
#include <algorithm>
#include <map>
#include <set>

using namespace std;
const double eps = 1e-8;
#define M_PI       3.14159265358979323846

#ifdef _MSC_VER
#else
typedef long long __int64;
#endif

int sum;

struct node
{
	string s;
	vector<node*> c;
	node *child(string sn)
	{
		for (int i=0;i<(int)c.size();i++)
			if (c[i]->s == sn)
				return c[i];
		c.push_back(new node());
		c.back()->s = sn;
		++sum;
		return c.back();
	}
};

void parse(string s, node *root)
{
	string tok;
	s.erase(s.begin());
	for (int i=0;i<(int)s.length();i++)
	{
		if (s[i] != '/')
		{
			tok += s[i];
		}
		else
		{
			root = root->child(tok);
			tok = "";
		}
	}
	root = root->child(tok);
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");


	int tn;
	cin>>tn;
	for (int aaa=1;aaa<=tn;aaa++)
	{
		int n,m;
		cin>>n>>m;
		sum = 0;
		node *root = new node();
		for (int i=0;i<n;i++)
		{
			string s;
			cin>>s;
			parse(s, root);
		}
		int ss = sum;
		for (int i=0;i<m;i++)
		{
			string s;
			cin>>s;
			parse(s, root);
		}
		cout<<"Case #"<<aaa<<": "<<sum - ss;
		cout<<endl;
	}




	return 0;
}