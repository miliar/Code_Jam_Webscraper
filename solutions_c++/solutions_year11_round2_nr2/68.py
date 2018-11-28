//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <complex>
#include <vector>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define F first
#define S second

using namespace std;
typedef pair<int, int> joft;
typedef complex<double> point;

const int MAX_C = 1000;

int c;
double d;
double p[MAX_C];
int v[MAX_C];

int main(){
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++){
		scanf("%d %lf", &c, &d);
		for(int i = 0; i < c; i++)
			scanf("%lf %d", &p[i], &v[i]);
		double s = 0, e = 1e14;
		while(s + 1e-7 < e){
			double t = (s + e) / 2;
			double last = -1e14;
			bool can = true;
			for(int i = 0; i < c && can; i++){
				last = max(last, p[i] - t);
				last += (v[i] - 1) * d;
				if(last > p[i] + t)
					can = false;
				last += d;
			}
			if(can)
				e = t;
			else	s = t;
		}
		printf("Case #%d: %0.7lf\n", test, s);
	}
	return 0;
}
