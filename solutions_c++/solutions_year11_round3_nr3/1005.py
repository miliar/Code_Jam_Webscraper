#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <iterator>
#include <map>
#include <list>
#include <string>
#include <sstream>
using namespace std;

#define ALL(X) X.begin(), X.end()
int p[10000];

int main()
{
	if( freopen("C-large.in", "rt", stdin) ) {
		freopen("C-large.out", "wt", stdout);
	} else 	if( freopen("C-small.in", "rt", stdin) ) {
		freopen("C-small.out", "wt", stdout);
	} else ( freopen("test.txt", "rt", stdin) );

	int T;
	cin >> T;

	for(int case_num = 1; case_num <= T; ++case_num)
	{
		int N, L, H;
		cin >> N >> L >> H ;
		for(int i = 0; i < N; ++i)
		{
			cin >> p[i];
		}
		int f = L;
		while(f <= H) {
			int i = 0;
			for(; i < N; ++i) {
				if(f > p[i]) {
					if( (f/p[i]) * p[i] != f) break;
				} else {
					if( (p[i]/f) * f != p[i]) break;
				}
			}
			if(i == N) break;
			++f;
		}
		cout << "Case #" << case_num << ": ";
		if(f <= H) cout << f << endl;
		else cout << "NO" << endl;
	}
	return 0;
}