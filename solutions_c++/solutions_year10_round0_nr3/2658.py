using namespace std;

#include <iostream>
#include <vector>


//#define TEST
#define SMALL
//#define LARGE
int main(void) {
#ifdef TEST
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif

#ifdef SMALL
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
#endif

#ifdef LARGE
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
#endif

	unsigned int T;
	unsigned int R, k, N, g;
	int last;
	vector<int> groups;
	unsigned int money;
	int free;
	bool full = false;
	cin >> T;

	for(int i=0; i< T; i++) {
		cin >> R;
		cin >> k;
		cin >> N;
		money = 0;
		last = -1;
		
		for(int j=0; j<N; j++) {
			cin >> g;
			groups.push_back(g);
		}
		for(int j=0; j<R; j++) {	
			free = k;
			if(groups[(last+1)%N]>k) {
				money += 0;
			} else {
				full = false;
				free -= groups[(last+1)%N];
				last = (last+1)%N;
				int l = last;
				while(!full) {
					if(((free - groups[(l+1)%N]) >= 0) && (((l+1)%N)!=last)) {
						free -= groups[(l+1)%N];
						l = (l+1)%N;
					} else {
						full = true;
					}
				};
				last = l;
				money = money + (k-free);
			}
		}
		printf("Case #%d: %d\n", (i+1), money);
		groups.clear();
	}

	return 0;
}
