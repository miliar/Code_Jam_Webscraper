#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#define MAXL 501
using namespace std;

ifstream fin("welcomeSmall.in");
ofstream fout("welcomeSmall.out");

const string wc = "welcome to code jam";

string s;

void process(int test) {
	int f[MAXL][MAXL];
	f[0][0] = (s[0] == wc[0]) ?1 :0;
	for (int i=1; i<s.length(); i++)
		if (s[i] == wc[0]) f[i][0] = f[i-1][0] + 1;
		else f[i][0] = f[i-1][0];
		
	for (int i=1; i<s.length(); i++) {
		int m = (wc.length()-1 < i) ? (wc.length()-1) : i;
		for (int j=1; j<=m; j++)
			if (s[i] != wc[j]) f[i][j] = f[i-1][j];
			else f[i][j] = (f[i-1][j] + f[i-1][j-1]) % 10000;
	}
	
	char str[10];
	itoa(f[s.length()-1][wc.length()-1], str, 10);
	fout << "Case #" << test <<": ";
	for (int i=1; i<=4-strlen(str); i++) fout << 0;
	fout << str << endl;	
}

int main()
{
	int numOfTest;
	fin >> numOfTest;
	getline(fin, s);
	
	for (int test=1; test<=numOfTest; test++) {
		getline(fin, s);
		process( test );
	}
//	fflush(stdin); cin.get();
	fin.close();
	fout.close();
}
