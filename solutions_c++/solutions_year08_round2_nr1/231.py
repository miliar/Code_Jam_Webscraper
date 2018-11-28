#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;

int main(void) {
	int T;
	int Cases = 1;
	int n;
	long long int x, y, A, B, C, D, M;
	long long int xm, ym;
	long long int res;
	vector<pair<long long int,long long int> > v;
	scanf("%d", &T);
	while(T--) {		
		v.clear();
		res = 0;
		scanf("%d%lld%lld%lld%lld%lld%lld%lld", &n, &A, &B, &C, &D, &x, &y, &M);
		v.push_back(make_pair(x,y));
		for(int i = 1; i < n; ++i){
			x = (A*x + B) % M;
			y = (C*y + D) % M;
			v.push_back(make_pair(x,y));
		}
		for(int i = 0; i < n; ++i) {
			for(int j = i+1; j < n; ++j) {
				for(int k = j+1; k < n; ++k) {					
					xm = v[i].first + v[j].first + v[k].first;
					ym = v[i].second + v[j].second + v[k].second;
					if(xm % 3 == 0 && ym % 3 == 0) res++;					
				}				
			}
		}
		printf("Case #%d: %lld\n", Cases++, res);	
	}	
	return 0;
}
