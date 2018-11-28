
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <queue>
#include <set>
#include <cstring>
#include <sstream>
#include <cassert>
#include <map>
#include <stack>

#define FOR(I,A,B) for(int I=(A);I<(B);I++)
#define REP(I,N) FOR(I,0,N)
#define ALL(A) (A).begin(),(A).end()

#define SQR(x) ((x)*(x))
#define PB(x) push_back(x)

#define PI (acos(-1.0))

using namespace std;

typedef vector<int> VI;
typedef vector< vector<int> > VVI;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int testcase;
	cin>> testcase;
	for(int tc=1;tc<=testcase;tc++) {
		int N;
		cin >> N;
		vector<string> schedule(N);
		REP(i,N) cin >> schedule[i];
		vector<double> WP(N);
		REP(i,N) {
			int count = 0;
			REP(j,N) {
				if(schedule[i][j] == '.')continue;
				count++;
				WP[i] += schedule[i][j] - '0';
			}
			WP[i] /= count;
		}
		vector<double> OWP(N);
		REP(i,N) {
			int count = 0;
			REP(j,N) {
				if(schedule[i][j] == '.')continue;
				count++;
				int count2=0;
				double sum = 0;
				REP(k,N) {
					if(i == k) continue;
					if(schedule[j][k] == '.') continue;
					count2++;
					sum += schedule[j][k] - '0';
				}
				OWP[i] += sum / count2;
			}
			OWP[i] /= count;
		}
		vector<double> OOWP(N);
		REP(i,N) {
			int count = 0;
			REP(j,N) {
				if(schedule[i][j] == '.')continue;
				count++;
				OOWP[i] += OWP[j];
			}
			OOWP[i] /= count;
		}
		printf("Case #%d:\n",tc);
		REP(i,N) cout << 0.25 * WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]<<endl;
//		REP(i,N) cout << WP[i] << " " << OWP[i]<< " " << OOWP[i]<<endl;
		

	}
}
