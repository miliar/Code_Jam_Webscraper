/*
FROM: GCJ (Google Code Jam) Round 1B 2008
PROB: B Number Sets

LANG: GNU C++ (g++ (GCC) 4.3.1 20080612 (Red Hat 4.3.1-2))
OPT: -lm -O2
*/

#include <cstdio>
#include <vector>
#include <ext/hash_map>
#include <ext/hash_set>

namespace std {
	using namespace __gnu_cxx;
};

long long P;
long long X;
int LEN;

struct myhash {
	size_t operator () (const long long &x) const {
		return (x | x << 5) & ((unsigned)-1);
	}
};

std::vector <long long> sets;
std::vector <int> w;
std::hash_map <long long, int, myhash> set_pos;
std::vector <long long> cses;

void clear_sets() {
	sets.clear();
	w.clear();
//	sets.resize(0);
	set_pos.clear();
//	set_pos = new std::hash_map<long long, int>();
}

void new_session() {
	//printf("new session! %lld\n", X);
	cses.resize(0);
}

int top(int a) {
	for (; a != sets[a]; a = sets[a]) sets[a] = sets[sets[a]];
	return a;
}

void join(int a, int b) {
	//printf("join %d %d\n", a, b);
	a = top(a);
	b = top(b);
	if (a != b) {
		sets[a] = b;
		w[b] += w[a];
	}
}

void pour(int x) {
	x = top(x);
	++w[x];
}

void add_set(long long x) {
	std::hash_map<long long, int, myhash>::iterator it;
	if ((it = set_pos.find(x)) != set_pos.end()) {
		//do nothing
	} else {
		it = set_pos.insert(std::pair<long long, int>(x, sets.size())).first;
		sets.push_back(sets.size());
		w.push_back(0);
	}
	cses.push_back(it->second);
	if (cses.size() == 1) {
		//printf ("POUR!\n");
		pour(cses[0]);
	}
}

void close_session() {
	for (size_t i = 0; i < cses.size(); ++i)
		for (size_t j = i+1; j < cses.size(); ++j) {
			join(cses[i], cses[j]);
		}
}

int ans() {
	int grps = 0;
	int tot = 0;
	std::hash_set<int> ends;
	for (size_t i = 0; i < sets.size(); ++i) {
		int ii;
		for (ii = i; ii != sets[ii]; ii = sets[ii])
			sets[ii] = sets[sets[ii]];
		//printf ("%zu %d %d\n", i, ii, w[ii]);
		if (ends.insert(ii).second) {
			if (w[ii] > 1) {
				++grps;
				tot += w[ii];
			}
		}
	}
	//printf ("%d %d %d\n", grps, tot, LEN);
	return grps + LEN - tot;
}

void proc(long long p) {
	if (X % p != 0) return;
	//printf("proc %lld\n", p);

	if (p >= P) add_set(p);

	do {
		X /= p;
	} while (X % p == 0);
}



void factor() {
	proc(2);
	proc(3);
	long long x = 1;//6x0 + 1, 6x1 - 1, 6x1 + 1...
	for (;;) {
		x += 4;
		if (x * x > X) break;
		proc(x);

		x += 2;
		if (x * x > X) break;
		proc(x);
	}

	if (X > 1) proc(X);
}

int main() {
	int tc;
	scanf ("%d", &tc);

	for (int ctc = 1; ctc <= tc; ++ctc) {
		long long a, b;
		scanf ("%lld %lld %lld", &a, &b, &P);
		LEN = b - a + 1;

		clear_sets();
		for (long long i = a; i <= b; ++i) {
			X = i;
			new_session();
			factor();
			close_session();
		}
		printf("Case #%d: %d\n", ctc, ans());
	}

	return 0;
}
