#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define EPS 1e-8

int T;

int q[10005];

bool check(int val){

}

int main(){
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	cin >> T;
	for (int I=0; I<T; I++){
		cout << "Case #" << I+1 << ": ";
		memset(q, 0, sizeof q);
		int N;
		cin >> N;
		if (!N){
			cout << 0 << endl;
			continue;
		}
		for (int i=0; i<N; i++){
			int tec;
			cin >> tec;
			q[tec]++;
		}
		int mn = 1<<30, done = 0;
		for (int i=0; done < N; i++){
			int cur = 0;
			for (int j=0; j<=10000; j++){
				if (cur){
					if (q[j] > q[j-1]){
						cur++;
						q[j]--;
						done++;
					} else {
						break;
					}
				} else {
					if (q[j] > 0){
						cur = 1;
						q[j]--;
						done++;
					}
				}
			}
			mn = min(mn, cur);
		}
		cout << mn << endl;
	}
	return 0;
}