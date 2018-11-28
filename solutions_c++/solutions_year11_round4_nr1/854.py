#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <ctime>

using namespace std;

typedef long long lint;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("Al.out", "w", stdout);

	int T, x, s, r, t, n, b, e, w, max; cin>>T;
	int length[201];
	double time, rt;
	for (int k=1; k<=T; k++) {
		memset(length, 0, sizeof(length));
		cin>>x>>s>>r>>t>>n;
		length[0]=x;
		max = 0;

		for (int i=0; i<n; i++) {
			cin>>b>>e>>w;
			length[w]+=(e-b);
			length[0]-=(e-b);
			if (max<w) max=w;
		}
		
		time = rt = 0;
		int ptr=0;
		//if (rt + 1.0*length[ptr]/(r) <= t) {
		//	time+=1.0*length[ptr]/(r);
		//	rt+=1.0*length[ptr]/(r);
		//}
		//else {
		//	time += ((t-rt) + 1.0*(length[ptr]-(t-rt)*(r))/(s));
		//	rt = t;
		//}
		//ptr++;
		while (rt<=t && ptr<=max) {
			if (rt + 1.0*length[ptr]/(r+ptr) <= t) {
				time+=1.0*length[ptr]/(r+ptr);
				rt+=1.0*length[ptr]/(r+ptr);
			}
			else {
				time += ((t-rt) + 1.0*(length[ptr]-(t-rt)*(r+ptr))/(s+ptr));
				rt = t;
			}
			ptr++;
		}
		while (ptr<=max) {
			time += 1.0*length[ptr]/(s+ptr);
			ptr++;
		}

		cout<<"Case #"<<k<<": ";
		printf("%.9f\n", time);
	}
}
