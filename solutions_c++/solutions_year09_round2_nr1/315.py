#pragma comment(linker, "/STACK:100000000")
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cctype>
using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(b); ++i)

typedef long long i64;
typedef unsigned long long u64;

struct
{
	double p;
	u64 key;
	int l, r;
} MEMO[1000000];

int nodes;



u64 GetKey(const char *ts)
{
	u64 key = 0, X = 257;
	for (int i=0; ts[i]; ++i)
		key = key * X + ts[i];
	return key;
}

int CreateNode(double p, u64 key)
{
	MEMO[nodes].p = p;
	MEMO[nodes++].key = key;
	return nodes - 1;
}

const u64 LEAF = (1LL<<60) - 1;

int CreateTree(char *s, int &len)
{
	if (s[0] != '(')
	{
		throw 0;
	}

	char ts[20];
	double p;
	sscanf(s+1, "%lf%s", &p, &ts);
	u64 key;
	if (ts[0] == ')')
		key = LEAF;
	else
		key = GetKey(ts);
		

	int ret = CreateNode(p, key);

	

	if (key != LEAF)
	{
		int l1, l2;
		char *s1 = strchr(s+1, '(');
		MEMO[ret].l = CreateTree(s1, l1);
		
		char *s2 = strchr(s1 + l1, '(');
		MEMO[ret].r = CreateTree(s2, l2);
		
		len = strchr(s2 + l2, ')') - s + 1;
	}
	else
	{
		len = strchr(s, ')') - s + 1;
	}

	return ret;
}

char inp[1000000];

double GetCute(int treeID, set<u64> &st)
{
	double res = MEMO[treeID].p;
	if (MEMO[treeID].key == LEAF)
		return res;
	if (st.find(MEMO[treeID].key) != st.end())
	{
		res *= GetCute(MEMO[treeID].l, st);
	}
	else
	{
		res *= GetCute(MEMO[treeID].r, st);
	}
	return res;
}

void addSpaces(char *inp)
{
	string s1 = inp, s2;
	FOR(i,0,s1.size())
		if (s1[i] == '(' || s1[i] == ')')
		{
			s2 += ' ';
			s2 += s1[i];
			s2 += ' ';
		}
		else
			s2 += s1[i];

	strcpy(inp, s2.c_str());
}

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

	int T;
	gets(inp);
	sscanf(inp, "%d", &T);
	FOR(cas, 1, T+1)
	{
		gets(inp);
		int L;
		sscanf(inp, "%d", &L);
		string sTree;
		FOR(l,0,L)
		{
			gets(inp);
			sTree += inp;
		}

		nodes = 0;
		int len;
		strcpy(inp, sTree.c_str());
		addSpaces(inp);
		sTree = inp+1;
		strcpy(inp, sTree.c_str());
		int treeID = CreateTree(inp, len);

		gets(inp);
		int A;
		sscanf(inp, "%d", &A);
		
		printf("Case #%d:\n", cas);
		
		FOR(i,0,A)
		{
			gets(inp);
			stringstream in(inp);
			string name;
			int n;
			in >> name >> n;
			set <u64> st;
			FOR(j,0,n)
			{
				string feature;
				in >> feature;
				st.insert(GetKey(feature.c_str()));
			}
			printf("%.10lf\n", GetCute(treeID, st));
		}

		
	}

	return 0;
}
	