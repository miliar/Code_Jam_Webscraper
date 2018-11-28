#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

vector< vector<char> >line;

int main(){
	int t=0;
	int count=0;
	char c='\n';

	scanf("%d\n",&t);
	line.resize(t);

	while(count<t){
		if (c=='\n') printf("Case #%d: ",count+1);
		scanf("%c",&c);
		switch (c){
			case 'y': printf("a"); break;
			case 'n': printf("b"); break;
			case 'f': printf("c"); break;
			case 'i': printf("d"); break;
			case 'c': printf("e"); break;
			case 'w': printf("f"); break;
			case 'l': printf("g"); break;
			case 'b': printf("h"); break;
			case 'k': printf("i"); break;
			case 'u': printf("j"); break;
			case 'o': printf("k"); break;
			case 'm': printf("l"); break;
			case 'x': printf("m"); break;
			case 's': printf("n"); break;
			case 'e': printf("o"); break;
			case 'v': printf("p"); break;
			case 'z': printf("q"); break;
			case 'p': printf("r"); break;
			case 'd': printf("s"); break;
			case 'r': printf("t"); break;
			case 'j': printf("u"); break;
			case 'g': printf("v"); break;
			case 't': printf("w"); break;
			case 'h': printf("x"); break;
			case 'a': printf("y"); break;
			case 'q': printf("z"); break;
			case ' ': printf(" "); break;
			case '\n': printf("\n"); count++; break;
		}
	}

	return 0;
}