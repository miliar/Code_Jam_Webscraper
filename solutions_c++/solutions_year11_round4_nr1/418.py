#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;


int main (int argc, char const *argv[])
{
	int tt;
	cin >> tt;
	for(int index = 1; index <= tt; index++) {
		int n, x, r;
		double t,s;
		int count = 0;
		int data[101] = {0};
		int st,ed,sp;
		int last = 0;
		cin >> x >> s >> r >> t >> n;
		for(int i = 0; i < n; i++) {
			cin >> st >> ed >> sp;
			data[0] += st-last;
			data[sp] += ed-st;
			last = ed;
		}
		data[0] += x-last;
		double ans = 0;
		for(int i = 0; i < 101; i++) {
			if (t > 0) {
				double speed = r+i;
				double oldspeed = s+i;
				double t1 = (double)data[i]/(double)speed;
				if (t1 > t) {
					double len = (double)data[i]-((double)speed*(double)t);
					t1 = t + len/(double)oldspeed;
					ans += t1;
					t = 0;
				} else {
					ans += t1;
					t -= t1;
				}
			} else {
				double speed = (double)s+i;
				ans +=  (double)data[i]/(double)speed;
			}
		}
		printf("Case #%d: %.6lf\n",index, ans);
	}
	return 0;
}