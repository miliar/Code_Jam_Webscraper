#include <iostream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define abs(x) ((x) > 0 ? (x) : -1*(x))
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))

char letter(char A) 
{
	switch(A) {
	case 'a':
		return 'y';
	case 'b':
		return 'h';
	case 'c':
		return 'e';
	case 'd':
		return 's';
	case 'e':
		return 'o';
	case 'f':
		return 'c';
	case 'g':
		return 'v';
	case 'h':
		return 'x';
	case 'i':
		return 'd';
	case 'j':
		return 'u';
	case 'k':
		return 'i';
	case 'l':
		return 'g';
	case 'm':
		return 'l';
	case 'n':
		return 'b';
	case 'o':
		return 'k';
	case 'p':
		return 'r';
	case 'q':
		return 'z';
	case 'r':
		return 't';
	case 's':
		return 'n';
	case 't':
		return 'w';
	case 'u':
		return 'j';
	case 'v':
		return 'p';
	case 'w':
		return 'f';
	case 'x':
		return 'm';
	case 'y':
		return 'a';
	case 'z':
		return 'q';
	}
	
	return A;
}

int main()
{
	int T, n;
	char line[101];
	
	cin >> T;
	cin.getline(line, 101);
	for(int i = 1; i <= T; i++) {
		cin.getline(line, 101);
		
		n = strlen(line);
		
		for (int j = 0; j < n; j++) {
			line[j] = letter(line[j]);
		}
		
		cout << "Case #" << i << ": " << line << endl;
	}
	
	return 0;
}
