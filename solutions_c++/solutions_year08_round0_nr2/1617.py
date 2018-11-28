#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctype.h>
#include <bitset>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2))) 
#define mset(a, val) memset(a, val, sizeof(a))
#define deb(x) cout<<#x<<" = "<<(x)<<endl
#define all(a) (a).begin(),(a).end() 
#define ab(a) (((a)>0)?(a):(-(a))) 
#define sqr(a) ((a)*(a)) 
#define sz(a) int((a).size())

#define PB push_back
#define MP make_pair
#define INF 0x3fffffff
#define X first
#define Y second

int u[405], m1, m2, time;
struct A
{
	A(pair<int, int> p, int b){ a = p; pos = b; }
	pair<int, int> a;
	int pos;
	bool operator < (A &b)
	{
		if(a.first == b.a.first)
			return a.second < b.a.second;
		return a.first < b.a.first;
	}
};

vector< A > va, vd;

int findBest()
{
	int i, j, res = -1, k, maxx = -1, len = va.size();
	for(i = 0; i < len; i++)
	{
		k = 1;
		if(u[i] == 0)
		{
			int ind = i, par = va[i].pos;
			for(j = i + 1; j < len; j++)
				if( u[j] == 0 && va[ind].a.second + time <= va[j].a.first && par != va[j].pos )
				{
					ind = j;
					par = va[j].pos;
					k++;
				}
		}
		if(u[i] == 0 && k > maxx )
		{
			maxx = k;
			res = i;
		}	
	}
	return res;
}
void put(int start)
{
	if( start == -1 ) return;
	int i, len = va.size();
	int ind = start, par = va[start].pos;
	u[start] = 1;
	for(i = start + 1; i < len; i++)
	{
		if( u[i] == 0 && va[ind].a.second + time <= va[i].a.first && par != va[i].pos )
		{
			ind = i;
			par = va[i].pos;
			u[ind] = 1;
		}
	}
}
int main()
{
	int i, j, n, m;
	int max = 0, T;

	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	scanf("%d", &T);

	int k = 1;
	va.clear(); vd.clear();
	
	while(k <= T)
	{
		int h1, m1, h2, m2;
		scanf("%d%d%d", &time, &n, &m);

		mset(u, 0);
		va.clear();
		for(i = 0; i < n; i++)
		{
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			va.PB( A(MP(h1*60+m1, h2*60+m2), 1) );
		}
		for(i = 0; i < m; i++)
		{
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			va.PB( A(MP(h1*60+m1, h2*60+m2), 2) );
		}	

		m1 = 0, m2 = 0;
		sort(all(va));

		while( 1 )
		{
			int way = findBest();
			put(way);
			if( way != -1 && va[way].pos == 1 )	m1++;
			else if( way != -1 && va[way].pos == 2 )	m2++;

			int c = 0;
			for(i = 0;  i < va.size(); i++)
				if(u[i] == 0) c++;
			if(c == 0) break;
		}
		printf("Case #%d: %d %d\n", k, m1, m2);
		k++;
	}
	return 0;
}