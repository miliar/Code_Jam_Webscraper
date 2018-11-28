#include <iostream>
#include <cmath>

using namespace std;


int main () {
char shit=0, mapa[4][4];
int cases=0;

scanf("%d\n", &cases);
//cout << cases << endl;
for (int g=1; g<=(cases); g++){
//	cout << g << endl;
for (int i=0; i<4; i++)
scanf ("%c%c%c%c\n", &mapa[i][0], &mapa[i][1], &mapa[i][2], &mapa[i][3]);


//for (int i=0; i<4; i++)
//printf ("%c%c%c%c\n", mapa[i][0], mapa[i][1], mapa[i][2], mapa[i][3]);
//printf("%d\n", cases);

for (int i=0; i<4; i++) {
	if ((mapa[i][0]=='X' || mapa[i][0]=='T') && (mapa[i][1]=='X' || mapa[i][1]=='T') && (mapa[i][2]=='X' || mapa[i][2]=='T') && (mapa[i][3]=='X' || mapa[i][3]=='T')) {cout << "Case #" << g << ": X won\n"; goto koniec;}
	if ((mapa[i][0]=='O' || mapa[i][0]=='T') && (mapa[i][1]=='O' || mapa[i][1]=='T') && (mapa[i][2]=='O' || mapa[i][2]=='T') && (mapa[i][3]=='O' || mapa[i][3]=='T')) {cout << "Case #" << g << ": O won\n"; goto koniec;}
	if ((mapa[0][i]=='X' || mapa[0][i]=='T') && (mapa[1][i]=='X' || mapa[1][i]=='T') && (mapa[2][i]=='X' || mapa[2][i]=='T') && (mapa[3][i]=='X' || mapa[3][i]=='T')) {cout << "Case #" << g << ": X won\n"; goto koniec;}
	if ((mapa[0][i]=='O' || mapa[0][i]=='T') && (mapa[1][i]=='O' || mapa[1][i]=='T') && (mapa[2][i]=='O' || mapa[2][i]=='T') && (mapa[3][i]=='O' || mapa[3][i]=='T')) {cout << "Case #" << g << ": O won\n"; goto koniec;}

}

if ((mapa[0][0]=='X' || mapa[0][0]=='T') && (mapa[1][1]=='X' || mapa[1][1]=='T') && (mapa[2][2]=='X' || mapa[2][2]=='T') && (mapa[3][3]=='X' || mapa[3][3]=='T')) {cout << "Case #" << g << ": X won\n"; goto koniec;}
if ((mapa[0][0]=='O' || mapa[0][0]=='T') && (mapa[1][1]=='O' || mapa[1][1]=='T') && (mapa[2][2]=='O' || mapa[2][2]=='T') && (mapa[3][3]=='O' || mapa[3][3]=='T')) {cout << "Case #" << g << ": O won\n"; goto koniec;}

if ((mapa[3][0]=='X' || mapa[3][0]=='T') && (mapa[2][1]=='X' || mapa[2][1]=='T') && (mapa[1][2]=='X' || mapa[1][2]=='T') && (mapa[0][3]=='X' || mapa[0][3]=='T')) {cout << "Case #" << g << ": X won\n"; goto koniec;}
if ((mapa[3][0]=='O' || mapa[3][0]=='T') && (mapa[2][1]=='O' || mapa[2][1]=='T') && (mapa[1][2]=='O' || mapa[1][2]=='T') && (mapa[0][3]=='O' || mapa[0][3]=='T')) {cout << "Case #" << g << ": O won\n"; goto koniec;}

for (int i=0; i<4; i++) 
	for (int j=0; j<4; j++) {
		if (mapa[i][j] == '.') {cout << "Case #" << g << ": Game has not completed\n"; goto koniec;}
}

cout << "Case #" << g << ": Draw\n"; goto koniec;
//cout << endl;
koniec:
shit=0;
}


return 0;
}
