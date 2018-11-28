#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int tn;
	scanf("%d", &tn);

	int n;
	char c[1000];
	int p[1000];
	for(int cc=1;cc<=tn;++cc) {
		scanf("%d", &n);
		for(int i=0;i<n;++i) {
			scanf(" %c %d", &c[i], &p[i]);
		}

		int ret = 0;

		int orange = 1;
		int blue = 1;

		for(int i=0;i<n;++i) {
			int next = -1;
			if( c[i] == 'O' ) {
				for(int j=i+1;j<n;++j) if( c[j] == 'B' ) {
					next = j;
					break;
				}
				while( orange != p[i] ) {
					++ret;
					if( orange < p[i] ) ++orange;
					else if( orange > p[i] ) --orange;
					if( next != -1 ) {
						if( blue < p[next] ) ++blue;
						else if( blue > p[next] ) --blue;
					}
				}
				++ret;
				if( next != -1 ) {
					if( blue < p[next] ) ++blue;
					else if( blue > p[next] ) --blue;
				}

			}
			else {
				for(int j=i+1;j<n;++j) if( c[j] == 'O' ) {
					next = j;
					break;
				}
				while( blue != p[i] ) {
					++ret;
					if( blue < p[i] ) ++blue;
					else if( blue > p[i] ) --blue;
					if( next != -1 ) {
						if( orange < p[next] ) ++orange;
						else if( orange > p[next] ) --orange;
					}
				}
				++ret;
				if( next != -1 ) {
					if( orange < p[next] ) ++orange;
					else if( orange > p[next] ) --orange;
				}
			}
		}
		printf("Case #%d: %d\n", cc, ret);

	}
}
