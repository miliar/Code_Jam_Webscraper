#include <iostream>
#include <string>

#define rep(i, n) for (int i=0; i<(n); i++)

using namespace std;

int main(void) {
	int N, S, Q;
	int count, used;
	int pos;
	string tmp;
	string names[1000];
	int flag[1000];

	cin >> N;
	rep(k, N) {
		count = 0;
		used = 0;
		cin >> S;
		getline(cin, tmp);
		rep(i, S) {
			getline(cin, names[i]);
			flag[i] = 0;
		}
		cin >> Q;
		getline(cin, tmp);
		rep(i, Q) {
			getline(cin, tmp);
			for(pos=0; pos < S; pos++) {
				if(names[pos] == tmp) break;
			}
			assert(pos < S);
			if (flag[pos] == 0) {
				flag[pos] = 1;
				used++;
				if (used == S) {
					count++;
					used = 1;
					rep(j, S) flag[j] = 0;
					flag[pos] = 1;
				}
			}
		}
		cout << "Case #" << (k+1) << ": " << count << endl;
	}

}
