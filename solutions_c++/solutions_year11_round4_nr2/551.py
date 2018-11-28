#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <iomanip>
//download TTMath from http://www.ttmath.org/
//#include <ttmath/ttmath.h>

using namespace std;
//using namespace ttmath;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)

#undef min

bool centered(
	const vector<vector<__int64> > & ii,
	const vector<vector<__int64> > & jj,
	const vector<vector<__int64> > & m,
	int ia, int ib, int ja, int jb,
	const vector<vector<int> > & w,
	int D
	)
{
	__int64 M = m[ib][jb];
	if (ia > 0) M -= m[ia-1][jb];
	if (ja > 0) M -= m[ib][ja-1];
	if (ia > 0 && ja > 0) M += m[ia-1][ja-1];
	__int64 I = ii[ib][jb];
	if (ia > 0) I -= ii[ia-1][jb];
	if (ja > 0) I -= ii[ib][ja-1];
	if (ia > 0 && ja > 0) I += ii[ia-1][ja-1];
	__int64 J = jj[ib][jb];
	if (ia > 0) J -= jj[ia-1][jb];
	if (ja > 0) J -= jj[ib][ja-1];
	if (ia > 0 && ja > 0) J += jj[ia-1][ja-1];
	M -= (D+w[ib][jb]) + (D+w[ib][ja]) + (D+w[ia][jb]) + (D+w[ia][ja]);
	I -= (D+w[ib][jb])*(ib) + (D+w[ib][ja])*(ib) + (D+w[ia][jb])*(ia) + (D+w[ia][ja])*(ia);
	J -= (D+w[ib][jb])*(jb) + (D+w[ib][ja])*(ja) + (D+w[ia][jb])*(jb) + (D+w[ia][ja])*(ja);

	return (2*I == M*(ia+ib)) && (2*J == M*(ja+jb));
}

int solve_case(int R, int C, int D, const vector<vector<int> > & w)
{
	vector<vector<__int64> > ii(R, vector<__int64>(C));
	vector<vector<__int64> > jj(R, vector<__int64>(C));
	vector<vector<__int64> > m(R, vector<__int64>(C));
	FOR(i,R)
		FOR(j,C) {
			if (i == 0) {
				if (j == 0) {
					ii[i][j] = 0;
					jj[i][j] = 0;
					m[i][j] = D + w[i][j];
				} else {
					ii[i][j] = 0;
					jj[i][j] = jj[i][j-1] + j*(D + w[i][j]);
					m[i][j] = m[i][j-1] + (D + w[i][j]);
				}
			} else {
				if (j == 0) {
					ii[i][j] = ii[i-1][j] + i*(D + w[i][j]);
					jj[i][j] = 0;
					m[i][j] = m[i-1][j] + (D + w[i][j]);
				} else {
					ii[i][j] = ii[i-1][j] + i*(D + w[i][j]) + (ii[i][j-1] - ii[i-1][j-1]);
					jj[i][j] = jj[i][j-1] + j*(D + w[i][j]) + (jj[i-1][j] - jj[i-1][j-1]);
					m[i][j] = m[i-1][j] + (D + w[i][j]) + (m[i][j-1] - m[i-1][j-1]);
				}
			}
		}

	int K = min( R, C );
	assert(K >= 3 && K <= R && K <= C);
	for (; K >= 3; --K) {
		for (int i = 0; i+K-1 < R; ++i)
		for (int j = 0; j+K-1 < C; ++j)
		{
			if (centered(ii,jj,m,i,i+K-1,j,j+K-1,w,D))
				return K;
		}
	}
	return -1;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int R, C, D;
		in >> R >> C >> D;
		assert(R >= 3 && C >= 3);
		vector<vector<int> > w(R, vector<int>(C));
		char c;
		FOR(i,R)
			FOR(j,C) {
				in >> c;
				w[i][j] = c - '0';
			}
		int K = solve_case(R, C, D, w);
		if (K < 0)
			out << "Case #" << t << ": IMPOSSIBLE\n";
		else
			out << "Case #" << t << ": " << K << "\n";
	}
}


int main()
{
	//ifstream in("B-sample.in");
	//ofstream out("B-sample.txt");

	//ifstream in("B-small-attempt1.in");
	//ofstream out("B-small-out.txt");

	ifstream in("B-large.in");
	ofstream out("B-large-out.txt");

	solve(in,out);

	return 0;
}