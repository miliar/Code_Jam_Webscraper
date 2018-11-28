#include <iostream>
#include <string>
using namespace std;

int C, D, N;
char comb[37][3] = {0};
char oppo[29][2] = {0};
char list[101] = {0};
string ele = "";

char incomb(char A, char B){
	for (int r = 0; r < C; r++){
		//cout << comb[r][0] << A << ' ' << comb[r][1] << B << endl;
		if ((comb[r][0] == A && comb[r][1] == B) ||
			(comb[r][0] == B && comb[r][1] == A)){
			return comb[r][2];
		}
	}
	return 0;
}
bool isoppo(){
	for (int r = 0; r < D; r++){
		bool flag1 = false, flag2 = false;
		for (int i = 0; i < ele.size(); i++){
			if (ele[i] == oppo[r][0]) flag1 = true;
			if (ele[i] == oppo[r][1]) flag2 = true;
			if (flag1 && flag2) return true;
		}
		if (flag1 && flag2) return true;
	}
	return false;
}

string lst(string a){
	if (a == "") return "[]";
	string ret;
	ret += '[';
	for (int r = 0; r < a.size(); r++){
		ret += a[r];
		if (r != a.size()-1) ret += ", ";
	}
	ret += ']';
	return ret;
}

int main(){
	int T;
	cin >> T;
	for (int r = 0; r < T; r++){
		C = 0, D = 0, N = 0;
		ele = "";
		cin >> C;
		for (int i = 0; i < C; i++) cin >> comb[i];
		cin >> D;
		for (int i = 0; i < D; i++) cin >> oppo[i];
		cin >> N;
		cin >> list;
		for (int i = 0; i < N; i++){
			if ((list[i] == 'Q') ||	(list[i] == 'W') || (list[i] == 'E') ||	(list[i] == 'R') ||	(list[i] == 'A') ||	(list[i] == 'S') ||	(list[i] == 'D') ||	(list[i] == 'F')) ele += list[i];			//cout << "BEFORE:" << ele << endl;
			if (ele.size() > 1){
				char a = incomb(ele[ele.size()-1], ele[ele.size()-2]);
				if (a != 0){
					//cout << a << endl;
					//cout << list[i] << list[i-1] << endl;
					ele.resize(ele.size()-2);
					ele += a;
					//i++;
				}
			}
			if (isoppo()) ele = "";
			//cout << "AFTER:" << ele << endl;
		}
		cout << "Case #" << r+1 << ": " << lst(ele) << endl;
	}
	return 0;
}
