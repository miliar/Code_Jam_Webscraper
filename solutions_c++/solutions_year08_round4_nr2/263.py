#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long LL;

LL absll(LL x) {
	if (x<0) return -x;
	return x;
}
LL triangle_area(LL x1, LL y1, LL x2, LL y2, LL x3, LL y3) {
	return absll((x3-x1)*(y2-y1) - (x2-x1)*(y3-y1));
}

int main() {
	int NCASES;
	cin >> NCASES;
	for (int z=1;z<=NCASES;++z) {
		LL N,M,A;
		cin >> N >> M >> A;
		bool ok=0;
		printf("Case #%d: ",z);
		for (LL x2=0;x2<=N && !ok;++x2) {
			for (LL y2=0;y2<=M && !ok;++y2) {
				if (x2==0 && y2==0) continue;
				for (LL x3=0;x3<=N && !ok;++x3) {
					for (LL y3=0;y3<=M && !ok;++y3) {
						if (x3==0 && y3==0) continue;
						if (x2==x3 && y2==y3) continue;
						if (absll(x3*y2 - x2*y3)==A) {
							ok=1;
							printf("0 0 %lld %lld %lld %lld\n", x2,y2,x3,y3);
						}
					}
				}
			}
		}
		if (!ok) printf("IMPOSSIBLE\n");
	}
}
