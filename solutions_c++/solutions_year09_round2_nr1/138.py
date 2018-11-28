#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <complex>
using namespace std;
struct Tree
{
	double p;
	string desc;
	Tree* lc, * rc;
};


string get_token()
{
	char c;
	while ((c = getchar()) == ' ' || c == '\n');
	if (c == '(') return "(";
	if (c == ')') return ")";
	if (c == '1')
	{
		c = getchar();
		if (c == '.')
		{
			ungetc(c, stdin);
			c = '1';
		}
		else
		{
			return "1";
		}
	}
	string ans;ans = c;
	if (isalpha(c)) while (isalpha(c = getchar())) ans += c;
	else
	{
		while (isdigit(c = getchar()) || c == '.') ans += c;
	}
	ungetc(c, stdin);
	return ans;
}
Tree* build()
{
	string tk = get_token();//read (
	tk = get_token();
	Tree* nd = new Tree;
	nd->p = atof(tk.c_str());
	nd->lc = nd->rc = 0;
	char c;
	while ((c = getchar()) == ' ' || c == '\n');
	if (c != ')')
	{
		ungetc(c, stdin);
		nd->desc = get_token();
		nd->lc = build();
		nd->rc = build();
		get_token();
	}

	return nd;
}

void show(Tree* nd)
{
	if (!nd) return;
	cout << nd->p << endl;
	show(nd->lc);
	show(nd->rc);
	return ;
}

void destroy(Tree* nd)
{
	if (nd->lc) destroy(nd->lc);
	if (nd->rc) destroy(nd->rc);
	delete nd;
}


map<string, int> mp;
double result;
void cal(Tree* nd)
{
	result *= nd->p;
	if (nd->lc == NULL)return;
	if (mp.find(nd->desc) != mp.end()) cal(nd->lc); else cal(nd->rc);
}
int main()
{
freopen("r1b\\A-large.in", "r", stdin);
freopen("r1b\\A-large.out", "w", stdout);
	int cas;scanf("%d", &cas);
	int id = 1;
	while (cas--)
	{
		scanf("%*d");
		Tree* nd = build();
		//show(nd);
		int k;cin>> k;
		printf("Case #%d:\n", id++);
		while (k--)
		{
			mp.clear();
			string str;cin>>str;
			int n;cin>>n;
			for (int i = 0; i < n; ++i)
			{
				cin>>str;++mp[str];
			}
			result = 1;
			cal(nd);
			printf("%.7f\n", result);
		}
		destroy(nd);
	}
	return 0;
}
