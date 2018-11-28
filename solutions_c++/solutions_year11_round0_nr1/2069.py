#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

int myAbs(int t){
	return t < 0 ? -t : t;
}

long long solve(){
	long long T = 0;
	int posO = 1, posB = 1, n;
	char op; int pos;

	vector < int > buttonsOrange;
	vector < int > buttonsBlue;
	vector < pair < char, int > > buttons;

	cin >> n;
	for (int i = 0; i < n; i++){
		cin >> op >> pos;

		if (op == 'O'){
			buttonsOrange.push_back(pos);
		}
		if (op == 'B'){
			buttonsBlue.push_back(pos);
		}

		buttons.push_back(make_pair(op, pos));
	}

	int indexBlue = 0, indexOrange = 0;
	int lengthO, lengthB;
	for (int i = 0; i < n; i++){
		op = buttons[i].first;
		pos = buttons[i].second;
		lengthO = 0; lengthB = 0;

		if (op == 'O'){
			lengthO = myAbs(pos - posO);
			if (indexBlue < buttonsBlue.size()) {
				lengthB = myAbs(buttonsBlue[indexBlue] - posB);
			}

			T += lengthO + 1;
			posO = pos; indexOrange++;

			if (indexBlue >= buttonsBlue.size()) continue;

			if (lengthO + 1 >= lengthB){
				posB = buttonsBlue[indexBlue];
			}
			else{
				if (posB < buttonsBlue[indexBlue]){
					posB += lengthO + 1;
				}
				else {
					posB -= lengthO + 1;
				}
			}
		}
		if (op == 'B'){
			lengthB = myAbs(pos - posB);
			if (indexOrange < buttonsOrange.size()){
				lengthO = myAbs(buttonsOrange[indexOrange] - posO);
			}

			T += lengthB + 1;
			posB = pos; indexBlue++;

			if (indexOrange >= buttonsOrange.size()) continue;

			if (lengthB + 1 >= lengthO){
				posO = buttonsOrange[indexOrange];
			}
			else{
				if (posO < buttonsOrange[indexOrange]){
					posO += lengthB + 1;
				}
				else{
					posO -= lengthB + 1;
				}
			}
		}
	}

	return T;
}

int main(){
	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; t++){
		cout << "Case #" << t << ": " << solve() << endl;
	}

	return 0;
}
/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
*/
