#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

char inString[10000];
int inLength;

double tree1[100000];
string tree2[100000];
int treeNext[100000];
int treeN;

set<string> features;

bool testBlank(char a)
{
	return (a == ' ' || a == '\n' || a == '\r');
}

void parseTree(int a, int &pos)
{
	if (a >= 100000)
	{
		printf("OverFlow!!!\n");
		exit(1);
	}
	//printf("in %d, %d\n", a, pos);
	while (testBlank(inString[pos]))
	{
		if (pos >= inLength)
		{
			return;
		}
		++pos;
	}

	//if (inString[pos] != '(') printf("Error!!!\n");
	++pos;

	while (testBlank(inString[pos]))
	{
		++pos;
	}

	char p[100];
	int pPos = 0;

	while (inString[pos] == '.' || (inString[pos] >= '0' && inString[pos] <= '9'))
	{
		p[pPos++] = inString[pos];
		++pos;
	}
	p[pPos] = 0;

	tree1[a] = atof(p);
	//printf("p = %9.7lf\n", tree1[a]);

	while (testBlank(inString[pos]))
	{
		++pos;
	}

	if (inString[pos] == ')')
	{
		treeNext[a] = treeN;
		tree1[treeN + 0] = -1;
		tree1[treeN + 1] = -1;
		tree2[treeN + 0].clear();
		tree2[treeN + 1].clear();
		treeN += 2;

		++pos;

		//printf("out1 %d\n", a);
		return;
	}

	char feature[100];
	int fPos = 0;

	while (!testBlank(inString[pos]))
	{
		feature[fPos++] = inString[pos];
		++pos;
	}
	feature[fPos] = 0;
	tree2[a] = feature;

	//printf("feature = %s\n", tree2[a].c_str());

	treeNext[a] = treeN;
	treeN += 2;
	parseTree(treeNext[a] + 0, pos);
	parseTree(treeNext[a] + 1, pos);

	while (testBlank(inString[pos]))
	{
		++pos;
	}

	//if (inString[pos] != ')') printf("Error2!!!\n");
	++pos;

	//printf("out2 %d\n", a);
}

double solve(void)
{
	double p = 1.0;

	int now = 0;

	while (tree1[now] != -1.0)
	{
		p *= tree1[now];

		if (features.find(tree2[now]) != features.end())
		{
			now = treeNext[now] + 0;
		}
		else
		{
			now = treeNext[now] + 1;
		}
	}

	return p;
}

int main(void)
{
	int T;
	scanf("%d ", &T);

	for (int t = 1 ; t <= T ; ++t)
	{
		printf("Case #%d:\n", t);

		int A;
		scanf("%d ", &A);

		inLength = 0;
		memset(inString, 0, 10000);
		for (int i = 0 ; i < A ; ++i)
		{
			fgets(inString + inLength, 100, stdin);
			inLength = strlen(inString);
		}

		treeN = 1;
		tree1[0] = -1;
		tree2[0].clear();
		int pos = 0;
		parseTree(0, pos);

		//printf("Parsed!!\n");

		int n;
		scanf("%d ", &n);

		for (int i = 0 ; i < n ; ++i)
		{
			char name[100];
			int m;

			scanf("%s %d ", name, &m);

			//printf("--%s\n", name);
			features.clear();
			for (int j = 0 ; j < m ; ++j)
			{
				char feature[100];
				scanf("%s ", feature);

				features.insert(feature);
			}

			printf("%9.7lf\n", solve());
		}
	}
}
