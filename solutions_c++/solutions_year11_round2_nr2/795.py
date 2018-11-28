#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#define mp make_pair
#define st first
#define nd second
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FORO(i,n) for(int i=1;i<=(n);i++)
#define FORS(i,a,n) for(int i=(a);i<(n);i++)
#define FORB(i,a,n) for(int i=(a);i>=(n);i--)
#define FORE(i,v) for(typeof((v).begin())i=(v).begin();i!=(v).end();i++)
#define INRANGE(a,b,c,d) ((a)>=0&&(b)>=0&&(a)<(c)&&(b)<(d))
#define pf printf
typedef long long ll;
using namespace std;


int C, D;
int P[500], V[500];

bool enough_time(double max_dist) {
	double tts = D * (V[0] - 1) / 2.0;
	if (tts > max_dist)
		return false;
	double can_go_left = max_dist - tts;
	double min_left = P[0] - can_go_left + tts + D;
	
	FORS(i, 1, C) {
		tts = D * (V[i] - 1) / 2.0;
		if (tts > max_dist)
			return false;
		double my_left = P[i] - tts;
		if (my_left < min_left) {
			my_left = min_left;
			if (abs(my_left - P[i]) > max_dist || abs(my_left + 2*tts - P[i]) > max_dist)
				return false;
		}
		else {
			can_go_left = min(max_dist - tts, my_left - min_left);
			my_left -= can_go_left;
		}
		min_left = my_left + 2*tts + D;
	}
	return true;
}

void tcase() {
	scanf("%d%d", &C, &D);
	FOR(i, C) {
		scanf("%d%d", &P[i], &V[i]);
	}
	double low = 0, high = 1e13;
	while (high - low > 1e-7) {
		double mid = (low + high) / 2;
		if (enough_time(mid))
			high = mid;
		else
			low = mid;
	}
	pf(" %.6f\n", high);
}

int main() {
	//freopen(".in", "r", stdin); freopen(".out", "w", stdout);
	int tn;
	scanf("%d", &tn);
	FOR(i, tn) {
		pf("Case #%d:", i+1);
		tcase();
	}
}


