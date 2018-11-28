#include <cstdio>
#include <vector>
using namespace std;

vector<int> v[255], vi, vc;
int cur_vi;
struct vstruct{
	int loc, target;
} vo, vb;

int doing(vstruct &vv, char vnow, int can_push) {
	if (vnow == vc[cur_vi] && vv.loc == v[vnow][vv.target]) {
		if (can_push == 0) return 0;
		cur_vi++;
		vv.target++;
		return 0;
	}
	if (vv.target >= v[vnow].size()) return 1;
	if (vv.loc < v[vnow][vv.target]) {
		vv.loc++;
	}
	if (vv.loc > v[vnow][vv.target]) {
		vv.loc--;
	}
	return 1;
}

int scan() {
	int ret = 0;
	while (cur_vi < vi.size()) {
		ret++;
		if (vc[cur_vi] == 'O') {
			doing(vo, 'O', doing(vb, 'B', 1));
		}
		else {
			doing(vb, 'B', doing(vo, 'O', 1));
		}
	}
	return ret;
}

int main() {
	int t, n, a;
	char s[10];
	freopen("trust.txt", "r", stdin);
	freopen("trust.out", "w", stdout);
	scanf("%d", &t);
	for (int t1=0; t1<t; t1++) {
		scanf("%d", &n);
		v['O'].clear();
		v['B'].clear();
		vi.clear();
		vc.clear();
		vo.loc = vb.loc = 1;
		vo.target = vb.target = 0;
		cur_vi = 0;
		for (int i=0; i<n; i++) {
			scanf("%s %d", s, &a);
			v[s[0]].push_back(a);
			vi.push_back(a);
			vc.push_back(s[0]);
		}
		printf("Case #%d: %d\n", t1+1, scan());
	}
	return 0;
}
