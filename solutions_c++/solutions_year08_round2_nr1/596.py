#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define forint(i, a, b) for (int i=(int)(a); i<(int)(b); i++)


#define v1i vector< int >
#define v2i vector< vector< int > >
#define v3i vector< vector< vector< int > > >

#define v1d vector< double >
#define v2d vector< vector< double > >
#define v3d vector< vector< vector< double > > >


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

using namespace std;

int main() {

	int N;

	cin >> N;

	forint(i,0,N) {
		int n;
		long long A, B, C, D, x0, y0, M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

		vector< pair<long long, long long> >* pts = new vector< pair<long long, long long> >(n);

		(*pts)[0].first = x0;
		(*pts)[0].second = y0;

		forint(j,1,n) {
			(*pts)[j].first = ((*pts)[j-1].first * A + B) % M;
			(*pts)[j].second = ((*pts)[j-1].second * C + D) % M;
		}

		long long total = 0;
		forint(a,0,n) {
			forint(b,a+1,n) {
				forint(c,b+1,n) {
					if (((*pts)[a].first + (*pts)[b].first + (*pts)[c].first) % 3 == 0 &&
						((*pts)[a].second + (*pts)[b].second + (*pts)[c].second) % 3 == 0) 
						total++;
				}
			}
		}


		cout << "Case #" << i+1 << ": " << total << endl;
		
		delete pts;

	}

	return 0;
}