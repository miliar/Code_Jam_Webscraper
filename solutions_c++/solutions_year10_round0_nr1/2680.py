#include <cstdio>
#include <cmath>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
#include <set>
#include <map>

using namespace std;


typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;
typedef long long LL;

#define FOR(i, L, U)		for(int i=L; i<=U; i++)
#define EPS 1e-9

#define MAX 101

bool S[MAX];				// means state
bool P[MAX];				// means power state


int main()
{

	freopen("E:\\A-large.in", "r", stdin);
	freopen("E:\\output.txt", "w", stdout);

	int TC, tcase;
	int snap, N, K;
	int i, j, constant;
	bool isFound;
	int count=0;

	cin >> TC;

	FOR(tcase, 1, TC) {
		cin >> N >> K;

//		cout << tcase << " :" << N << " " << K << "\n";
/*
		memset(S, 0, sizeof(S));
		memset(P, 0, sizeof(P));

		P[1] = 1;

		FOR(snap, 1, K) {
			S[1] = S[1] == 0 ? 1 : 0;
			FOR(j, 2, N)  {
				if(P[j]) S[j] = (S[j] == 0) ? 1 : 0;
				if(S[j-1] && P[j-1]) P[j] = 1;
				else P[j] = 0;
			}
//		FOR(i, 1, N) 
//			cout << P[i] << " " << S[i] << "\n";
//		cout << "\n";
		}

*/
		constant = (1<<N);
		isFound = 0;

		for(i=1; (j = i*constant-1) <=K; i++) {
			if(j == K) {
				isFound = 1;
				break;
			}
		}

		cout << "Case #" << tcase << ": ";
		if(isFound)  cout << "ON\n";
		else cout << "OFF\n";

//		if(P[N] && S[N]) {
//			cout << "ON\n";
//			count++;
//		}
	}
//	cout << count;

	return 0;
}
