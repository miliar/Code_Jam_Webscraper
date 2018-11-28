// A2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int hw[110][110];
int ph[110][110];
int pw[110][110];
int testcase, h, w;
int direction[4][2];
void solve()
{
	map<int,int> map_assign;
	int h_i, w_i, d_i;
	int m_a, m_h, m_w, d_h, d_w;
	for (h_i = 0; h_i < h; ++h_i)
	{
		for (w_i = 0; w_i < w; ++w_i)
		{
			ph[h_i][w_i] = -1;
			pw[h_i][w_i] = -1;
		}
	}

	for (h_i = 0; h_i < h; ++h_i)
	{
		for (w_i = 0; w_i < w; ++w_i)
		{
		
			m_a = hw[h_i][w_i];
			d_h = -1;
			d_w = -1;
			for (d_i = 0; d_i < 4; ++d_i)
			{
				m_h = h_i+direction[d_i][0];
				m_w = w_i+direction[d_i][1];
				if (m_h >= 0 && m_h < h &&
					m_w >= 0 && m_w < w && hw[m_h][m_w] < m_a)
				{
					d_h = m_h;
					d_w = m_w;
					m_a = hw[m_h][m_w];
				}
			}
			if (d_h >=0 && d_w >= 0)
			{
				ph[h_i][w_i] = d_h;
				pw[h_i][w_i] = d_w;
			}
		}
	}
	for (h_i = 0; h_i < h; ++h_i)
	{
		for (w_i = 0; w_i < w; ++w_i)
		{
			while (ph[h_i][w_i] >= 0 && pw[h_i][w_i] >= 0 &&
				ph[ph[h_i][w_i]][pw[h_i][w_i]] >= 0 &&
				pw[ph[h_i][w_i]][pw[h_i][w_i]] >= 0 )
			{
				d_h = ph[h_i][w_i];
				d_w = pw[h_i][w_i];
				ph[h_i][w_i] = ph[d_h][d_w];
				pw[h_i][w_i] = pw[d_h][d_w];
			}
		}
	}
	for (h_i = 0; h_i < h; ++h_i)
	{
		for (w_i = 0; w_i < w; ++w_i)
		{
			if (ph[h_i][w_i] < 0 || pw[h_i][w_i] < 0)
			{
				ph[h_i][w_i] = h_i;
				pw[h_i][w_i] = w_i;
			}
		}
	}
	d_h = 'a';
	map<int,int>::iterator iter;
	for (h_i = 0; h_i < h; ++h_i)
	{
		for (w_i = 0; w_i < w; ++w_i)
		{
			d_i = ph[h_i][w_i]*w+pw[h_i][w_i];
			if ((iter=map_assign.find(d_i)) != map_assign.end())
				ph[h_i][w_i] = iter->second;
			else
			{
				map_assign.insert(pair<int,int>(d_i,d_h));
				ph[h_i][w_i] = d_h;
				d_h++;
			}
		}
	}
}
int _tmain(int argc, _TCHAR* argv[])
{
	freopen("..\\B-large.in","r",stdin);
	freopen("..\\B1.out","w",stdout);
	scanf("%d", &testcase);
	
	direction[0][0] = -1;
	direction[0][1] = 0;
	direction[1][0] = 0;
	direction[1][1] = -1;
	direction[2][0] = 0;
	direction[2][1] = 1;
	direction[3][0] = 1;
	direction[3][1] = 0;
	int h_i, w_i;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		scanf("%d %d", &h, &w);
		for (h_i = 0; h_i < h; ++h_i)
		{
			for (w_i = 0; w_i < w; ++w_i)
			{
				scanf("%d", &hw[h_i][w_i]);
			}
		}
		printf("Case #%d:\n",caseId);
		solve();
		for (h_i = 0; h_i < h; ++h_i)
		{
			for (w_i = 0; w_i < w; ++w_i)
			{
				printf("%c ", ph[h_i][w_i]);
			}
			printf("\n");
		}
		fflush(stdout);
	}
	return 0;
}


