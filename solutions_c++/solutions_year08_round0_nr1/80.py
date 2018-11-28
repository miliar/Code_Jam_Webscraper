#include <iostream>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

int sn, qn;
int q[1000];

void input() {
	cin >> sn;
	string line;
	getline(cin, line);
	map<string, int> s2i;
	for(int i=0;i<sn;i++) {
		getline(cin, line);
		int index = s2i.size();
		s2i[line] = index;
	}
	
	cin >> qn;
	getline(cin, line);	
	for(int i=0;i<qn;i++) {
		getline(cin, line);
		q[i] = s2i[line];
	}
}

const int MAX = 1000000000;

int table[100][1001];
int gettable(int i, int j) {
	int& item = table[i][j];
	if(item == -1) {
		if(j == qn)
			item = 0;
		else {
			item = MAX;
			for(int k=0;k<sn;k++)
				if(k != q[j]) {
					if(k == i)
						item = min(item, gettable(k, j+1));
					else
						item = min(item, gettable(k, j+1)+1);
				}
		}
	}
	return item;	
}

int main() {
	int casen;
	cin >> casen;
	for(int casei=0;casei<casen;casei++) {
		input();
		int r = MAX;
		for(int i=0;i<sn;i++)
			for(int j=0;j<=qn;j++)
				table[i][j] = -1;
		for(int i=0;i<sn;i++)
			r = min(r, gettable(i,0));
		cout << "Case #" << casei+1 << ": " << r << endl;
	}
	return 0;
}
