#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <deque>

using namespace std;

#define reep(i,f,t) for(int i=f ; i<int(t) ; ++i)
#define rep(i,n) reep(i, 0, n) 

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

double solve()
{
	int x, s, r, t, n;
	scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
	
	map<int, int> m;
	int sum = 0;
	rep(i, n){
		int b, e, w;
		scanf("%d%d%d", &b, &e, &w);
		m[w] += e-b;
		sum += e-b;
	}
	m[0] = x - sum;
	
	double ans = 0.0;
	double rem = t;
	for(map<int,int>::iterator i=m.begin(); i!=m.end(); ++i){
		double time = i->second / double(r + i->first);
		if(time > rem){
			time = rem;
		}
		ans += (i->second - time * (r + i->first)) / (s + i->first) + time;
		rem -= time;
	}
	
	return ans;
}

int main()
{
	int t;
	scanf("%d", &t);
	
	rep(i, t){
		printf("Case #%d: %lf\n", i+1, solve());
	}
	
	return 0;
}
