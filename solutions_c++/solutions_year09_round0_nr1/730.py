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

#define null 0
typedef struct _node
{
	struct _node *lis[26];
} node;

node tree;
int mc;
string out;
int l;

void buildtree(string s)
{
	node *p;
	p = &tree;
	for(int i = 0; i < s.size(); i++)
	{
		if(p->lis[(s[i]-'a')] == null)
		{
			p->lis[(s[i]-'a')] = new node;
			p = p->lis[(s[i]-'a')];
			set0(p->lis);
		}
		else
		{
			p = p->lis[(s[i]-'a')];
		}
	}
}

void run(int n, node *p)
{
	int nn;
	int tn;
	nn = n;
	if(out[nn] == '(')
	{
		nn++;
		tn = nn;
		while(out[tn] != ')')
			tn++;
		while(out[nn] != ')')
		{
			if(p->lis[(out[nn]-'a')] == null)
			{}
			else
			{
				if(tn == out.size()-1)
				{
					mc++;
				}
				else
					run(tn+1, p->lis[(out[nn]-'a')]);
			}
			nn++;
		}
	}
	else
	{
		if(p->lis[(out[nn]-'a')] == null)
			return;
		else
		{
			if(n == out.size()-1)
			{
				mc++;
				return;
			}
			else
				run(n+1, p->lis[(out[nn]-'a')]);
		}
	}
}

int main()
{
	int d, n;
	string s;
	cin>>l>>d>>n;
	set0(tree.lis);
	for(int i = 0; i < d; i++)
	{
		cin>>s;
		buildtree(s);
	}
	for(int i = 0; i < n; i++)
	{
		mc = 0;
		cin>>out;
		run(0, &tree);
		cout<<"Case #"<<i+1<<": "<<mc<<endl;
	}
	return 0;
}