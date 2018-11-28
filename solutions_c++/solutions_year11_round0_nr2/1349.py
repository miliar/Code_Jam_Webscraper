#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cassert>
#include <utility>
using namespace std;
#define VAR(i,v) __typeof((v))i=(v)
#define FOREACH(i,v) for(VAR(i,(v).begin());i!=(v).end();i++)

int main() {
	int _T; scanf("%d",&_T);
	for(int _iT=1; _iT<=_T; _iT++) {
		int res[256][256];
		memset(res, 0, sizeof(res));
		int rescl[256][256];
		memset(rescl, 0, sizeof(res));

		int n;

		scanf("%d", &n);
		for(int i=0; i<n; i++) {
			unsigned char buf[10];
			scanf("%s", buf);
			assert(strlen((char*)buf)==3);
			res[buf[0]][buf[1]] = buf[2];
			res[buf[1]][buf[0]] = buf[2];
		}
		scanf("%d", &n);
		for(int i=0; i<n; i++) {
			unsigned char buf[10];
			scanf("%s", buf);
			assert(strlen((char*)buf)==2);
			rescl[buf[0]][buf[1]] = 1;
			rescl[buf[1]][buf[0]] = 1;
		}

		unsigned char sp[1000];
		scanf("%d", &n);
		scanf("%s", sp);
		assert((int)strlen((char*)sp) == n);

		vector<unsigned char> result;
		for(int i=0; i<n; i++) {
			result.push_back(sp[i]);
			int rs = (int)result.size();
			if(rs<2)
				continue;
			int t = res[result[rs-2]][result[rs-1]];
			if(t>0) {
				result.pop_back();
				result.pop_back();
				result.push_back(t);
			} else {
				for(int j=0; j<rs; j++) {
					if(rescl[result[j]][result[rs-1]]) {
						result.clear();
						break;
					}
				}
			}
		}
		printf("Case #%d: [", _iT);
		for(int i=0; i<(int)result.size(); i++) {
			printf( "%s%c", (i>0)?", ":"", result[i] );
		}
		printf("]\n");
	}

	return 0;
}
