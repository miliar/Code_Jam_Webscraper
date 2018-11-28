#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>

#include<stdio.h>
#include<ctype.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
#define SZ size

int main () {
	int pocet, i;
	map <char, char> pismena;
	char znak;
	pismena.insert(pair<char, char>('a', 'y'));
	pismena.insert(pair<char, char>('b', 'h'));
	pismena.insert(pair<char, char>('c', 'e'));
	pismena.insert(pair<char, char>('d', 's'));
	pismena.insert(pair<char, char>('e', 'o'));
	pismena.insert(pair<char, char>('f', 'c'));
	pismena.insert(pair<char, char>('g', 'v'));
	pismena.insert(pair<char, char>('h', 'x'));
	pismena.insert(pair<char, char>('i', 'd'));
	pismena.insert(pair<char, char>('j', 'u'));
	pismena.insert(pair<char, char>('k', 'i'));
	pismena.insert(pair<char, char>('l', 'g'));
	pismena.insert(pair<char, char>('m', 'l'));
	pismena.insert(pair<char, char>('n', 'b'));
	pismena.insert(pair<char, char>('o', 'k'));
	pismena.insert(pair<char, char>('p', 'r'));
	pismena.insert(pair<char, char>('r', 't'));
	pismena.insert(pair<char, char>('s', 'n'));
	pismena.insert(pair<char, char>('t', 'w'));
	pismena.insert(pair<char, char>('v', 'p'));
	pismena.insert(pair<char, char>('u', 'j'));
	pismena.insert(pair<char, char>('w', 'f'));
	pismena.insert(pair<char, char>('z', 'q'));
	pismena.insert(pair<char, char>('q', 'z'));
	pismena.insert(pair<char, char>('y', 'a'));
	pismena.insert(pair<char, char>('x', 'm'));
	pismena.insert(pair<char, char>(' ', ' '));
	pismena.insert(pair<char, char>('\n', '\n'));
	cin >> pocet;
	cout << "Case #1: ";
	scanf("%c", &znak);
	for (i = 0; i < pocet;) {
		scanf("%c", &znak);
		cout << pismena[znak];
		if (znak == '\n') {
			i++;
			if (i != pocet)
				cout << "Case #" << i + 1 << ": ";
		}
	}
	return 0;
}