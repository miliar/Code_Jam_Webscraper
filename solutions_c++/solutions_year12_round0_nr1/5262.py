#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define NMAX 110

char orig[] = "abcdefghijklmnopqrstuvwxyz";
//char code[] = "ynficwlbkuomxsevzpdrjgthaq";
char code[] = "yhesocvxduiglbkrztnwjpfmaq";
char instr[NMAX];

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tc;
	cin >> tc;
	gets(instr);
	for (int tci=0; tci<tc; tci++){
		gets(instr);
		int len = strlen(instr);
		for (int i=0; i<len; i++)
			if (instr[i] != ' ')
				instr[i] = code[instr[i] - 'a'];
		printf("Case #%d: %s\n", tci+1, instr);
	}
}