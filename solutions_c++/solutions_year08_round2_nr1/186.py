#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>

using namespace std;

#ifndef DEB
#define DEBUG(out)
#else
#define DEBUG(out) cerr << __LINE__ << ":\t" << out << endl
#endif

long long cm[3][3];

int main(){
	int tcs;
	scanf("%d", &tcs);
	for(int tc=0; tc<tcs; ++tc){
		long long n, a, b, c, d, x0, y0, m;
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &a, &b, &c, &d, &x0, &y0, &m);
		vector<long long> x;
		vector<long long> y;
		x.push_back(x0);
		y.push_back(y0);
		DEBUG(x0 << " " << y0);
		for(int i=1; i<n; ++i){
			x0 = (a * x0 + b) % m;
			y0 = (c * y0 + d) % m;
			DEBUG(x0 << " " << y0);
			x.push_back(x0);
			y.push_back(y0);
		}

		memset(cm, 0, sizeof(cm));
		long long count = 0;
		for(int i=0; i<n; ++i)
			++cm[x[i]%3][y[i]%3];
		for(int i0=0; i0<3; ++i0){
			for(int i1=0; i1<3; ++i1){
				long long c0 = cm[i0][i1];
				for(int j0=0; j0<3; ++j0){
					for(int j1=0; j1<3; ++j1){
						long long c1 = cm[j0][j1];
						if(j0 == i0 && j1 == i1)
							--c1;
						for(int k0=0; k0<3; ++k0){
							for(int k1=0; k1<3; ++k1){
								long long c2 = cm[k0][k1];
								if(k0 == i0 && k1 == i1)
									--c2;
								if(k0 == j0 && k1 == j1)
									--c2;
								if(c0 <= 0 || c1 <= 0 || c2 <= 0)
									continue;
								if((i0+j0+k0)%3==0 && (i1+j1+k1)%3==0)
									count += c0*c1*c2;
							}
						}
					}
				}
			}
		}
		printf("Case #%d: %lld\n", tc+1, count/6);
	}
}
