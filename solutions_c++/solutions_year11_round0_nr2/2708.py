#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

struct node
{
	char first, second, son;
};

char combine(char a, char b, const vector<node> &com)
{
	for (int i = 0; i < com.size(); i++)
	{
		if (com[i].first == a && com[i].second == b ||
			com[i].second == a && com[i].first == b)
		{
			return com[i].son;
		}
	}

	return char(0);
}

bool oppose(char a, char b, const vector<node>& opp)
{
	for (int i = 0; i < opp.size(); i++)
	{
		if (opp[i].first == a && opp[i].second == b ||
			opp[i].second == a && opp[i].first == b)
		{
			return true;
		}
	}

	return false;
}

void solve(const vector<node>& com, const vector<node>& opp, const string& seq)
{
	if (seq.empty())
	{
		printf("[]\n");
		return;
	}

	vector<char> ans;

	for (int i = 0; i < seq.size(); i++)
	{
		char c = seq[i];
		if (ans.empty())
		{
			ans.push_back(c);
		}
		else
		{
			char last = ans[ans.size() - 1];
			char son = combine(c, last, com);
			if (son != 0)
			{
				ans.pop_back();
				ans.push_back(son);
				continue;
			}

			bool bOpp = false;
			for (int j = ans.size() - 1; j >= 0; j--)
			{
				if (oppose(c, ans[j], opp))
				{
					ans.clear();
					bOpp = true;
					break;
				}
			}

			if (!bOpp)
			{
				ans.push_back(c);
			}
		}
	}

	putchar('[');
	if (!ans.empty())
	{
		for (int i = 0; i < ans.size() - 1; i++)
		{
			printf("%c, ", ans[i]);
		}
		printf("%c", ans[ans.size() - 1]);
	}
	
	putchar(']');
	putchar('\n');
}

void solve()
{
	int caseNum;
	scanf("%d", &caseNum);
	char s[4];
	char buf[1024];

	for (int caseId = 1; caseId <= caseNum; caseId++)
	{
		printf("Case #%d: ", caseId);
		int m, n, k;

		scanf("%d", &m);
		vector<node> com;
		com.resize(m);
		for (int i = 0; i < m; i++)
		{
			scanf("%s", s);
			com[i].first = s[0];
			com[i].second = s[1];
			com[i].son = s[2];
		}

		scanf("%d", &n);
		vector<node> opp;
		opp.resize(n);
		for (int i = 0; i < n; i++)
		{
			scanf("%s", s);
			opp[i].first = s[0];
			opp[i].second = s[1];
		}

		scanf("%d", &k);
		scanf("%s", buf);
		string str(buf);
		solve(com, opp, str);		
	}
}

int main()
{
	char directoryName[] = "C:\\Documents and Settings\\GaoGuang\\My Documents\\Downloads\\";
	char dataFileName[]= "B-large";
	char inputFileName[256];
	char outputFileName[256];
	strcpy(inputFileName, directoryName);
	strcat(inputFileName, dataFileName);
	strcat(inputFileName, ".in");

	strcpy(outputFileName, directoryName);
	strcat(outputFileName, dataFileName);
	strcat(outputFileName, ".out");

	freopen(inputFileName, "r", stdin);
	freopen(outputFileName, "w", stdout);

	solve();

	return 0;
}