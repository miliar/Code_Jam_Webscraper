#include <iostream>
#include <vector>
#include <algorithm>
#include <cctype>
#include <ctime>
int z=0;
using namespace std;

int check (vector < vector <char> > arr,int p, int q, char c) {
	int cnt = 0;
	for (int i = 0; i < 4; i++) {
		if (arr[i][q] == c || arr[i][q] == 'T') {
			cnt++;
			if (cnt == 4)
				return cnt;
		}
		else
			break;
	}
	cnt = 0;
	for (int i = 0; i < 4; i++) {
		if (arr[p][i] == c || arr[p][i] == 'T') {
			cnt++;
			if (cnt == 4)
				return cnt;
		}
		else
			break;
	}
	cnt = 0;
	if (p == q) {
		if ((arr[0][0] == c || arr[0][0] == 'T') && (arr[1][1] == c || arr[1][1] == 'T') && (arr[2][2] == c || arr[2][2] == 'T') && (arr[3][3] == c || arr[3][3] == 'T')) {
			cnt = 4;
			return cnt;
		}
	}
	if ((p == 1 && q==2) || (p==2 && q==1) || (p==3 && q==0) || (p==0 && q==3)) {
		if ((arr[3][0] == c || arr[3][0] == 'T') && (arr[2][1] == c || arr[2][1] == 'T') && (arr[1][2] == c || arr[1][2] == 'T') && (arr[0][3] == c || arr[0][3] == 'T')) {
			cnt = 4;
			return cnt;
		}
	}
	return 0;
}

int main () {
	int t,x;
	vector<int>zx;
	cin >> t;
	for (int y = 1; y <= t; y++) {
	    vector<int> v4;
		int e1= 0,ax=0,ao=0;
		char ch,bv;
		vector < vector <char> > arr (4,vector <char> (4,'c'));
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> ch;
				arr[i][j] = ch;
			}
		}
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (arr[i][j] == '.') {
					e1= 1;
				}
			if (arr[i][j] == 'X')
				ax = check (arr,i,j,arr[i][j]);
			if (arr[i][j] == 'O')
				ao = check (arr,i,j,arr[i][j]);
			}
			if (ax == 4 || ao == 4)
				break;
		}
            if (ax == 4)
                cout <<"Case #"<<y<<": "<< "X won" << endl;
            if (ao == 4)
                cout <<"Case #"<<y<<": "<< "O won" << endl;
            if (ax != 4 && ao != 4) {
                if (e1== 1) {
                    cout <<"Case #"<<y<<": "<<"Game has not completed" << endl;
			}
		}
		if (ax != 4 && ao != 4) {
			if (e1== 0) {
				cout <<"Case #"<<y<<": "<< "Draw" << endl;
			}
		}
	}
	return 0;
}

