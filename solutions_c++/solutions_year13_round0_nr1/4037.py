#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t=1; t<=T; ++t) {
		char field[4][4];
		char winner = 'D';
		for(int i=0; i<4; ++i) for(int j=0; j<4; ++j) {
			cin >> field[i][j];
			if(field[i][j] == '.') winner = 'N';
		}
		for(char team : {'X','O'}) {
			auto pred = [&](char t){return t==team||t=='T';};
			for(int i=0; i<4; ++i) {
				if(all_of(field[i],field[i]+4,pred))
					winner = team;
				for(int j=0; j<5; ++j) {
					if(j==4)
						winner = team;
					else
						if(!pred(field[j][i]))
							break;
				}
			}
			if((pred(field[0][0]) && pred(field[1][1]) &&
				pred(field[2][2]) && pred(field[3][3])) ||
				(pred(field[0][3]) && pred(field[1][2]) &&
			       	pred(field[2][1]) && pred(field[3][0])))
				winner = team;

		}
		cout << "Case #" << t << ": ";
		if(winner == 'N') {
			cout << "Game has not completed\n";
		} else if (winner == 'D') {
			cout << "Draw\n";
		} else
			cout << winner << " won\n";
	}
}
