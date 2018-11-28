#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

void switchChar(char G[]);

void main () {
	int T;
	char G[31][101];
	ifstream fin;
	fin.open("A-small-attempt1.in");
	fin >> T;
	fin.get();

	ofstream fout;
	fout.open("Output.txt");
    for (int i = 0; i < T; i++) {
		fin.getline(G[i],101);
        switchChar(G[i]);
		fout << "Case #" << i+1 << ": " << G[i] << endl;
    }
	fin.close();
	fout.close();
}

void switchChar(char G[]) {
    int a = strlen(G);
    for (int i = 0; i < a;i++) {
		switch (G[i]) {
		case 'a':
			G[i] = 'y';
			break;
		case 'b':
			G[i] = 'h';
			break;
		case 'c':
			G[i] = 'e';
			break;
		case 'd':
			G[i] = 's';
			break;
		case 'e':
			G[i] = 'o';
			break;
		case 'f':
			G[i] = 'c';
			break;
		case 'g':
			G[i] = 'v';
			break;
		case 'h':
			G[i] = 'x';
			break;
		case 'i':
			G[i] = 'd';
			break;
		case 'j':
			G[i] = 'u';
			break;
		case 'k':
			G[i] = 'i';
			break;
		case 'l':
			G[i] = 'g';
			break;
		case 'm':
			G[i] = 'l';
			break;
		case 'n':
			G[i] = 'b';
			break;
		case 'o':
			G[i] = 'k';
			break;
		case 'p':
			G[i] = 'r';
			break;
		case 'q':
			G[i] = 'z';
			break;
		case 'r':
			G[i] = 't';
			break;
		case 's':
			G[i] = 'n';
			break;
		case 't':
			G[i] = 'w';
			break;
		case 'u':
			G[i] = 'j';
			break;
		case 'v':
			G[i] = 'p';
			break;
		case 'w':
			G[i] = 'f';
			break;
		case 'x':
			G[i] = 'm';
			break;
		case 'y':
			G[i] = 'a';
			break;
		case 'z':
			G[i] = 'q';
			break;
		}
    }
}