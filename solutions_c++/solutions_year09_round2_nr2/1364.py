#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <set>
#include <numeric>

using namespace std;

#define SZ(A) (A).size()
#define ALL(A) (A).begin(), (A).end()
#define SORT(A) sort(ALL(A))
#define REP(I,N) for(int I=0, I<N ; I++)
#define PB push_back

typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<long long> vl;
typedef vector<vl> vvl;

int main(void) {

	int T;
	cin >> T;
	for(int t=1 ; t<=T ; t++){
		int N;
		cin >> N;
		int n = N;

		vector<int> cnt (10, 0);
		while(N){ cnt[N%10]++; N/= 10; }

		vector<int> cnt1;
		bool es = false;

		int i;
		for( i=n+1 ; !es ; i++){
			int ii = i;
			cnt1 = cnt;
			while(ii){
				cnt1[ii%10]--;
				ii /= 10;
			}
			cnt1[0] = 0;
			es = count(ALL(cnt1), 0) == 10;
		}

		cout <<"Case #"<<t<<": " << i-1 << endl;
	}
	return 0;
}
