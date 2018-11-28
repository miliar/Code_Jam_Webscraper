#include <fstream>
#include <string>
#include <vector>
using namespace std;

ofstream out("a.out");
ifstream in("a.in");

char d[5000][15] = {0};
string n[500];
int cn[500] = {0};
vector<string> segments[500];
int L, D, N;

void find(char *str){
	int len = strlen(str);
	for (int r = 0; r < N; r++){
		if (segments[r].size() == len){
			bool found = true;
			for (int p = 0; p < len; p++) if (segments[r][p].find(str[p]) == string.npos) found = false;
			if (found) cn[r]++;
		}
	}
}

int main(){
	in >> L >> D >> N;
	for (int r = 0; r < D; r++) in >> d[r];
	for (int p = 0; p < N; p++) {
		in >> n[p];
		bool brack = false;
		string str;
		for (int r = 0; r < n[p].size(); r++){
			if (n[p][r] == '(') {brack = true; continue;}
			else if (n[p][r] == ')') {brack = false; segments[p].push_back(str); str.clear(); continue;}
			else if (brack == true) str.push_back(n[p][r]);
			else if (brack == false) {str.push_back(n[p][r]); segments[p].push_back(str); str.clear();}
		}
	}
	for (int r = 0; r < D; r++) find(d[r]);
	for (int r = 0; r < N; r++) out << "Case #" << r+1 << ": " << cn[r] << endl;
	return 0;
}