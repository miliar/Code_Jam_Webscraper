#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<deque>
#include<map>
#include<functional>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOREACH(i,x) for(typeof(x)::iterator it=(x).begin(); it!=(x).end(); ++it)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define pb	push_back
#define mp	make_pair
#define eps	1e-15
#define inf 0x3FFFFFFF

typedef long long int lint;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

void solve()
{
	map<pair<int, int>, bool> m[2];
	typedef map<pair<int, int>, bool>::iterator map_it;

	int r;
	scanf("%d",&r);
	REP(i,r) {
		int x1, x2, y1, y2;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		for(int x=x1; x<=x2; x++)
			for(int y=y1; y<=y2; y++)
				m[0][make_pair(x, y)] = true;
	}

	int cur = 0;
	int result = 0;

	while(m[cur].size() != 0) {
		int next = (cur + 1) % 2;
		m[next].clear();
		for(map_it it=m[cur].begin(); it != m[cur].end(); ++it) {
			int x = it->first.first;
			int y = it->first.second;
			if (m[cur].find(make_pair(x-1, y+1)) != m[cur].end()) {
				m[next][make_pair(x,y+1)] = true;
			}
			if (m[cur].find(make_pair(x-1, y)) != m[cur].end() ||
					m[cur].find(make_pair(x, y-1)) != m[cur].end())
				m[next][make_pair(x,y)] = true;
		}
		cur = next;
		result++;
	}
	printf("%d\n",result);
}

int main(void)
{
	//freopen("","r",stdin);
	//freopen("T-small.out","w",stdout);
	int test;
	scanf("%d",&test);
	REP(i,test) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

