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

#define blue 0
#define orange 1

struct node
{
	int pos;
	int flag;  // 0 -> blue, 1 -> orange
};

int sign(int val)
{
	if (val > 0)
		return 1;
	return -1;
}

int solve(const vector<node>& seq)
{
	vector<int> bseq;
	vector<int> oseq;

	for (int i = 0; i < seq.size(); i++)
	{
		if (seq[i].flag == blue)
		{
			bseq.push_back(seq[i].pos);
		}
		else
		{
			oseq.push_back(seq[i].pos);
		}
	}

	int ans = 0;
	int bpos, opos;
	bpos = opos = 1;
	int bid, oid;
	bid = oid = 0;

	for (int i = 0; i < seq.size(); i++)
	{
		if (seq[i].flag == blue)
		{
			int cost = abs(bpos - seq[i].pos) + 1;
			bpos = seq[i].pos;
			ans += cost;
			bid++;

			if (oid < oseq.size())
			{
				int dis = oseq[oid] - opos;
				if (abs(dis) <= cost)
				{
					opos += dis;
				}
				else
				{
					opos += cost * sign(dis);
				}
			}
		}
		else
		{
			int cost = abs(opos - seq[i].pos) + 1;
			opos = seq[i].pos;
			ans += cost;
			oid++;

			if (bid < bseq.size())
			{
				int dis = bseq[bid] - bpos;
				if (abs(dis) <= cost)
				{
					bpos += dis;
				}
				else
				{
					bpos += cost * sign(dis);
				}
			}
		}
	}

	return ans;
}

void solve()
{
	int caseNum;
	scanf("%d", &caseNum);

	for (int caseId = 1; caseId <= caseNum; caseId++)
	{
		printf("Case #%d: ", caseId);
		int num;
		scanf("%d", &num);
		vector<node> seq;
		seq.resize(num);
		for (int i = 0; i < num; i++)
		{
			char s[2];
			int pos;
			scanf("%s %d", &s, &pos);

			seq[i].pos = pos;
			seq[i].flag = (s[0] == 'B' ? blue: orange); 
		}

		printf("%d\n", solve(seq));
	}
}

int main()
{
	char directoryName[] = "C:\\Documents and Settings\\GaoGuang\\My Documents\\Downloads\\";
	char dataFileName[]= "A-large";
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