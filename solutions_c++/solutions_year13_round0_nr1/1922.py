#include <iostream>
#include <vector>
using namespace std;
typedef vector<char> vc;
typedef vector<vc> vcc;

void read(vcc& m) {
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			cin >> m[i][j];
}

char check(const vcc& m) {
	for (int i = 0; i < 4; ++i) {
		char t = m[i][0];
		for (int j = 1; j < 4; ++j){
			if (t == 'T')
				t = m[i][j];
			else if (t != m[i][j] and m[i][j] != 'T')
				t = '.';
		}
		if (t != '.') 
			return t;
	}
	for (int j = 0; j < 4; ++j) {
		char t = m[0][j];
		for (int i = 1; i < 4; ++i){
			if (t == 'T')
				t = m[i][j];
			else if (t != m[i][j] and m[i][j] != 'T')
				t = '.';
		}
		if (t != '.')
			return t;
	}
	//diagonal
	char t = m[0][0];
	for (int i = 1; i < 4; ++i) {
		if (t == 'T')
			t = m[i][i];
		else if (t != m[i][i] and m[i][i] != 'T')
			t = '.';
	}
	if (t != '.')
		return t;
	t = m[0][3];
	for (int i = 0; i < 4; ++i) {
		if (t == 'T')
			t = m[i][3-i];
		else if (t != m[i][3-i] and m[i][3-i] != 'T')
			t = '.';
	}
	return t;
	

}

int main() {
	int n;
	char c;
	vcc m (4, vc(4));
	cin >> n;
	for (int ncase = 1; ncase <= n; ++ncase) {
		read(m);
		char c = check(m);
		cout << "Case #" << ncase << ": ";
		if (c == '.'){
			bool full = true;
			for (int i = 0; i < 4; ++i) {
				for (int j = 0; j < 4; ++j) {
					if (m[i][j] == '.')
						full = false;
				}
			}
			if (full)
				cout << "Draw" << endl;
			else
				cout << "Game has not completed" << endl;
		}
		else
			cout << c << " won" << endl;
	}

}