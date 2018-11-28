#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const int MAXN = 10010;
int T, N;
int d[MAXN],l[MAXN];
int longest[MAXN];
int D;

int main(){
	cin>>T;
	for (int times = 0; times < T; ++times) {
		cin >> N;
		for (int i = 0; i < N; ++i){
			cin >> d[i] >> l[i];
		}
		cin >> D;
		bool found = false;
		longest[0] = d[0];
		if (d[0] + longest[0] >= D) {
			found = true;
		}
		if (!found) {
			for (int i = 1; i < N; ++i){
				longest[i] = 0;
				for (int j = 0; j < i; ++j) {
					if (longest[j] + d[j] >= d[i]) {
						int newL = d[i]-d[j];
						if (newL > l[i]) newL = l[i];
						if (newL > longest[i]) longest[i] = newL;
						if (longest[i] == l[i]) break;
					}
				}
				if (longest[i] + d[i] >= D) {
					found = true;
					break;
				}
			}
		}
		cout << "Case #" << times+1 << ": ";
		if (found) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
	return 0;
}