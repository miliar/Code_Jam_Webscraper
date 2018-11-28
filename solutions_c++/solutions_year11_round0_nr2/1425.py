#include <iostream>
#include <string>

using namespace std;

int loc(char card);

int main (int argc, char * const argv[]) {
    char Gx1[8][8], Gx2[8][8], card1, card2, card3;
	int T, C, D, i, j, k, N;
	string s;
	bool CanAdd;
	
	cin >> T;
	
	for (i=0; i<T; i++) {
		memset(Gx1, 0, 64*sizeof(char));
		memset(Gx2, 0, 64*sizeof(char));
		s.clear();
		
		cin >> C;
		for (j=0; j<C; j++) {
			do {
				cin >> card1;
			} while ((card1 <'A') || (card1 > 'Z'));
			cin >> card2 >> card3;
			Gx1[loc(card1)][loc(card2)] = Gx1 [loc(card2)][loc(card1)] = card3;
		}
		
		cin >> D;
		for (j=0; j<D; j++) {
			do {
				cin >> card1;
			} while ((card1 <'A') || (card1 > 'Z'));
			cin >> card2;
			Gx2[loc(card1)][loc(card2)] = Gx2 [loc(card2)][loc(card1)] = 1;
		}
		
		cin >> N;
		for (j=0; j<N; j++) {
			do {
				cin >> card1;
			} while ((card1 <'A') || (card1 > 'Z')); 
			
			CanAdd = true;
			
			if ((loc(s[s.length() - 1]) < 8) && (Gx1 [loc(card1)][loc(s[s.length() - 1])] > 1)) {
				s[s.length()-1] = Gx1 [loc(card1)][loc(s[k])];
				CanAdd = false;
			} else {
				for (k=0; k<s.length(); k++) {
					if ((loc(s[k]) < 8) & (Gx2 [loc(card1)][loc(s[k])] == 1)) {
						s.clear(); 
						CanAdd = false;
						break;
					} 
				}
			}
			
			if (CanAdd) s += card1;
		}
		printf("Case #%d: [", i+1 );
		if (s.length() > 0) {
			for (j=0; j<s.length()-1; j++) {
				cout << s[j] <<", ";
			}
			cout << s[s.length()-1];
		}
		printf("]\n");
	}
	return 0;
}

int loc(char card) {
	switch (card) {
		case 'Q':
			return 0;
			break;
		case 'W':
			return 1;
			break;
		case 'E':
			return 2;
			break;
		case 'R':
			return 3;
			break;
		case 'A':
			return 4;
			break;
		case 'S':
			return 5;
			break;
		case 'D':
			return 6;
			break;
		case 'F':
			return 7;
			break;
	}
	return 8;
}