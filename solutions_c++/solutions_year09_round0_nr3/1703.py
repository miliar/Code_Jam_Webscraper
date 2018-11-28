#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("C-large.in");
ofstream fout("C-large.out");

const int MAXL = 510;

int N;

const char *str = "welcome to code jam";

int		nextc[27][3];
int		nexti[27][3];
char	word[MAXL];
int		total[MAXL][3];

int G(char c) {
	if (c == ' ')
		return 0;
	else
		return c - 'a' + 1;
}

char G(int i) {
	if (i == 0)
		return ' ';
	else
		return 'a' + i - 1;
}

int GetOcc(int p, int w) {
	if (nexti[G(word[p])][w] == -1)
		return 0;	
	else {
		char c = G(nextc[G(word[p])][w]);
		int tmp = 0;
		for (int i = p + 1; i < strlen(word); i++)
			if (word[i] == c)
				tmp += total[i][nexti[G(word[p])][w]];
		return tmp % 10000;
	}
}

void DoIt(int p) {
	memset(total, 0, sizeof(total));
	fin.getline(word, sizeof(word));
	cout << word << endl;
	for (int i = strlen(word) - 1; i >= 0; i--) {
		if (word[i] == 'm') {
			total[i][0] = GetOcc(i, 0);
			total[i][1] = 1;
			total[i][2] = GetOcc(i, 2);
		} 
		else {
			total[i][0] = GetOcc(i, 0);
			total[i][1] = GetOcc(i, 1);
			total[i][2] = GetOcc(i, 2);
		}		
	}
	int tmp = 0;
	for (int i = 0; i < strlen(word); i++)
		if (word[i] == 'w')
			tmp += total[i][0];
	fout << "Case #" << p << ": " 
		<< (tmp / 1000) % 10 
		<< (tmp / 100) % 10 
		<< (tmp / 10) % 10 
		<< (tmp / 1) % 10 << endl;	
}

void GetPos() {
	memset(nextc, 255, sizeof(nextc));
	memset(nexti, 255, sizeof(nexti));
	for (int i = 0; i < strlen(str) - 1; i++) {
		int ti = 0;
		int tj = 0;
		for (int k = 0; k < i; k++)
			if (str[i] == str[k])
				ti++;
		for (int k = 0; k <= i; k++)
			if (str[i + 1] == str[k])
				tj++;
		nextc[G(str[i])][ti] = G(str[i + 1]);
		nexti[G(str[i])][ti] = tj;		
	}
}

int main() {
	GetPos();
	fin >> N;
	fin.getline(word, sizeof(word));
	for (int i = 0; i < N; i++) {
		DoIt(i + 1);
	}
	return 0;
}