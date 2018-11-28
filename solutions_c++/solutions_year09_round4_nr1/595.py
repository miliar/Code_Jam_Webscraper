#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <string>
#include <list>
#include <map>
#include <cmath>

using namespace std;

int N;
int t[50];

void solve() {

	cin >> N;
	for(int i = 0; i < N; i++) {
		string s;
		cin >> s;
		t[i] = 0;
		for(int j = 0; j < N; j++) if(s[j] == '1') t[i]=j;
	}


	int result = 0;

	for(int i = 0; i < N; i++) {

		int j = i;
		while(t[j] > i) j++;
		if(i == j) continue;
		for(j--; j >= i; j--) {
			swap(t[j], t[j+1]);		
			result++;
		}
	}



	cout << result << endl;

	

}


int main() {		
	int C;
	cin >> C;	
	for(int i = 1; i <= C; i++) {
		cout << "Case #" << i << ": ";
		solve();	
	}
}