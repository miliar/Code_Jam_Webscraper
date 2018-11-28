#include <cstdio>
#include <utility>
#include <map>

using namespace std;
typedef pair<int, int> PII;

typedef long long ll;




int A1, A2, B1, B2;



map<PII, bool> memo;



bool f(int A, int B) {
	if(A <= 0 || B <= 0) return true;

	PII p = PII(A, B);
	map<PII, bool>::iterator it = memo.find(p);
	if(it != memo.end()) return it->second;;


	int mink = max(1, A/B-2);
	int maxk = mink+5;	
	for(int k = mink; k <= maxk; k++) if(!f(A-k*B, B)) return memo[p] = true;
	mink = max(1, B/A-2);
	maxk = mink+5;	
	for(int k = mink; k <= maxk; k++) if(!f(A, B-k*A)) return memo[p] = true;

	return memo[p] = false;

}

ll solve() {
	ll result = 0;
	scanf("%d %d %d %d", &A1, &A2, &B1, &B2);
	

	for(int i = A1; i <=  A2; i++) {
		for(int j = B1; j <=  B2; j++) {
			if(f(i, j)) result++;
		}
	}
	return result;
}


int main() {
	int t;
	memo.clear();
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) printf("Case #%d: %lld\n", i, solve()); 

}