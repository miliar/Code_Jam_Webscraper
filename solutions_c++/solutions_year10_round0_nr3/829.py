#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<cctype>
#include<sstream>
#include<map>
#include<queue>
#include<vector>

using namespace std;

#define vi vector<int>
#define re return
#define co continue
#define sf scanf
#define pf printf
#define pb push_back

const int inf = 1000000000;

int R, K, N;
vi V;
vector<long long> VS;
int flag[1010];

int main() {
	int cases = 1;
	int t, i;
	for( sf("%d", &t); t--; ) {
		V.clear();
		VS.clear();
		cin >> R >> K >> N;
		for(i=0;i<N;i++) {
			int a;
			cin >> a;
			V.pb(a);
			flag[i] = 0;
		}

		long long euro = 0;
		int cur = 0;
		int cycle = 1;

		for(i=0;i<R;i++) {
			if( flag[cur] ) { // cycle e porse
				break;
			}
			else {
				flag[cur] = cycle++;
				long long sum = 0;
				int cnt = N;
				while(cnt--) {
					if( sum + V[cur] <= K ) {
						sum += V[cur];
						cur++; cur %= N;
					}
					else break;
				}
				VS.push_back(sum);
				euro += sum;
			}
		}

		printf("Case #%d: ", cases++);

		int rem = R - i;
		int cycle_length = cycle - flag[cur];
		long long sum = 0;
		int c = cycle_length;
		for(i=flag[cur]-1;c--;i++) {
			sum += VS[i];
		}

		euro += sum * (rem / cycle_length);
		rem = rem % cycle_length;
		for(i=flag[cur]-1;rem--;i++)
		 euro += VS[i];

		cout << euro << endl;


	}
	return 0;
}
