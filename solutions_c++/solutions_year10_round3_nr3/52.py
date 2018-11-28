#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
//download TTMath from http://www.ttmath.org/
//#include <ttmath/ttmath.h>

using namespace std;
//using namespace ttmath;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)

vector<size_t> cut(size_t M, size_t N, vector< vector<int> > & A)
{
	size_t K = (min)(M,N);
	vector<size_t> howmany(K+1,0);
	for(size_t k = K; k>0;--k){
		FOR(i,M-k+1) {
			FOR(j,N-k+1) {
				FOR(ii,k)
					FOR(jj,k)
						if(A[i+ii][j+jj] != 1)
							goto cannotcut;
cancut:				
				++howmany[k];
				FOR(ii,k)
					FOR(jj,k)
						A[i+ii][j+jj] = 0;
cannotcut:
				;
			}
		}
	}
	return howmany;

}

vector< pair<size_t, size_t> > solve_case(size_t M, size_t N, vector<string> rows)
{
	vector< vector<int> > A(M, vector<int>(N,0));
	vector< vector<int> > B(M, vector<int>(N,0));
	int inA = 8+2;
	int inB = 4+1;
	FOR(i,M) {
		FOR(j,N/4) {
			char c = rows[i][j];
			assert(('0' <= c && c <= '9') || ('A' <= c && c <= 'F'));
			int digit = (('0' <= c && c <= '9') ? c-'0' : c-'A'+10);
			assert(0 <= digit && digit < 16);
			FOR(k,4) {
				int bit = 1 << (3-k);
				if ((digit ^ inA) & bit)
					A[i][j*4+k] = 1;
				else
					B[i][j*4+k] = 1; //((digit ^ inB) & bit) != 0;
			}
		}
		swap(inA,inB);
	}
	vector<size_t> howmanyA = cut(M,N,A);
	vector<size_t> howmanyB = cut(M,N,B);
	size_t K = (min)(M,N);
	assert(howmanyA.size() == K+1 && howmanyB.size() == K+1);
	FOR(i,K+1)
		howmanyA[i] += howmanyB[i];
	vector< pair<size_t, size_t> > result;
	for(size_t k = K; k>0;--k){
		if (howmanyA[k] != 0)
			result.push_back(make_pair(k,howmanyA[k]));
	}
	return result;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	for (int t = 1; t <= TC_NCases; ++t)
	{
		size_t M, N;
		in >> M >> N;
		assert(N % 4 == 0);
		vector<string> rows(M);
		FOR(i,M) {
			in>>rows[i];
			assert(rows[i].size()*4 == N);
		}
		vector< pair<size_t, size_t> > result = solve_case(M,N,rows);
		out << "Case #" << t << ": " << result.size() << "\n";
		size_t check = 0;
		FOR(i,result.size()) {
			out << result[i].first << ' ' << result[i].second << "\n";
			check += result[i].first * result[i].first * result[i].second;
		}
		assert(check == M*N);
	}
}


int main()
{
	//ifstream in("C-sample.in");
	//ofstream out("C-sample.txt");

	//ifstream in("C-small-attempt0.in");
	//ofstream out("C-small-out.txt");

	ifstream in("C-large.in");
	ofstream out("C-large-out.txt");

	solve(in,out);

	return 0;
}