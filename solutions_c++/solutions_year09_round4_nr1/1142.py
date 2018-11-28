#include <algorithm>
#include <iostream>
#include <cstdio>
#include <stack>
#include <queue>
#include <vector>
#include <deque>
#include <functional>
#include <sstream>

using namespace std;

int get() { int x; cin >> x; return x; }

#define MAX 45

int n;
char row[MAX][MAX];

int works(int i,int j) {
	// does row i work up to col j?
	for(int k=j+1;k<n;k++)
		if(row[i][k]=='1')return 0;
	return 1;
}
void swap(int i) {
	for(int j=0;j<n;j++){
		int temp = row[i][j];
		row[i][j] = row[i+1][j];
		row[i+1][j] = temp;
	}
}

void gocase() {
	cin >> n;
	for(int i=0;i<n;i++)
		cin>>row[i];
	int ans=0;
	for(int i=0;i<n;i++) {
		for(int j=i;j<n;j++)
			if(works(j,i)) {
				for(int k=j-1;k>=i;k--) {
					swap(k);
					ans++;
				}
				break;
			}
	}
	cout << ans << endl;
}

int main() {
	int t = get();
	for(int i=1;i<=t;i++) {
		cout << "Case #" << i << ": ";
		gocase();
	}
	return 0;
}
