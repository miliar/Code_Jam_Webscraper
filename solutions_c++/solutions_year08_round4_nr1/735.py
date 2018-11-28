#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 1000000000;

int n;

bool r;

bool g[10000];
bool c[10000];

bool v[10000];
bool leaf[10000];

void input() {
	cin >> n >> r;
	for(int i=0;i<(n-1)/2;i++) {
		cin >> g[i] >> c[i];
		leaf[i] = false;
	}
	for(int i=(n-1)/2;i<n;i++) {
		cin >> v[i];		
		leaf[i] = true;
	}	
}

int table[10000][2];

int gettable(int i, int j) {
	int& item = table[i][j];
	if(item == -1) {
		int left = i*2+1;
		int right = i*2+2;
		if(leaf[i]) {
			if(v[i] == j)
				item = 0;
			else
				item = MAX;
		} else {
			if(g[i]) { // and gate
				if(j==0) {
					item = min(gettable(left,0), gettable(right, 0));
					if(c[i])
						item = min(item , 1 + gettable(left, 0) + gettable(right, 0));
				} else {
					item = gettable(left, 1) + gettable(right, 1);
					if(c[i])
						item = min(item, 1 + min(gettable(left, 1), gettable(right, 1)));
				}
			} else { // or gate
				if(j==0) {
					item = gettable(left,0) + gettable(right, 0);
					if(c[i])
						item = min(item, 1 + min(gettable(left, 0), gettable(right, 0)));
				} else {
					item = min(gettable(left, 1), gettable(right, 1));
					if(c[i])
						item = min(item, 1 + gettable(left, 1) + gettable(right, 1));
				}
			}			
		}		
		
	}
	return item;
}

int main() {
	int casen;
	cin >> casen;
	for(int casei=1;casei<=casen;casei++) {
		input();
		
		for(int i=0;i<n;i++)
			for(int j=0;j<2;j++)
				table[i][j] = -1;
		
		int res = gettable(0, r);
		
		cout << "Case #" << casei << ": ";
		if(res >= MAX)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;				
	}
	return 0;
}
