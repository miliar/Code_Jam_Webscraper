#include <fstream>
#include <cmath>
#include <vector>
#include <string>
#include <queue>
using namespace std;
ifstream in ("input.in");
ofstream out ("output.out");
void print (bool grid[][1000], int S, int Q) {
	for (int i=0; i<S; i++) {
		for (int j=0; j<Q; j++)
			out << grid[i][j];
		out << "\n";
	}
}
int main() {
	int C;
	in >> C;
	for (int z=0; z<C; z++) {
		int N, ans=0, a, b;
		in >> N;
		vector <pair <int, int> > p;
		for (int i=0; i<N; i++) {
			in >> a >> b;
			p.push_back (make_pair (a, b));
		}
		for (int i=0; i<N-1; i++)
			for (int j=i+1; j<N; j++)
				if ((p[i].first>p[j].first && p[i].second<p[j].second) || (p[i].first<p[j].first && p[i].second>p[j].second))
					ans++;
		out << "Case #" << z+1 << ": " << ans << "\n";
	}
	return 0;
}