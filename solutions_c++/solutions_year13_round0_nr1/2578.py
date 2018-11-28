#include <fstream>
#include <string>
using namespace std;

ifstream f("A-small-attempt0.in"); ofstream g("A-small-attempt0.out");

int i, j, k, n, m;
int points, xs, os, ts;
string s[4];
bool found;

void process (char c){
	if (c=='.') points++;
	else if (c=='X') xs++;
	else if (c=='O') os++;
	else if (c=='T') ts++;
}

int main(){
	f>>n;
	for (i=1; i<=n; i++){
		found = 0;
		for (j=0; j<4; j++)	f>>s[j];
		for (j=0; j<4 && !found; j++){
			points = xs = os = ts = 0;
			for (k=0; k<4; k++)	process (s[j][k]);
			if (os+ts==4 || xs+ts==4) found = 1;
		}
		for (j=0; j<4 && !found; j++){
			points = xs = os = ts = 0;
			for (k=0; k<4; k++) process (s[k][j]);
			if (os+ts==4 || xs+ts==4) found = 1;
		}
		if (!found){
			points = xs = os = ts = 0;
			process (s[1][1]); process (s[2][2]); process (s[3][3]); process (s[0][0]); 
			if (os+ts==4 || xs+ts==4) found = 1;
		}
		if (!found){
			points = xs = os = ts = 0;
			process (s[0][3]); process (s[1][2]); process (s[2][1]); process (s[3][0]); 
			if (os+ts==4 || xs+ts==4) found = 1;
		}
		
		if (found){
			if (os+ts==4) g<<"Case #"<<i<<": O won\n";
			else g<<"Case #"<<i<<": X won\n";
		}
		else {
			if (points!=0) g<<"Case #"<<i<<": Game has not completed\n";
			else g<<"Case #"<<i<<": Draw\n";
		}
	}
}
