#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
using namespace std;
typedef vector<int> VI;

const int p10[10] = {1e0,1e1,1e2,1e3,1e4,1e5,1e6,1e7,1e8,1e9};

int a, b, l, r;


int main()
{
	int t; scanf("%d", &t);
	for (int ti=1; ti<=t; ++ti) {
		scanf("%d%d", &a, &b); l = log10(a); r = 0;
		
		for (int i=a; i<b; ++i) {
			int now = i;
			VI v;
			
			for (int j=0; j<l; ++j) {
				now = now/10 + now%10*p10[l];
				if (i<now && now<=b) v.PB(now);
			}
			
			sort(ALL(v));
			r += unique(ALL(v)) - v.begin();
		}
		
		printf("Case #%d: %d\n", ti, r);
	}
	
	return 0;
}
