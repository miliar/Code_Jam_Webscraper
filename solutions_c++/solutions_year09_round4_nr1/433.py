#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <stack>
#include <utility>
#include <cstdlib>
#include <sstream>
#include <fcntl.h>

using namespace std;

const int INF=0x7fffffff;
const int M = 50;
char tab[M][M];
int num[M];

int main(int argc,char**argv) {
	int cs;
	scanf("%d",&cs);
	for (int csi=1; csi<=cs; ++csi) {
		int n;
		scanf("%d",&n);
		for (int i=0; i<n; ++i) {
			scanf("%s",tab[i]);
		}
		for (int i=0; i<n; ++i) {
			num[i] = 0;
			for (int j=0; j<n; ++j) if (tab[i][j] == '1') num[i] = j;
		}
		int ret = 0;
		for (int i=0; i<n; ++i) {
			for (int j=0; j<n; ++j) {
				if (num[j] > i) ++ret;
				else if (num[j] >= 0) {
					num[j] = -1;
					break;
				}
			}
		}

		printf("Case #%d: %d\n",csi,ret );




	}
	return 0;
}
