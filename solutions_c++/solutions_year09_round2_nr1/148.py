
#define _CRT_SECURE_NO_DEPRECATE 

#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 

using namespace std; 

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define EPS 1e-7
#define Pi 3.14159265358979

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PI;

char buf[1 << 17];

struct tree
{
	string name;
	double val;
	tree *left;
	tree *right;
};

char b[1000];

tree* read(string str)
{
	int pos = 0;
	while(str[pos] != '(')
		++pos;
	++pos;
	str = str.substr(pos);
	pos = str.length() - 1;
	while(str[pos] != ')')
		--pos;
	str = str.substr(0, pos);
	tree *res = new tree();
	if(sscanf(str.c_str(), "%lf%s", &res->val, b) == 2)
	{
		res->name = b;
		pos = 0;
		while(str[pos] != '(')
			++pos;
		str = str.substr(pos);
		pos = 1;
		int cnt = 1;
		while(cnt != 0)
		{
			if(str[pos] == '(')
				++cnt;
			if(str[pos] == ')')
				--cnt;
			++pos;
		}
		res->left = read(str.substr(0, pos));
		res->right = read(str.substr(pos + 1));
	}
	return res;
}

double f(tree* t, vector<string> &V, double p)
{
	p *= t->val;
	if(t->name == "")
		return p;
	if(binary_search(ALL(V), t->name))
		return f(t->left, V, p);
	return f(t->right, V, p);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	gets(buf);
	sscanf(buf, "%d", &T);
	REP(I, T)
	{
		gets(buf);
		int L;
		sscanf(buf, "%d", &L);
		string str = "";
		REP(i, L)
		{
			gets(buf);
			str += buf;
			str += " ";
		}
		tree *t = read(str);
		gets(buf);
		int n;
		sscanf(buf, "%d", &n);
		printf("Case #%d:\n", I + 1);
		REP(i, n)
		{
			gets(buf);
			istringstream iss(buf);
			int k;
			string s;
			iss >> s >> k;
			vector<string> V;
			REP(j, k)
			{
				iss >> s;
				V.pb(s);
			}
			sort(ALL(V));
			printf("%.7lf\n", f(t, V, 1));
		}
	}
	return 0;
}