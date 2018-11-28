#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) ((x).begin, (x).end)
#define eps	1e-15

typedef long long int lint;

int solve()
{
	vector<pair<int, int> > v;
	int k;
	scanf("%d",&k);

	REP(i,k) {
		char buf[128];
		int pos;
		scanf("%s%d",buf,&pos);
		v.push_back(make_pair( buf[0] == 'O' ? 0 : 1, pos ) );
	}
	int result = 0;

	int pos[2] = {1, 1};
	int time[2] = {0, 0};
	
	REP(i,k) {
		int robot = v[i].first;
		int dest = v[i].second;

		int move = abs(dest-pos[robot]);
		move -= result - time[robot];
		if ( move > 0 ) result += move;
		pos[robot] = dest;
		time[robot] = ++result;
	}
	return result;
}

int main(void)
{
	int T;
	scanf("%d",&T);

	REP(i,T) {
		printf("Case #%d: %d\n", i+1, solve() );

	}

	return 0;
}

