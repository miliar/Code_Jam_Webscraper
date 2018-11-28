#include <cstdio>
#include <cstring>
#include <algorithm>

#define REP(AA,BB) for(AA=0; AA<BB; ++AA)
#define FOR(AA,BB,CC) for(AA=BB; AA<CC; ++AA)
#define FC(AA,BB) for(typeof(AA.begin()) BB=AA.begin(); BB!=AA.end(); ++BB)

using namespace std;

char a[50][50]; int N;

int last(int x) {
	int i;
	for(i=N-1; i>=0; --i) {
		if(a[x][i]==1)
			return i;
	}
	return -1;
}

void sw(int x, int y) {
	int i;
	REP(i,N)
		swap(a[x][i],a[y][i]);
}

int main(void) {
	int t, T, n, m, i, j, k, res=0;
	scanf("%d", &T);
	REP(t,T) {
		scanf("%d", &N); res=0;
		REP(i,N)
			scanf("%s", a[i]);
		REP(i,N) {
			REP(j,N)
				a[i][j]-='0';
		}
		j=0;
		REP(i,N) {
			FOR(k,j,N) {
				if(last(k)<=i)
					break;
			}
			for(; k>i; --k) {
				sw(k,k-1);
				++res;
			}
			++j;
		}
		printf("Case #%d: %d\n", t+1, res);
	}
	return 0;
}
		
