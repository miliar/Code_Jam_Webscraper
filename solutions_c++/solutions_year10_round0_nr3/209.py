#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

typedef long long llong;
typedef pair<int, llong> PIL;

const int N = 1024;

int R, K, n, G[N];

PIL oneStep(int from)
{
	int seat = K, nid = from;
	llong get = 0;
	for(int i = 0; i < n; i++) {
		int gi = G[(from+i)%n];
		if(seat >= gi) { seat -= gi; get += gi; }
		else { nid = (from+i)%n; break; }
	}
	return PIL(nid, get);
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		scanf("%d %d %d", &R, &K, &n);
		for(int i = 0; i < n; i++) scanf("%d", &G[i]);
		llong income[N], step[N];
		memset(income, 0, sizeof(income));
		memset(step, -1, sizeof(step));
		step[0] = 0;
		income[0] = 0;
		int cur = 0, id = 0;
		llong res = 0;
		bool cyced = false;
		while(cur < R) {
			PIL pr = oneStep(id);
			int nid = pr.first, ns = step[id]+1;
			res += pr.second;
			id = nid;
			cur++;
		
			if(cyced) continue;
			if(step[nid] == -1) { step[nid] = ns; income[nid] = res; continue; }
			int cyc_l = ns-step[nid];
			llong cycGet = res-income[nid];
			int cyc_n = (R-cur)/cyc_l;
			cur += cyc_n*cyc_l;
			res += cyc_n*cycGet;
			cyced = true;
		}
		printf("Case #%d: %lld\n", t+1, res);
	}
	
	return 0;
}

