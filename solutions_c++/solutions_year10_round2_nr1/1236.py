#include <stdio.h>
#include <string.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <stack>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

typedef __int64 LL;

int min(int a, int b)
{
	if (a>b) return b;
	return a;
}

int main()
{
	freopen("a.in.txt","r",stdin);
	freopen("a.out.txt","w",stdout);

	int kase, tCase = 0;
	scanf ("%d",&kase);

	while (kase--)
	{
		int N, M, i, j, k, p, push=0, res = 0, no = 0;
		char input[500], list[500], quary[500], hold[500];
		scanf ("%d%d",&N,&M);
		getchar();
		vector<string>dir_given[500], testcase;
		vector<int>millo;
		for (i=0; i<N; i++)
		{
			k=1;
			string a;
			gets(input);

			while (1)
			{
				p=0;
				while (input[k] != '/' && input[k] != NULL)
				{
					list[p] = input[k];
					k++;
					p++;
				}
				list[p] = '\0';
				a = list;
				dir_given[push].push_back(a);
				if (input[k] != NULL) k++;
				else break;
			}
			push++;
		}
		for (j=0; j<M; j++)
		{
			millo.clear();
			testcase.clear();
			gets(quary);
			k=1;
			string b;
			for (int time = 0;;time++)
			{
				p=0;
				while (quary[k] != '/' && quary[k] != NULL)
				{
					hold[p] = quary[k];
					k++;
					p++;
				}
				hold[p] = '\0';
				b = hold;
				testcase.push_back(b);
				if (quary[k] != NULL) k++;
					else break;
			}
			int finalCheck, r, high = 0, index = 0, w, e, small;
			for (finalCheck = 0; finalCheck < push; finalCheck++)
			{
				small = min(testcase.size(),dir_given[finalCheck].size());
				for (r=0; r<small; r++)
					if (dir_given[finalCheck][r] != testcase[r]) break;
				millo.push_back(r);
			}
			for (w=0; w<millo.size(); w++)
			{
				if (millo[w] > high)
				{
					high = millo[w];
					index = w;
				}
			}
			res += (testcase.size()-high);
			if (testcase.size()-high != 0)
			{
				for (e=0; e<testcase.size(); e++)
					dir_given[push].push_back(testcase[e]);
				push++;
			}
		}
		printf ("Case #%d: %d\n",++tCase,res);
	}

	return 0;
}