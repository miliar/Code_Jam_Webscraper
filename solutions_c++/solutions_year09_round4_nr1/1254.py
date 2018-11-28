#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <bitset>

using namespace std;

#define pb push_back
#define SZ(v) ((int)(v).size())
#define REP(i, a) for(int i=0; i<(a); ++i)
#define SQR(a) ((a)*(a))
#define TR(v, it) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define ALL(v) (v).begin(), (v).end()

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;

char buf[100];

bool good(const vi &v){
	REP(i, SZ(v)){
		if(i < v[i]) return false;
	}
	return true;
}

inline bool solve(int tc){
	int n;
	scanf("%d", &n);
	vi v;
	REP(i, n){
		scanf("%s", buf);
		char *l = strrchr(buf, '1');
		if(l == NULL)
			v.pb(-1);
		else
			v.pb(l-buf);
	}
	set<vi> visited;
	typedef pair<vi, int> state;
	queue<state> q;
	bool done = false;
	int ans = 0;
	if(good(v)) done = true;
	visited.insert(v);
	q.push(state(v, 0));
	while(!q.empty() && !done){
		state s = q.front();q.pop();
		for(int i = 0; i<n-1; ++i){
			vi tmp = s.first;
			swap(tmp[i], tmp[i+1]);
			if(visited.find(tmp) != visited.end()) continue;
			if(good(tmp)){
				ans = s.second+1;
				done = true;
				break;
			}
			visited.insert(tmp);
			q.push(state(tmp, s.second+1));
		}
	}
	printf("Case #%d: %d\n", tc, ans);
	return true;
}

int main (int argc, char const *argv[]) {
	int n; scanf("%d",&n);
	for(int k=1;solve(k)&&k<n;k++);
	return 0;
}