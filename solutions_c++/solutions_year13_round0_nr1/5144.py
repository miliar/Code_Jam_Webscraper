#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

bool win(const vector<string> & table,char c) {
	for (int j=0;j < 4;++j) {
		if (std::all_of( table[j].begin(),table[j].end(),[c](char d) {return c == d || d == 'T';}))
			return true;
	}
	for (int i = 0;i < 4;++i) {
		bool ok = true;
		for (int j=0;j < 4;++j) {
			if (table[j][i] != c && table[j][i] != 'T')
				ok = false;
		}
		if (ok) return true;
	}
	bool ok = true;
	for (int i=0;i < 4;++i) {
		if (table[i][i] != c && table[i][i] != 'T')
			ok = false;
	}
	if (ok) return true;
	ok = true;
	for (int i=0;i < 4;++i) {
		if (table[i][3-i] != c && table[i][3-i] != 'T')
			ok = false;
	}
	if (ok) return true;
	return false;	
}

bool full(const vector<string> & table) {
	for (int i=0;i < 4;++i)
		if ( ! std::all_of( table[i].begin(),table[i].end(),[](char d) {return d != '.';}) )
			return false;
	return true;
}

int main(int argc, char **argv) {
    int N;
	
	cin >> N;
	cin.ignore(1000,'\n');
	for (int i=0;i < N;++i) {
		vector<string> table(4);
		for (int j=0;j < 4;++j) {
			getline(cin,table[j]);
			assert(table[j].size() == 4);
		}
		string ans;
		bool xwin = win(table,'X');
		bool owin = win(table,'O');
		bool f = full(table);
		if (xwin) ans = "X won";
		else if (owin) ans = "O won";
		else if (f) ans = "Draw";
		else ans = "Game has not completed";
		
		std::cout << "Case #" << (i+1) << ": " << ans << std::endl;
		cin.ignore(1000,'\n');
	}
	
    return 0;
}
