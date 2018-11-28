#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
using namespace std;
const int maxn = 1001;
struct node
{
	int k, x;
};

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int p, q;
	int n;
	node a[maxn];
	int textnum, T = 0, tmp;
	string st;
	cin >> textnum;
	while (textnum--) {
		++T;
		cout << "Case #" << T << ": ";

		cin >> n;
		for (int i = 0; i != n; ++i) {
			cin >> st;
			if (st=="B") a[i].k = 0; else a[i].k = 1; 
			cin >> a[i].x;
		}
		long ans = 0;
		p = 1; q = 1;
		for (int i = 0; i != n; ++i) 
			if (a[i].k==0) {
				tmp = abs(a[i].x-p)+1;
				ans += tmp;
				p = a[i].x;
				for (int j = i+1; j != n; ++j) 
					if (a[j].k==1) {
						if (tmp>=abs(a[j].x-q)) q = a[j].x;
						else {
							if (a[j].x>q) q += tmp;
							else q -= tmp;
						}
						break;
					}
			} else {
				tmp = abs(a[i].x-q)+1;
				ans += tmp;
				q = a[i].x;
				for (int j = i+1; j != n; ++j) 
				if (a[j].k==0) {
					if (tmp>=abs(a[j].x-p)) p = a[j].x;
					else {
						if (a[j].x>p) p += tmp;
						else p -= tmp;
					}
					break;
				}
			}
		cout << ans << endl;
	}
	return 0;
}