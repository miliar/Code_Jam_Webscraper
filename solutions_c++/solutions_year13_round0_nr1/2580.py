#include <iostream>
#include <string>

using namespace std;

string s;
string tab[5];
int T;
int w1,w2,k1,k2,d11,d12,d21,d22;
bool notend;
bool p1,p2,draw;
int n;

int main() {

	cin >> T;
	for(int x=1;x<=T;x++) {
		notend = false;
		p1 = p2 = draw = false;
		for(int i=0;i<4;i++) cin >> tab[i];

		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				if(tab[j][j] == 'T') {d11++; d12++;}
				if(tab[j][j] == 'X') d11++;
				if(tab[j][j] == 'O') d12++;

				if(tab[j][3-j] == 'T') {d21++; d22++;}
				if(tab[j][3-j] == 'X') d21++;
				if(tab[j][3-j] == 'O') d22++;

				if(tab[i][j] == 'T') {w1++; w2++;}
				if(tab[i][j] == 'X') w1++;
				if(tab[i][j] == 'O') w2++;

				if(tab[j][i] == 'T') {k1++; k2++;}
				if(tab[j][i] == 'X') k1++;
				if(tab[j][i] == 'O') k2++;

				if(tab[i][j] == '.') notend = true;

			}
			if(w1 == 4 || k1 == 4 || d11 == 4 || d21 == 4) p1 = true;
			if(w2 == 4 || k2 == 4 || d12 == 4 || d22 == 4) p2 = true;
			if(!p1 && !p2 && !notend) draw = true;
			k1 = k2 = w1 = w2 = d11 = d12 = d21 = d22 = 0;
		}

		if(p1) {cout << "Case #"<<x <<": "<<"X won" << endl; continue;}
		if(p2) {cout << "Case #"<<x <<": "<<"O won" << endl; continue;}
		if(draw) {cout << "Case #"<<x <<": "<<"Draw" << endl; continue;}
		if(notend) {cout << "Case #"<<x <<": "<<"Game has not completed" << endl; continue;}
	}
	return 0;
}
