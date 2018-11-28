#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>
#define ll long long
using namespace std;
string d;
vector<int> l;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T, i, j;
	char str[128];
	ll k, x, xx;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		scanf("%s",str); d = str;
		x = 0;
		for (i = 0; i < d.size(); i++) {
			if (d[i] == '1')
				x += 1LL << (d.size()-1-i);
		}
		l.clear();
		for (i = 0; i < d.size(); i++) {
			if (d[i] == '?')
				l.push_back(d.size()-1-i);
		}
		for (i = 0; i < 1<<l.size(); i++) {
			xx = x;
			for (j = 0; j < l.size(); j++) {
				if (i&(1<<j)) {
					x += 1LL << l[j];
				}
			}
			k = (ll)sqrt(x+0.0);
			for (j = -10; j <= 10; j++) {
				if (0 <= k+j) {
					if ((k+j)*(k+j) == x) break;
				}
			}
			if (j <= 10) {
				for (j = 0; j < l.size(); j++) {
					if (i&(1<<j))
						d[d.size()-1-l[j]] = '1';
					else d[d.size()-1-l[j]] = '0';
				}
				break;
			}
			x = xx;
		}
		printf("%s\n",d.c_str());
	}
	return 0;
}