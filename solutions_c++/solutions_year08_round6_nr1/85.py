#include <stdio.h>
#include <string.h>
#include <math.h>

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
const int MAXN = 110;
typedef pair<int, int>	pii;
typedef vector<pii> vi;

const int INF = 1 << 30;

int 	cas, T = 0;
int 	n, m;
vi 		bird;
vi 		not;
int 	xm, xi, ym, yi;
int 	_xm, _xi, _ym, _yi;

bool 	Bird(int w, int h)
{
	if (xi <= w && w <= xm && yi <= h && h <= ym)
		return true;
	else
		return false;
}

int 	NotBird(int w, int h)
{
	if (_xi <= w && w <= _xm && _yi <= h && h <= _ym)
		return true;
	else
	{
		int 	nxm, nxi, nym, nyi;
		
		nxm = max(xm, w);
		nxi = min(xi, w);
		nym = max(ym, h);
		nyi = min(yi, h);
		int 	sz = not.size();
		
		for (int i=0; i<sz; i++)
		{
			if (nxi <= not[i].first && not[i].first <= nxm
				&& nyi <= not[i].second && not[i].second <= nym)
					return true;
		}
		return false;
	}	
}

void print()
{
	printf("Case %d:\n", ++T);
}



int main()
{
	int 	i, j, k;

	freopen("a_small.out", "w", stdout);
	freopen("A-small-attempt0.in", "r", stdin);	
	
	for (scanf("%d", &cas); cas; cas--)
	{
		bird.clear();
		not.clear();
		xm = ym = -INF;
		yi = xi = INF;
	
		_xm = _ym = -INF;
		_yi = _xi = INF;	
			
		scanf("%d", &n);
		for (i=0; i<n; i++)
		{
			int 	a, b;
			string 	msg;
			char 	line[100];
			
			scanf("%d %d", &a, &b);
			cin >> msg;
			
			
			if (msg == "BIRD")
			{
				pii 	temp(a, b);
				bird.push_back(temp);
				
				xm = max(xm, a);
				xi = min(xi, a);
				ym = max(ym, b);
				yi = min(yi, b);
			}
			else
			{
				gets(line);
				pii 	temp(a, b);
				not.push_back(temp);
				
				_xm = max(xm, a);
				_xi = min(xi, a);
				_ym = max(ym, b);
				_yi = min(yi, b);
			}
		}
		
		scanf("%d", &m);
		
		print();
		for (i=0; i<m; i++)
		{
			int 	a, b;
			scanf("%d %d", &a, &b);
			bool 	bd = Bird(a, b);
			bool 	nb = NotBird(a, b);
		
			if (bd)	 
				printf("%s\n", "BIRD");
			else if (nb)
				printf("NOT BIRD\n");
			else
				printf("UNKNOWN\n");				
		}
		
		//print();
	}

	return 0;
}
