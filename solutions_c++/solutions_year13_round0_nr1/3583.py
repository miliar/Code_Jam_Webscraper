#include <iostream>
#include <cstring>
#include <string>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <climits>
using namespace std;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	cin >> t;
	for (int l = 1; l <= t; l++) {	
		string str[4];
		for (int i = 0; i < 4; i++) cin >> str[i];
		bool wonx = false, wono = false, full = true;
		for (int i = 0; i < 4; i++) {
			int numx = 0, numo = 0, numt = 0;
			for (int j = 0; j < 4; j++) {
				if (str[i][j] == '.') full = false;
				if (str[i][j] == 'X') numx++;
				if (str[i][j] == 'O') numo++;
				if (str[i][j] == 'T') numt++;
			}
			if ((numx == 3 && numt == 1) || numx == 4) wonx = true;
			if ((numo == 3 && numt == 1) || numo == 4) wono = true;
		}
		for (int j = 0; j < 4; j++) {
			int numx = 0, numo = 0, numt = 0;
			for (int i = 0; i < 4; i++) {
				if (str[i][j] == '.') full = false;
				if (str[i][j] == 'X') numx++;
				if (str[i][j] == 'O') numo++;
				if (str[i][j] == 'T') numt++;
			}
			if ((numx == 3 && numt == 1) || numx == 4) wonx = true;
			if ((numo == 3 && numt == 1) || numo == 4) wono = true;
		}
		int numx = 0, numo = 0, numt = 0;	
		for (int i = 0; i < 4; i++) {
			//if (str[i][i] == '.') full = false;                             
                        if (str[i][i] == 'X') numx++;
                        if (str[i][i] == 'O') numo++;
                        if (str[i][i] == 'T') numt++;
		}
		if ((numx == 3 && numt == 1) || numx == 4) wonx = true;
		if ((numo == 3 && numt == 1) || numo == 4) wono = true;
		numx = 0; numo = 0; numt = 0;	
		for (int i = 0; i < 4; i++) {
			//if (str[i][i] == '.') full = false;                             
                        if (str[i][3 - i] == 'X') numx++;
                        if (str[i][3 - i] == 'O') numo++;
                        if (str[i][3 - i] == 'T') numt++;
		}
		if ((numx == 3 && numt == 1) || numx == 4) wonx = true;
		if ((numo == 3 && numt == 1) || numo == 4) wono = true;
	 	if (wonx) cout << "Case #" << l << ": X won\n";
	 	if (wono) cout << "Case #" << l << ": O won\n";
		if (!wono && !wonx && full) cout << "Case #" << l << ": Draw\n";
		if (!wono && !wonx && !full) cout << "Case #" << l << ": Game has not completed\n";
	}
	return 0;
}
		
