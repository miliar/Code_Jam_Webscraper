//be name oo
#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <utility>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <sstream>
#include <set>
#include <complex>
#include <iomanip>
#include <queue>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define show(x) cerr << "#" << #x << ": " << x << endl
#define F first
#define S second
#define X real()
#define Y imag()

using namespace std;
typedef pair<int, int> pii;
typedef complex<double> point;

bool win(char c, string tab[]){
	int dig1 = 0, dig2 = 0;
	FOR(i, 4){
		int countv = 0;
		int counth = 0;
		FOR(j, 4){
			if(tab[i][j] == c || tab[i][j] == 'T')
				countv++;
			if(tab[j][i] == c || tab[j][i] == 'T')
				counth++;
		}
		if((countv == 4) || (counth == 4))
			return true;
		if(tab[i][i] == c || tab[i][i] == 'T')
			dig1++;
		if(tab[i][3 - i] == c || tab[i][3 - i] == 'T')
			dig2++;
	}
	if(dig1 == 4 || dig2 == 4)
		return true;
	return false;
}

int main(){
	int n;
	cin >> n;
	int testCase = 1;
	while(n--){
		cout << "Case #" << testCase++ << ": ";

		string tab[4];
		FOR(i, 4)
			cin >> tab[i];
		if(win('O', tab))
			cout << "O won" << endl;
		else if(win('X', tab))
			cout << "X won" << endl;
		else{
			int countEmpty = 0;
			FOR(i, 4)
				FOR(j, 4)
					if(tab[i][j] == '.')
						countEmpty++;
			if(countEmpty)
				cout << "Game has not completed" << endl;
			else
				cout << "Draw" << endl;
		}


	}
	return 0;
}

