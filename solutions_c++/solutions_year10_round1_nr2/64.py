#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

int d, i, m, n;

int memo[105][260];
int tab[105];

int best(int from, int prev){
	if(from == n) return 0;
	int& res = memo[from][prev+1];
	if(res != -1) return res;
	
	res = d + best(from+1, prev); // del
	for(int val = 0; val <= 255; val++){
		int dist = ( 
			(val == prev || prev == -1) ? 0 : (
				m == 0 ? 1000000000 : i*((abs(val-prev)-1)/m)
			)
		);  
		int prop = dist;
		prop += abs(tab[from]-val);
		prop += best(from+1, val);
		res = min(res, prop);
		//printf("prop: %d\n", prop);
	}
	return res;
}

int main(){
	int lz;
	scanf("%d", &lz);
	for(int cnt = 1; cnt <= lz; cnt++){
		scanf("%d%d%d%d", &d, &i, &m, &n);
		for(int j = 0; j < n; j++) scanf("%d", &tab[j]);
		int dif = 0;
		for(int j = 1; j < n; j++) if( tab[j]!=tab[j-1]) dif++;
		memset(memo, -1, sizeof(memo));

		printf("Case #%d: %d\n", cnt, best(0,-1));
	}
	return 0;
}
