#include <iostream>
#include <string>

using namespace std;

int main() {
	freopen ("A-large.in","r",stdin);
	freopen ("out.txt","w",stdout);
	string s;
	int t=0;
	cin>>t;
	char a[4][4];
	for (int ww=0; ww<t; ww++) {
		for (int j=0; j<4; j++) {
			cin>>s;
			a[j][0]=s[0];
			a[j][1]=s[1];
			a[j][2]=s[2];
			a[j][3]=s[3];
		}
		bool wX=false;
		bool wO=false;
		
		for (int i=0; i<4; i++) {
			int nO=0;
			int nX=0;
			bool tt=false;
			for (int j=0; j<4; j++) {
				if (a[i][j]=='X') nX++;
				else if (a[i][j]=='O') nO++;
				else if (a[i][j]=='T') tt=true;
			}
			if (nX==4 || (nX==3 && tt)) wX=true;
			if (nO==4 || (nO==3 && tt)) wO=true;
		}

		for (int i=0; i<4; i++) {
			int nO=0;
			int nX=0;
			bool tt=false;
			for (int j=0; j<4; j++) {
				if (a[j][i]=='X') nX++;
				else if (a[j][i]=='O') nO++;
				else if (a[j][i]=='T') tt=true;
			}
			if (nX==4 || (nX==3 && tt)) wX=true;
			if (nO==4 || (nO==3 && tt)) wO=true;
		}

		int nO=0;
		int nX=0;
		bool tt=false;
		if (a[0][0]=='X') nX++;
		else if (a[0][0]=='O') nO++;
		else if (a[0][0]=='T') tt=true;
		if (a[1][1]=='X') nX++;
		else if (a[1][1]=='O') nO++;
		else if (a[1][1]=='T') tt=true;
		if (a[2][2]=='X') nX++;
		else if (a[2][2]=='O') nO++;
		else if (a[2][2]=='T') tt=true;
		if (a[3][3]=='X') nX++;
		else if (a[3][3]=='O') nO++;
		else if (a[3][3]=='T') tt=true;
		if (nX==4 || (nX==3 && tt)) wX=true;
		if (nO==4 || (nO==3 && tt)) wO=true;

		nO=0;
		nX=0;
		tt=false;
		if (a[0][3]=='X') nX++;
		else if (a[0][3]=='O') nO++;
		else if (a[0][3]=='T') tt=true;
		if (a[1][2]=='X') nX++;
		else if (a[1][2]=='O') nO++;
		else if (a[1][2]=='T') tt=true;
		if (a[2][1]=='X') nX++;
		else if (a[2][1]=='O') nO++;
		else if (a[2][1]=='T') tt=true;
		if (a[3][0]=='X') nX++;
		else if (a[3][0]=='O') nO++;
		else if (a[3][0]=='T') tt=true;
		if (nX==4 || (nX==3 && tt)) wX=true;
		if (nO==4 || (nO==3 && tt)) wO=true;
		
		int nn=0;
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				if (a[i][j]!='.')
					nn++;
			}
		}

		cout<<"Case #"<<ww+1<<": ";
		if ((wX && wO)||(!wX && !wO && (nn==16))) {
			cout<<"Draw";
		}
		else if (wX) {
			cout<<"X won";
		}
		else if (wO) {
			cout<<"O won";
		}
		else {
			cout<<"Game has not completed";
		}
		cout<<'\n';
	}
	return 0;
}