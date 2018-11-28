#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

#define REP(AA,BB) for(AA=0; AA<(BB); ++AA)
#define FOR(AA,BB,CC) for(AA=(BB); AA<(CC); ++AA)
#define FC(AA,BB) for(typeof(AA.begin()) BB=AA.begin(); BB!=AA.end(); ++BB)
#define SZ(AA) ((int)(AA.size()))
#define ALL(AA) (AA).begin(), (AA).end()
#define PB push_back
#define MP(AA,BB) make_pair((AA), (BB))

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;

int main(void) {
	int T, t, n, m;
	scanf("%d", &T);
	FOR(t,1,T+1) {
		scanf("%d%d", &n, &m);
		printf("Case #%d: %s\n", t, (m%(1<<n)==((1<<n)-1))?"ON":"OFF");
	}
	return 0;
}
