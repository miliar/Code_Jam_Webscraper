#include <vector>
#include <string>
#include <iostream>

using namespace std;

struct State
{
	bool isFill = true;
	string result = "";
};

void searchHorizon(vector<string> list,State &s)
{
	char work;
	
	for (int i=0; i<4; ++i) {
		work = list[i][0];
		if (work == 'T') {
			work = list[i][1];
		}
		if (work == '.') {
			s.isFill = false;
			continue;
		}
		for (int j=0; j<4; ++j) {
			if(list[i][j] == work || list[i][j] == 'T'){
				if (j == 3) {
					switch (work) {
						case 'O':
							s.result = "O won";
							break;
							
						case 'X':
							s.result = "X won";
							break;
					}
				}
			}
			else if(list[i][j] == '.'){
				s.isFill = false;
				break;
			}
			else {
				break;
			}
		}
	}
}

void searchVertical(vector<string> list,State &s)
{
	char work;
	
	for (int j=0; j<4; ++j) {
		work = list[0][j];
		if (work == 'T') {
			work = list[1][j];
		}
		if (work == '.') {
			s.isFill = false;
			continue;
		}
		for (int i=0; i<4; ++i) {
			if(list[i][j] == work || list[i][j] == 'T'){
				if (i == 3) {
					switch (work) {
						case 'O':
							s.result = "O won";
							break;
							
						case 'X':
							s.result = "X won";
							break;
					}
				}
			}
			else if(list[i][j] == '.'){
				s.isFill = false;
				break;
			}
			else {
				break;
			}
		}
	}
}

void searchSlashRight(vector<string> list,State &s)
{
	char work;
	
	work = list[0][0];
	if (work == 'T') {
		work = list[1][1];
	}
	if (work == '.') {
		s.isFill = false;
		return;
	}
	
	for (int i=0; i<4; ++i) {
		if(list[i][i] == work || list[i][i] == 'T'){
			if (i == 3) {
				switch (work) {
					case 'O':
						s.result = "O won";
						break;
						
					case 'X':
						s.result = "X won";
						break;
				}
			}
		}
		else if(list[i][i] == '.'){
			s.isFill = false;
			return;
		}
		else {
			return;
		}
	}
}

void searchSlashLeft(vector<string> list,State &s)
{
	char work;
	
	work = list[0][3];
	if (work == 'T') {
		work = list[1][2];
	}
	if (work == '.') {
		s.isFill = false;
		return;
	}
	
	int j;
	for (int i=0; i<4; ++i) {
		j = 3 - i;
		if(list[j][i] == work || list[j][i] == 'T'){
			if (i == 3) {
				switch (work) {
					case 'O':
						s.result = "O won";
						break;
						
					case 'X':
						s.result = "X won";
						break;
				}
			}
		}
		else if(list[j][i] == '.'){
			s.isFill = false;
			return;
		}
		else {
			return;
		}
	}
}

string solve(vector<string> list)
{
	State s;
	searchHorizon(list,s);
	searchVertical(list,s);
	searchSlashRight(list, s);
	searchSlashLeft(list, s);
	
	if (s.result != "") {
		return s.result;
	}
	if (s.isFill) {
		return "Draw";
	}
	else{
		return "Game has not completed";
	}
}

int main()
{
	int num;
	cin >> num;
	for (int i=0; i<num+1; ++i) {
		vector<string> list(4);
		for (vector<string>::iterator it = list.begin(); it != list.end(); ++it) {
			cin >> *it;
		}
		
		string result = solve(list);
		cout << "Case #" << i+1 << ": " ;
		cout << result << endl;
		
		list.clear();
	}
	return 0;
}