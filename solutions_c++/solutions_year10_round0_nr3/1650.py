#include <cstdio>
#include <vector>
#include <map>
typedef __int64 llong;
using namespace std;

int main() {
	int t, r, k, n, tmp;
	scanf("%d", &t);
	for (int kase = 0; kase < t; ++kase) {
		scanf("%d%d%d", &r, &k, &n);
		vector<llong> group;
		vector<llong> cnt;
		vector<llong> seq;
		vector<llong> accum;
		for (llong i = 0; i < n; ++i) {
			scanf("%d", &tmp);
			group.push_back(tmp);
			cnt.push_back(0);
			seq.push_back(-1);
		}
		llong ret = 0;
		llong st = 0;
		llong loopst = 0;
		llong looplen = 0, loopearn = 0;
		accum.push_back(0);
		for (llong i = 0; i < r; ++i) {
			llong cur = 0;
			llong next = st;
			do {
//			for ( ; cur < k && next < st; next = (next + 1) % group.size()) {
				llong num = group[next];
				if (cur + num <= k) {
					cur += num;
					ret += num;
				} else {
					break;
				}
				next = (next + 1) % group.size();
			} while (cur < k && next != st);
			seq[st] = i;
			cnt[st] = cur;
			accum.push_back(ret);
			//prllongf("cur %d st %d next %d seq %d\n", cur, st, next, seq[st]);
			
			if (seq[next] != -1) {
				loopst = seq[next];
				looplen = i - seq[next] + 1;
				loopearn = ret - accum[seq[next]];
				break;
			}
			st = next;
		}
		//prllongf("loopst %d looplen %d, loopearn %d\n", loopst, looplen, loopearn);
		llong rr = r-loopst;
		if (looplen)
			ret = (rr/looplen)*loopearn + accum[loopst + rr%looplen];
		else
			ret = accum[r];
		printf("Case #%d: %I64d\n", kase + 1, ret);
	}
	return 0;
}

