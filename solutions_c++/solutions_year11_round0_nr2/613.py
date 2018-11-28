#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

#define CLEAR(x,with) memset(x,with,sizeof(x))

char trans[256][256];
bool opp[256][256];
int cant[256];
int C, D, N;

int main() {
	int ncasos;
	string s;
	cin >> ncasos;
	for (int caso = 1; caso <= ncasos; caso++) {
		CLEAR(trans, 0);
		CLEAR(opp, false);
		CLEAR(cant, 0);
		cin >> C;
		for (int i = 0; i < C; i++) {
			cin >> s;
			trans[s[0]][s[1]] = s[2];
			trans[s[1]][s[0]] = s[2];
		}
		cin >> D;
		for (int i = 0; i < D; i++) {
			cin >> s;
			opp[s[0]][s[1]] = true;
			opp[s[1]][s[0]] = true;
		}
		cin >> N;
		cin >> s;
		vector<char> spells;
		for (int i = 0; i < N; i++) {
			spells.push_back(s[i]);
			cant[s[i]]++;
			if (spells.size() >= 2 && trans[spells[spells.size()-1]][spells[spells.size()-2]]) {
				char result = trans[spells[spells.size()-1]][spells[spells.size()-2]];
				cant[spells.back()]--;
				spells.pop_back();
				cant[spells.back()]--;
				spells.pop_back();
				spells.push_back(result);
				cant[result]++;
			}
			for (char rest = 'A'; rest <= 'Z'; rest++) {
				if (cant[rest] && rest != spells.back() && opp[rest][spells.back()]) {
					spells.clear();
					CLEAR(cant, 0);
					break;
				}
			}
		}
		cout << "Case #" << caso << ": [";
		for (int i = 0; i < spells.size(); i++) {
			if (i > 0) cout << ", ";
			cout << spells[i];
		}
		cout << "]" << endl;
	}
	return 0;
}

