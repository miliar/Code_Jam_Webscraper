#include <cstdio>
#include <iostream>
#include <sstream>
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

#define fi first
#define se second
#define MP make_pair
#define PB push_back
#define SZ size
#define SIZE(x) (int)(x).size()

#define MAX 2020

char p[200];

void init() {
p['a'] = 'y';
p['b'] = 'h';
p['c'] = 'e';
p['d'] = 's';
p['e'] = 'o';
p['f'] = 'c';
p['g'] = 'v';
p['h'] = 'x';
p['i'] = 'd';
p['j'] = 'u';
p['k'] = 'i';
p['l'] = 'g';
p['m'] = 'l';
p['n'] = 'b';
p['o'] = 'k';
p['p'] = 'r';
p['q'] = 'z';
p['r'] = 't';
p['s'] = 'n';
p['t'] = 'w';
p['u'] = 'j';
p['v'] = 'p';
p['w'] = 'f';
p['x'] = 'm';
p['y'] = 'a';
p['z'] = 'q';
p[' '] = ' ';
}

int main() {
	init();
	int N;
	scanf("%d", &N);
	cin.get();
	
	for (int q = 1; q <= N; q++) {
		string s;
		getline(cin, s);
		
		printf("Case #%d: ", q);
		
		for (int i = 0; i < SIZE(s); i++)
			printf("%c", p[s[i]]);
		
		printf("\n");
	}	
	return 0;
}