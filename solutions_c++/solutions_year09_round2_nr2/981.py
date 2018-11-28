#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int N;
	cin >> N;
	string tmp;
	string orig;
	for (int r = 0; r < N; r++){	
		cin >> tmp;
		orig = tmp;
		if (!next_permutation(tmp.begin(), tmp.end())) {
			tmp.insert(0, "0");
			int p;
			for (p = 0; p < tmp.size(); p++) if (tmp[p] != '0') break;
			char copy[2] = {tmp[p], '\0'};
			tmp.erase(tmp.begin()+p);
			tmp.insert(0, copy);
		}
		cout << "Case #" << r+1 << ": " << tmp << endl;
	}
	return 0;
}