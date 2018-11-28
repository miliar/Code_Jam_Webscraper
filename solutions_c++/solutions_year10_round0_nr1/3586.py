#include <iostream>

using namespace std;

typedef long long LL;

LL timeOn[35];
LL T, N, K, tc;

void input () {
	scanf ("%lld%lld", &N, &K);
}

void solve () {
}

void output () {
	if (K%(timeOn[N]+1)==timeOn[N]) {
		printf ("Case #%d: ON\n", tc);
	}
	else {
		printf ("Case #%d: OFF\n", tc);
	}
}

LL getTime (int num) {
	if (timeOn[num]!=-1) return timeOn[num];
	LL &ans = timeOn[num];
	ans = 0;
	if (num==1)
		ans = 1;
	else
		ans = getTime(num-1)*2+1;
	return ans;
}

int main () {
	freopen ("prog.in", "r", stdin);
	freopen ("prog.out", "w", stdout);
	scanf ("%lld", &T);
	memset (timeOn, -1, sizeof(timeOn));
	getTime(31);
	for (tc=1;tc<=T;tc++) {
		input ();
		solve ();
		output ();
	}
	return 0;
}
