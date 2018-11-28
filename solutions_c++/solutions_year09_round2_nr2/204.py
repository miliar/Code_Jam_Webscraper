#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int T, i;
string st, tt;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;
	for (i = 1; i <= T; i++){
		cin >> st;
		tt = st;
		if (!next_permutation(st.begin(), st.end())){
			st = "0" + tt;
			next_permutation(st.begin(), st.end());
		}
		cout << "Case #" << i << ": ";
		cout << st << endl;
	}
	return 0;
}