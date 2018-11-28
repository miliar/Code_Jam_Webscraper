#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <sstream>
#include <cmath>
#include <string>
#include <iostream>

using namespace std;

#define REP(i,n) for(int(i)=0;(i)<(n);(i)++)

typedef struct {
	int d, l;
	bool isP;
} vine;

vine v[10005];

int main() 
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int T;
	cin >> T;
	for (int TC = 1; TC <= T; TC++) {
		int n, D;
		cin >> n;
		for (int i = 0; i < n; i++) { cin >> v[i].d >> v[i].l; v[i].isP = false;}
		cin >> D;
		v[0].l = v[0].d;
		v[0].isP = true;
		bool isOk = false;
		for (int i = 0; i < n && !isOk; i++) {
			if (!v[i].isP) continue;
			for (int j = i+1; v[j].d <= v[i].d + v[i].l; j++) {
				if (!v[j].isP) { v[j].l = min(v[j].l, v[j].d-v[i].d); }
				v[j].isP = true;
			}
			if (v[i].d + v[i].l >= D) isOk = true;
		}
		printf("Case #%d: %s\n", TC, (isOk ? "YES" : "NO"));
	}

	return 0;
}