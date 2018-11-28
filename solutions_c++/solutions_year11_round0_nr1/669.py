#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <map>

using namespace std;

int N, T;

inline int myabs(int a) {return (a < 0 ? -a : a);}

inline int op(int &a, int b) {
	if (a < b) {a++;}
	else if (a > b) {a--;}
}

int main() {
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		cin >> N;
		vector< pair< int , int > > A, B;
		string str;
		int x;
		for(int i = 0 ; i < N ; i++) {
			cin >> str >> x;
			if (str[0] == 'B') {
				B.push_back(make_pair(x, i));
			}	else {
				A.push_back(make_pair(x, i));
			}
		}
		
		int ans = 0;
		int posA = 1;
		int posB = 1;
		while (1) {
			if (A.empty()) {
				ans += myabs(posB - B[0].first);
				for(int i = 1 ; i < (int)B.size() ; i++) {
					ans += myabs(B[i].first - B[i - 1].first);
				}
				ans += (int)B.size();
				break;
			}	else if (B.empty()) {
				ans += myabs(posA - A[0].first);
				for(int i = 1 ; i < (int)A.size() ; i++) {
					ans += myabs(A[i].first - A[i - 1].first);
				}
				ans += (int)A.size();
				break;
			}	else if (A[0].second < B[0].second) {
				while (posA != A[0].first) {
					op(posA, A[0].first);
					op(posB, B[0].first);
					ans++;
				}
				A.erase(A.begin());
				op(posB, B[0].first);
				ans++;
			}	else {
				while (posB != B[0].first) {
					op(posA, A[0].first);
					op(posB, B[0].first);
					ans++;
				}
				B.erase(B.begin());
				op(posA, A[0].first);
				ans++;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
