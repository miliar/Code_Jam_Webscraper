#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <stdio.h>

#include <cassert>
using namespace std;

#define ALL(ar)       (ar).begin(),(ar).end()
#define SZ(a)         int((a).size())
#define REP(i,n)      for(int i=0,len123=(n);i<len123;i++)
#define FOR(i,n,m)    for(int i=(n),len123=(m);i<len123;i++)
#define INF           (1<<30)
typedef long long          LL;
typedef long double        LD;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int,int>      II;

int TC, d, AB, BA;
vector<pair<pair<double,double>, bool> > vv;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in", "rt", stdin);
    freopen("out.out", "wt", stdout);
#endif

    scanf("%d", &TC);
	REP(tc,TC)
	{
		scanf("%d", &d);
		scanf("%d %d", &AB, &BA);
		
		REP(i,AB+BA) {
			int h, m, h2, m2; string c;
			cin >> c;
			stringstream c1(string(c.begin(),c.begin()+2));	c1 >> h;
			stringstream c2(string(c.begin()+3,c.begin()+5)); c2 >> m;
			
			cin >> c;
			stringstream c3(string(c.begin(),c.begin()+2));	c3 >> h2;
			stringstream c4(string(c.begin()+3,c.begin()+5)); c4 >> m2;
			vv.push_back(make_pair(make_pair(h+((double)m)/60.0, h2+((double)m2)/60.0), i >= AB));
		}
		
		unique(ALL(vv));
		sort(ALL(vv));
		int len = SZ(vv);

		multiset<double> cache[2];
		int ans[2] = {0,0};

		double dd = ((double)d)/60.0;

		REP(i,len)
		{
			pair<pair<double,double>, bool>& p = vv[i];
			multiset<double>::iterator beg = cache[p.second].begin();
			if (!cache[p.second].empty() && p.first.first-(*beg)-dd >= -(1E-6)) {
				cache[p.second].erase(beg);
//				cache[!p.second].insert(p.first.second);
			}
			else
				ans[p.second]++;
			cache[!p.second].insert(p.first.second);
			printf("");
		}
		
		printf("Case #%d: %d %d\n", tc+1, ans[0], ans[1]);
		vv.clear();
	}

    return 0;
}
