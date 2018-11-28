#include <iostream>
using namespace std;

#define REP(i,n) for(int i = 0,_n = (n);i < _n;++i)
typedef long long LL;

const int NMAX = 1000;
int group[NMAX], zysk[NMAX], nast[NMAX], first[NMAX];

LL parthead[NMAX+10], partcycle[NMAX+10];

inline int next(int i,int N) {
	return i<N-1 ? i+1 : 0;
}

void testcase(int t) {
	int R,k,N;
	cin >> R >> k >> N;
	REP(i,N) cin >> group[i];
	fill_n(zysk,N,0);
	REP(i,N) {
		int cur = i;
		do {
			zysk[i] += group[cur];
			cur = next(cur,N);
		} while (cur != i && zysk[i]+group[cur] <= k);
		nast[i] = cur;
	}
//REP(i,N) cerr << "group=" << group[i] << " zysk=" << zysk[i]<< " nast=" << nast[i] << endl;
	fill_n(first,N,0);
	int cur = 0, i = 0;
	while (first[cur] == 0) {
		first[cur] = ++i;
		cur = nast[cur];
	}
//REP(i,N) cerr << first[i] << " "; cerr << endl;	
	// dlugosc glowy - first[cur]
	int nhead = first[cur]-1;
//cerr << "nhead =" << nhead << endl;
	parthead[0] = 0;
	for(cur = 0,i = 0;i < nhead;cur = nast[cur],++i)
		parthead[i+1] = parthead[i] + zysk[cur];
//REP(i,nhead) cerr << parthead[i] << " "; cerr << endl;
	int ncycle = 0;
	partcycle[0] = 0;
	do {
		partcycle[ncycle+1] = partcycle[ncycle] + zysk[cur];
		++ncycle;
		cur = nast[cur];
	} while (first[cur] != nhead+1);

	LL res = 0;
	if (R < nhead) {
		res = parthead[R];
		R = 0;
	} else {
		res = parthead[nhead];
		R -= nhead;
	}
	res += R/ncycle * partcycle[ncycle];
	R %= ncycle;
	res += partcycle[R];
	
	cout << "Case #" << t << ": " << res << "\n";
}

int main() {
	int T;
	cin >> T;
	for(int i = 1;i <= T;++i)
		testcase(i);
}
