#include <algorithm> 
#include <cassert>
#include <cctype> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <iostream>
#include <map> 
#include <set> 
#include <string> 
#include <sstream>
#include <queue> 
#include <vector> 
using namespace std;

int T, R, cap, N, ans;
vector <int> g;

void read()
{
	scanf("%d%d%d", &R, &cap, &N);
	int t;
	g.clear();
	for (int i=0; i<N; i++)
	{
		scanf("%d",&t);
		g.push_back(t);
	}
}

int putpeople(int cur)
{
	int res=0, tot=g[cur];
	while (true)
	{
		res++;
		cur++; cur %=N;
		if (tot +g[cur] <=cap)
			tot += g[cur];
		else
		{
			if (res <=N)
			return res;
			else return N;
		}
	}
}

int getmoney(int beg, int num)
{
	int res=0;
	for (int i=beg; i<beg+num; i++)
		res += g[i%N];
	return res;
}



void solve()
{
	map <int, int> money;
	vector <int> order;
	int curgr=0, curmoney=0, dm, gr, cgr, cm, beg;

	money.insert(make_pair(0,0));
	order.push_back(0);

	while (true)
	{
		gr = putpeople(curgr);
		dm = getmoney(curgr, gr);
		curgr+=gr;
		curgr %= g.size();

		curmoney+=dm;
		if (money.find(curgr)==money.end())
		{
			money.insert(make_pair(curgr,curmoney));
			order.push_back(curgr);
		}
		else
		{
			for (beg=0; beg<order.size(); beg++)
				if (order[beg]==curgr) break;
			cgr = order.size()-beg;
			cm = curmoney-money[curgr];
			break;
		}
	}
	if (R<=beg) ans = money[order[R]];
	else
	{
		int en = (R-beg)%cgr;
		ans = cm*((R-beg)/cgr)+money[order[beg+en]];
	}
}

void write(int i)
{
	printf("Case #%d: %d",i+1,ans);
	if (i!=T-1) printf("\n");
}
int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	

	scanf("%d",&T);
	
	for (int i=0; i<T; i++)
	{
		read();
		solve();
		write(i);
	}
	return 0;
}
