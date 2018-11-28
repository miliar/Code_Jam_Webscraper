#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int cal (vector < vector <char> > v,int p, int q, char c) {
	int cou = 0;
	for (int i = 0; i < 4; i++) {
		if (v[i][q] == c || v[i][q] == 'T') {
			cou++;
			if (cou == 4)
				return cou;
		}
		else
			break;
	}
	cou = 0;
	for (int i = 0; i < 4; i++) {
		if (v[p][i] == c || v[p][i] == 'T') {
			cou++;
			if (cou == 4)
				return cou;
		}
		else
			break;
	}
	cou = 0;
	if (p == q) {
		if ((v[0][0] == c || v[0][0] == 'T') && (v[1][1] == c || v[1][1] == 'T') && (v[2][2] == c || v[2][2] == 'T') && (v[3][3] == c || v[3][3] == 'T')) {
			cou = 4;
			return cou;
		}
	}
	if ((p == 1 && q==2) || (p==2 && q==1)) {
		if ((v[3][0] == c || v[3][0] == 'T') && (v[2][1] == c || v[2][1] == 'T') && (v[1][2] == c || v[1][2] == 'T') && (v[0][3] == c || v[0][3] == 'T')) {
			cou = 4;
			return cou;
		}
	}
	if ((p==3 && q == 0) || (p==0 && q==3)) {
		if ((v[3][0] == c || v[3][0] == 'T') && (v[2][1] == c || v[2][1] == 'T') && (v[1][2] == c || v[1][2] == 'T') && (v[0][3] == c || v[0][3] == 'T')) {
			cou = 4;
			return cou;
		}
	}
	return 0;
}

int main () {
	int t;
	cin >> t;
	for (int k = 1; k <= t; k++) {
		int emp = 0;
		int ansx = 0;
		int anso = 0;
		char x;
		vector < vector <char> > v (4,vector <char> (4,'c'));
		//vector < vector <bool> > s (4,vector <bool> (4,false));
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> x;
				v[i][j] = x;
			}
		}
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (v[i][j] == '.') {
					emp = 1;
				}
			//if (emp == 1)
				//break;
			if (v[i][j] == 'X') 
				ansx = cal (v,i,j,v[i][j]);
			if (v[i][j] == 'O')
				anso = cal (v,i,j,v[i][j]);
			}
			if (ansx == 4 || anso == 4)
				break;
			//if (emp == 1)
				//break;
		}
		if (ansx == 4)
			cout <<"Case #"<<k<<": "<< "X won" << endl;
		if (anso == 4)
			cout <<"Case #"<<k<<": "<< "O won" << endl;
		if (ansx != 4 && anso != 4) {
			if (emp == 1) {
				cout <<"Case #"<<k<<": "<<"Game has not completed" << endl;
			}
		}
		if (ansx != 4 && anso != 4) {
			if (emp == 0) {
				cout <<"Case #"<<k<<": "<< "Draw" << endl;
			}
		}

	}
	return 0;
}

