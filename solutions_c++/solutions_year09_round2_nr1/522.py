#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <ctime>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <cassert>
#include <stack>
#include <limits>
#include <cstring>
using namespace std;


typedef long long int64;
typedef unsigned long long uint64;
#define pause system("pause");
#define set0(x) memset(x, 0, sizeof(x))

clock_t __time;
#define retime __time = clock();
#define outtime cout<<clock()-__time<<endl;
const double pi = acos(-1.0);
const double eps = 1e-11;

template<class T> T gcd(const T &a, const T &b) {return (b == 0) ? a : gcd ( b, a%b);}
template<class T> T lcm(const T &a, const T &b) {return a*(b/gcd(a,b));}

int toInt(string s) { istringstream sin(s); int t; sin>>t; return t;}
int64 toInt64(string s) { istringstream sin(s); int64 t; sin>>t; return t;}
string toString(int v ){ ostringstream sout; sout<<v; return sout.str();}
string toString(int64 v){ ostringstream sout; sout<<v; return sout.str();}

typedef struct _node
{
	double p;
	string tag;
	struct _node *y, *n;
	_node()
	{
		p = 1;
		y = n = NULL;
		tag = "";
	}
} node;

node *tree;

void read(node *p)
{
	char c;
	c = getchar();
	while(c == ' ' || c == '\n')
		c = getchar();
	if(c == '(')
	{
		cin>>p->p;
		c = getchar();
	}
	while(c == ' ' || c == '\n')
		c = getchar();
	if(c == ')')
	{
		return;
	}
	else
	{
		p->tag = c;
		c = getchar();
		while(c != '\n')
		{
			p->tag += c;
			c = getchar();
		}
	}
	p->y = new node();
	read(p->y);
	p->n = new node();
	read(p->n);
	c = getchar();
	while(c != ')')
		c = getchar();
}

set <string> ttag;

double run(node *p)
{
	if(p->tag == "")
		return p->p;
	else
	{
		if(ttag.find(p->tag) == ttag.end())
		{
			return run(p->n) * p->p;
		}
		else
		{
			return run(p->y) * p->p;
		}
	}
}

int main()
{
	int cas;
	cin>>cas;
	getchar();
	for(int i = 1; i <= cas; i++)
	{
		int t;
		cin>>t;
		getchar();
		tree = new node();
		read(tree);
		char c;
		c = getchar();
		while(c != '\n')
			c = getchar();
		cin>>t;
		string s;
		cout<<"Case #"<<i<<":"<<endl;
		for(int j = 0; j < t; j++)
		{
			cin>>s;
			int m;
			cin>>m;
			ttag.clear();
			for(int k = 0; k < m; k++)
			{
				cin>>s;
				ttag.insert(s);
			}
			double out;
			out = run(tree);
			printf("%.7f\n",out);
		}
	}
	return 0;
}