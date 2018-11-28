#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;

bool **p;
char **words;
char*  pattern;
int plen;


int L, D, N;
int count();
void patternDisolve();


void main(){
	freopen("D:\\Visual Studio 2008\\Projects\\googlejam2008\\Alien Language\\input.txt", "rt", stdin);
	freopen("D:\\Visual Studio 2008\\Projects\\googlejam2008\\Alien Language\\output.txt", "wt", stdout);

	scanf("%d %d %d", &L, &D, &N);
//	printf("%d, %d, %d", L, D, N);
	
	pattern = new char [1000];

	p = new bool *[L];
	for(int i = 0; i < L; i ++){
		p[i] = new bool[26];
	}

	words = new char*[D];
	for(int i = 0; i < D; i ++){
		words[i] = new char[L + 1];
	}

	int i;
	for(i = 0; i < D; i ++)
		scanf("%s", words[i]);
//	printf("%s", words[D -1]);



	for(i = 0; i < N; i ++){
		scanf("%s", pattern);
		plen = strlen(pattern);
		printf("Case #%d: %d\n", i + 1, count());
	}
}

int count(){
	int count = D;
	patternDisolve();
	for(int i = 0; i < D; i ++){
		for(int j = 0; j < L; j ++){
			if(p[j][(words[i][j] - 'a')] == false){
				count --; 
				break;
			}
		}

	}
	return count;
}

void patternDisolve(){
	bool inParenthesis = false;
	int index = -1;
	
	for(int i = 0; i < L; i ++)
		for(int j = 0; j < 26; j ++)
			p[i][j] = false;

	for(int i = 0; i < plen; i ++){
		if(! inParenthesis){
			if(pattern[i] == '('){
				inParenthesis= true;
				index ++;
			}
			else
			{
				index ++;
				p[index][pattern[i] - 'a'] = true;
			}			
		}
		else
		{
			if(pattern[i] == ')'){
				inParenthesis = false;
			}
			else{
				p[index][pattern[i] -'a'] = true;
			}
		}
	}

}