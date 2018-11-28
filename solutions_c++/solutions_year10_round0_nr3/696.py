#include <fstream>
#include <iostream>
#include <deque>
using namespace std;

#define INPUTFILE "D:\\A-small.in"
#define OUTPUTFILE "D:\\A-small.out"

long long g[1001];
int nxt[1001];
long long visited_profit[1001];
long long visited_number[1001];
long long money[1001];

int main(void) {
	ifstream fi;
	fi.open(INPUTFILE);
	ofstream fo;
	fo.open(OUTPUTFILE);
	int T;
	fi >> T;
	long long R, N, K;
	
	for (int i = 1; i <= T; i++) {
		
		fi >> R >> K >> N;
		
		for (int j = 0; j < N; j++)
		{ fi >> g[j]; visited_profit[j] = -1; }
		
		for (int j = 0; j < N; j++) {
			long long sum = 0;
			int m = j;
			while (1) {
				if (sum + g[m] > K) {
					nxt[j] = m;
					money[j] = sum;
					break;
				}
				else {
					sum += g[m++];
					if (m == N)
						m = 0;
					if (m == j) {
						nxt[j] = j;
						money[j] = sum;
						break;
					}

				}
			}
		}

		int current = 0;
		long long profit = 0;
		int iteration = 0;
		while ((visited_profit[current] == -1) && (R > 0)) {
				visited_profit[current] = profit;
				profit += money[current];
				visited_number[current] = iteration++;
				current = nxt[current];
				R--;
		}
		if (R > 0) {
			long long period_length = iteration - visited_number[current];
			long long period_profit = profit - visited_profit[current];
			long long num = R / period_length;
			profit += num * period_profit;
			R %= period_length;
		}
		while (R > 0) {
				profit += money[current];
				current = nxt[current];
				R--;
		}
		fo << "Case #" << i << ": " << profit << endl;
	}
	
	fi.close();
	fo.close();
}
