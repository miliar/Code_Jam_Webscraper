#include <cstdio>
#include <set>
using namespace std;

typedef multiset<int>::iterator ITR;
typedef long long int64;
const int N = 1024;
int64 cnt[N];
int P, K, L;

int main(){
	int nCase;
	scanf("%d", &nCase);
	for(int ca = 1; ca <= nCase; ++ca){
		int64 ans = 0;
		int val;
		scanf("%d %d %d", &P, &K, &L);
		multiset<int> s;
		for(int i = 0; i < L; ++i){
			scanf("%d", &val);
			s.insert(-val);
		}
		memset(cnt, 0, sizeof(cnt));
		for(ITR itr = s.begin(); itr != s.end(); ++itr){
			int mini = 0;
			for(int i = 1; i < K; ++i)
				if(cnt[i] < cnt[mini]) mini = i;
			cnt[mini]++;
			//printf("mini = %d, cnt = %d\n", mini, cnt[mini]);
			//printf("%d used %d times\n", (-*itr), cnt[mini]);
			ans += cnt[mini] * (-(*itr));
		}
		printf("Case #%d: %I64d\n", ca, ans);
	}
	return 0;
}
