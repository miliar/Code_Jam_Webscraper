// for MinGW g++ 3.4.5
#include <iostream>
#include <string>
#include <map>

using namespace std;

std::map<pair<int,int>,bool>	happiness;

bool ishappy(int base, int number) {
	pair<int,int> key(base,number);
	map<pair<int,int>,bool>::const_iterator v = happiness.find(key);
	if (v != happiness.end()) {
		return	v->second;
	}


	int x = 0;
	do {
		int digit = number % base;
		x += digit * digit;
		number = number / base;
	} while (number != 0);

	happiness[key] = false;
	bool result = (x == 1) ? true : ishappy(base,x);
	happiness[key] = result;
	return result;
}

int main(){
	int T;
	cin >> T;
	string dummy;
	getline(cin, dummy);

	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";

		string s;
		getline(cin, s);
		
		int base[9];
		int count = sscanf(s.c_str(), "%d%d%d%d%d%d%d%d%d", &base[0],&base[1],&base[2],&base[3],&base[4],&base[5],&base[6],&base[7],&base[8]);
		int number = 2;
		for (;;) {
			bool hit = true;
			for (int i = 0; i < count; ++i) {
				if (!ishappy(base[i], number)) { hit = false; break; }
			}
			if (hit) break;
			++number;
		}
		cout << number << endl;
	}
}
