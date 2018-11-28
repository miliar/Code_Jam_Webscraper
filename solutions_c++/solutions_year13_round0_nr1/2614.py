#include <iostream>
#include <cstring>

using namespace std;

struct casa {
    int cima, esq, diag, diagc;


};

int main()
{
    int t, c = 1;
    cin >> t;
    while (t--) {
		cout << "Case #" << c++ << ": ";
		string M[4];
		casa O[6][6], X[6][6];
		bool p = false;
		for (int i = 0; i < 6; ++i)
		    for (int j = 0; j < 6; ++j) {
				O[i][j].cima = O[i][j].esq = O[i][j].diag = O[i][j].diagc = 0;
				X[i][j].cima = X[i][j].esq = X[i][j].diag = X[i][j].diagc = 0;
		    }
		cin >> M[0] >> M[1] >> M[2] >> M[3];

		for (int i = 0; i < 4; ++i) {
		    for (int j = 0; j < 4; ++j) {
		    	if(M[i][j] == '.')p = true;
				if (M[i][j] == 'O' || M[i][j] == 'T') {
				    O[i + 1][j + 1].esq = O[i + 1][j].esq + 1;
				    O[i + 1][j + 1].cima = O[i][j + 1].cima + 1;
				    O[i + 1][j + 1].diag = O[i][j].diag + 1;
				    O[i + 1][j + 1].diagc = O[i][j+2].diagc + 1;
				}
				if (M[i][j] == 'X' || M[i][j] == 'T') {
				    X[i + 1][j + 1].esq = X[i + 1][j].esq + 1;
				    X[i + 1][j + 1].cima = X[i][j + 1].cima + 1;
				    X[i + 1][j + 1].diag = X[i][j].diag + 1;
				    X[i + 1][j + 1].diagc = X[i][j+2].diagc + 1;
				}
		    }
		}
		bool Xwin = false, Owin = false;
		for (int i = 1; i < 5; ++i) {
		  //  cout << endl;
		    for (int j = 1; j < 5; ++j) {
		//	cout << O[i][j].diagc << " ";
			if (O[i][j].cima >= 4 || O[i][j].esq >= 4 || O[i][j].diag >= 4 || O[i][j].diagc >= 4)
			    Owin = true;
			if (X[i][j].cima >= 4 || X[i][j].esq >= 4 || X[i][j].diag >= 4 || X[i][j].diagc >= 4)
			    Xwin = true;
		    }

		}
		//cout << endl;
		if (Xwin && Owin)
		    cout << "Draw" << endl;
		if (Xwin && !Owin)
		    cout << "X won" << endl;
		if (Owin && !Xwin)
		    cout << "O won" << endl;
		if(!Xwin && !Owin && p)cout<<"Game has not completed"<<endl;
		if(!Xwin && !Owin && !p)cout << "Draw" << endl;
    }


    return 0;
}
