// 2.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"

#include<vector>
#include<algorithm>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	scanf("%d", &t);
	for (int k = 1; k <= t; k++)
	{
		int c;
		scanf("%d", &c);
		char comb[64][4];
		for (int x = 0; x < c; x++)
			scanf("%s", comb[x]);

		int d;
		scanf("%d", &d);
		char opps[64][3];
		for (int x = 0; x < d; x++)
			scanf("%s", opps[x]);

		int n;
		scanf("%d", &n);
		char str[128];
		scanf("%s", str);

		//run
		vector<char> out;
		for (int x = 0; x < n; x++)
		{
			out.push_back(str[x]);

START:
			//check comb
			if (out.size() >= 2)
			{
				unsigned s = out.size();
				int f;
				for (f = 0; f < c; f++)
					if ((out[s-2] == comb[f][0] && out[s-1] == comb[f][1]) ||
						(out[s-1] == comb[f][0] && out[s-2] == comb[f][1]))
						break;
				if (f < c)
				{
					out.pop_back();
					out.pop_back();
					out.push_back(comb[f][2]);
					goto START;
				}
			}

			//check opps
			if (out.size() >= 2)
			{
				unsigned s = out.size();
				int f;
				for (f = 0; f < d; f++)
					if (find(out.begin(),out.end(),opps[f][0]) != out.end() &&
						find(out.begin(),out.end(),opps[f][1]) != out.end())
						break;
				if (f < d)
					out.clear();
			}

		}

		//result
		printf("Case #%d: [", k);
		for (unsigned x = 0; x < out.size(); x++)
		{
			if (x == 0) printf("%c", out[0]);
			else printf(", %c", out[x]);
		}
		printf("]\n");
	}
	return 0;
}

