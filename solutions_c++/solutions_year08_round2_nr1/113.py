#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(int a=0;a<(b);++a)
#define FOR(a,c,b) for(int a=c;a<(b);++a)


int main()
{
	//ifstream fin("A-small.in");
	//ofstream fout("A-small2.out");
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	long long N, n, a, b, c, d, x0, y0, m;

	fin >> N;

	for (int tc = 1; tc <= N; ++tc)
	{
		fin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;

		vector <pair<long long,long long> > t;

		long long X = x0, Y = y0;
		t.push_back(make_pair(X, Y));
		for (int i = 1; i <= n-1; ++i) {
			X = (a * X + b) % m;
			Y = (c * Y + d) % m;
			t.push_back(make_pair(X, Y));
		}

		long long q[3][3];
		long long cnt = 0;
		memset(q, 0, sizeof(q));
		REP(i,n) q[t[i].first%3][t[i].second%3]++;

		REP(i,9) FOR(j,i,9) FOR(k,j,9) {
			int a = i/3+j/3+k/3, b=i%3+j%3+k%3;
			if (a%3 || b%3) continue;
			long long z;
			if (i == j && j == k) {
				z = (q[i/3][i%3]*(q[j/3][j%3]-1)*(q[k/3][k%3]-2))/6;
			} else if (i == j) {
				z = (q[i/3][i%3]*(q[j/3][j%3]-1)*(q[k/3][k%3]))/2;
			} else if (j == k) {
				z = (q[i/3][i%3]*(q[j/3][j%3]-1)*(q[k/3][k%3]))/2;
			} else if (i == k) {
				z = (q[i/3][i%3]*(q[j/3][j%3])*(q[k/3][k%3]-1))/2;
			} else {
				z = q[i/3][i%3]*q[j/3][j%3]*q[k/3][k%3];
			}
			cnt += z;
		}

		fout <<"Case #"<<tc<<": "<<cnt<<endl;

	}



	fin.close();
	fout.close();

	return 0;
}

