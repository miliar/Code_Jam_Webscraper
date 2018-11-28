#include <iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
char replace(char c)
{
	switch (c) {
		case 'e': return 'o';
		case 'j': return 'u';
		case 'p': return 'r';
		case 'm': return 'l';
		case 'y': return 'a';
		case 's': return 'n';
		case 'l': return 'g';
		case 'c': return 'e';
		case 'k': return 'i';
		case 'd': return 's';
		case 'x': return 'm';
		case 'v': return 'p';
		case 'n': return 'b';
		case 'r': return 't';
		case 'i': return 'd';
		case 'b': return 'h';
		case 't': return 'w';
		case 'a': return 'y';
		case 'h': return 'x';
		case 'w': return 'f';
		case 'f': return 'c';
		case 'o': return 'k';
		case 'u': return 'j';
		case 'g': return 'v';
		case 'z': return 'q';
		case 'q': return 'z';
		default: return c;
	}
}
int main(int argc, char *argv[]) {
	freopen("A-small-attempt0.in.txt", "r", stdin);
	freopen("out.out", "w", stdout);
	int n, t = 1;
	string s;
	scanf("%d", &n);
	getline(cin, s);
	while (n--) {
		getline(cin, s);
		for (int i=0; i<s.length(); i++) 
			s[i] = replace(s[i]);
		printf("Case #%d: ", t++);
		cout << s << endl;
	}
	return 0;
}