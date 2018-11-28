#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
using namespace std;
#define 	no	first 	
#define		st	second	

typedef 	pair<int, int>		pii;

const int MAXN = 2010;

int 	cas, T;

int 	n, m;
vector< pii >	pep[2010];

int 	rnt[MAXN];
vector< int >	temp;

bool 	check()
{
	int 	i, j, k;
	bool 	flag = true;
	
	temp.clear();
	for (i=0; i<m; i++)	
	{
		k = pep[i].size();
		int 	cnt = 0;
		int 	add = -1;
		for (j=0; j<k; j++)
		{
			if (rnt[pep[i][j].no] == pep[i][j].st)	
				cnt++;
			else
			{
				if (pep[i][j].st == 1)
				{
					//temp.push_back(pep[i][j].no);
					add = pep[i][j].no;
				}
			}
		}
		
		if (cnt == 0 )
		{
			if (add >=0)	temp.push_back(add);
			flag = false;
		}
	}
	
	return flag;
}

int main()
{
	int 	i, j, k;

	freopen("B-large.in", "r", stdin);
	freopen("B-Large.out", "w", stdout);

	
	for (scanf("%d", &cas); cas; cas--)
	{
		scanf("%d %d", &n, &m);
		for (i=0; i<m; i++)	pep[i].clear();
		
		for (i=0; i<m; i++)
		{
			int 	tt;
			scanf("%d", &tt);
			for (j=0; j<tt; j++)
			{
				int 	no, st;
				scanf("%d %d", &no, &st);
				no--;
				pep[i].push_back(make_pair(no, st));
			}
		}

		memset(rnt, 0, sizeof(rnt));
		
		do
		{
			check();
			if (temp.size() != 0)
			{
				k = temp.size();
				for (i=0; i<k; i++)
					rnt[temp[i]] = 1;
			}
			else
				break;
			
		} while (1);
		
		printf("Case #%d:", ++T);	
		
		if (check())
		{
			for (i=0; i<n; i++)
				printf(" %d", rnt[i]);
			printf("\n");
		}
		else
			printf(" IMPOSSIBLE\n");
	}

	return 0;
}
