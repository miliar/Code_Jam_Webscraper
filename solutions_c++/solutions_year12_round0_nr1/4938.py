#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#define INF 100000000

using namespace std;

inline char transf(char c)
{
	if (c=='a') return 'y';
	if (c=='b') return 'h';
	if (c=='c') return 'e';
	if (c=='d') return 's';
	if (c=='e') return 'o';
	if (c=='f') return 'c';
	if (c=='g') return 'v';
	if (c=='h') return 'x';
	if (c=='i') return 'd';
	if (c=='j') return 'u';
	if (c=='k') return 'i';
	if (c=='l') return 'g';
	if (c=='m') return 'l';
	if (c=='n') return 'b';
	if (c=='o') return 'k';
	if (c=='p') return 'r';
	if (c=='q') return 'z';
	if (c=='r') return 't';
	if (c=='s') return 'n';
	if (c=='t') return 'w';
	if (c=='u') return 'j';
	if (c=='v') return 'p';
	if (c=='w') return 'f';
	if (c=='x') return 'm';
	if (c=='y') return 'a';
	if (c=='z') return 'q';
}

int main(void)
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int t;
	string s;
	scanf("%d\n", &t);
	for (int i=0; i<t; i++)
	{
		getline(cin, s);
		cout << "Case #" << i+1 << ": ";
		for (int j=0; j<s.length(); j++)
			printf("%c", transf(s[j]));
		cout << endl;
	}
}