#include<iostream>
#include<cstdlib>
#include<cstring>

using namespace std;

char GtoE (char a){
	if (a == 'a') return 'y';
	else if (a == 'b') return 'h';
	else if (a == 'c') return 'e';
	else if (a == 'd') return 's';
	else if (a == 'e') return 'o';
	else if (a == 'f') return 'c';
	else if (a == 'g') return 'v';
	else if (a == 'h') return 'x';
	else if (a == 'i') return 'd';
	else if (a == 'j') return 'u';
	else if (a == 'k') return 'i';
	else if (a == 'l') return 'g';
	else if (a == 'm') return 'l';
	else if (a == 'n') return 'b';
	else if (a == 'o') return 'k';
	else if (a == 'p') return 'r';
	else if (a == 'q') return 'z';
	else if (a == 'r') return 't';
	else if (a == 's') return 'n';
	else if (a == 't') return 'w';
	else if (a == 'u') return 'j';
	else if (a == 'v') return 'p';
	else if (a == 'w') return 'f';
	else if (a == 'x') return 'm';
	else if (a == 'y') return 'a';
	else if (a == 'z') return 'q';
	else if (a == ' ') return ' ';
}

string w (string q) {
	string s = q;
	int j;
	for (j = 0; j < q.length(); j++) {
		s[j] = GtoE(q[j]);
	}
	return s;
}

int main(){
	int N, i;
	cin >> N;
	string *Input = new string[N+1]; 
	for (i = 0; i <= N; i++) {
		getline(cin, Input[i]);
	}
	
	for (i = 0; i <= N; i++) {
		if (i > 0) {
			cout << "Case #" << i << ": ";
			cout << w(Input[i]) << endl;
		}
	}
	return 0;
}