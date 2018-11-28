#include <fstream>
#include <cstdio>

using namespace std;

ifstream in("test.txt");
ofstream out("answer.txt");

int a[10000];
int d[10000];
int l[10000];

void doit(int t) {
	int N;
	in >> N;
	for (int i = 0; i < N; i++) {
		in >> d[i] >> l[i];
		a[i] = 0;
	}
	int target;
	in >> target;
	out << "Case #" << t << ": ";
	bool yes = false;
	a[0] = d[0];
	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			if (d[i] + a[i] >= d[j]) {
				int best = d[j] - d[i];
				if (best > l[j])
					best = l[j];
				if (best > a[j])
					a[j] = best;
			}
		}
	}
	for (int i = 0; i < N; i++) {
		if (d[i] + a[i] >= target)
			yes = true;
	}
	if (yes)
		out << "YES" << endl;
	else
		out << "NO" << endl;
}

int main() {
	int T;
	in >> T;
	for (int t = 1; t <= T; t++)
		doit(t);
	return 0;
}