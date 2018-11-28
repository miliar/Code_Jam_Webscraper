#include <cstdio>
#include <vector>
FILE *in, *out;
const int MAX_C = 50, MAX_D = 50, MAX_N = 105;
int N, C, D, T;
struct Elem {
	Elem(int _a = -1, int _b = -1, int _c = -1) : a(_a), b(_b), c(_c) {}
	char a, b, c;
};
std::vector<Elem> join, oppose;
std::vector<char> l;

bool opposed(char a, char b) {
	for (int i = 0; i < oppose.size(); ++i)
		if (oppose[i].a == a && oppose[i].b == b || oppose[i].b == a && oppose[i].a == b) return true;
	return false;
}

char joined(char a, char b) {
	for (int i = 0; i < join.size(); ++i)
		if (join[i].a == a && join[i].b == b || join[i].b == a && join[i].a == b) return join[i].c;
	return 0;
}

void doJoin() {
	char ch;
	if (l.size() >= 2 && (ch = joined(l[l.size()-1], l[l.size()-2]))) {
		l.pop_back(); l.pop_back();
		l.push_back(ch);
	}
}

void doOppose() {
	for (int i = 0; i < l.size()-1; ++i)
		if (opposed(l[i], l[l.size()-1])) {
			l.clear();
			return;
		}
}


int main() {
	in = fopen("magicin.txt", "r"); out = fopen("magicout.txt", "w");
	fscanf(in, "%d", &T);
	char a, b, c;
	for (int t = 1; t <= T; ++t) {
		l.clear(); join.clear(); oppose.clear();
		fscanf(in, "%d ", &C);
		for (int i = 0; i < C; ++i) {
			fscanf(in, " %c %c %c ", &a, &b, &c);
			join.push_back(Elem(a, b, c));
		}
		fscanf(in, "%d ", &D);
		for (int i = 0; i < D; ++i) {
			fscanf(in, " %c %c ", &a, &b);
			oppose.push_back(Elem(a, b));
		}
		fscanf(in, "%d ", &N);
		for (int k = 0; k < N; ++k) {
			fscanf(in, " %c ", &a);
			l.push_back(a);
			doJoin();
			doOppose();
		}
		fprintf(out, "Case #%d: [", t);
		if (l.size()) {
			for (int i = 0; i < l.size()-1; ++i) 
				fprintf(out, "%c, ", l[i]);
				fprintf(out, "%c", l[l.size()-1]);
		}
		fprintf(out, "]\n");
	}
}