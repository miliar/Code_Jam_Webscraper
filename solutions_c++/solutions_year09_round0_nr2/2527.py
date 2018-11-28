#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <fstream>

using namespace std;

typedef pair<int, int> PII;

int mas[100][100];
char res[100][100];
bool mask[100][100];


PII findBottommost(int i, int j, int h, int w){
	PII minim = PII(i, j);
	bool flag = false;
	
	if(mas[i-1][j] < mas[minim.first][minim.second] && i > 0){
		minim = PII(i-1, j);
	}
	if(mas[i][j-1] < mas[minim.first][minim.second] && j > 0){
		minim = PII(i, j-1);
	}
	if(mas[i][j+1] < mas[minim.first][minim.second] && j < w-1){
		minim = PII(i, j+1);
	}
	if(mas[i+1][j] < mas[minim.first][minim.second] && i < h-1){
		minim = PII(i+1, j);
	}
	if(i != minim.first || j != minim.second){
		return minim;
	}else{
		return PII(-1, -1);
	}
	

}

char dfs(char l, int i, int j, int h, int w){
	PII minim = findBottommost(i, j, h, w);
	if(minim.first != -1){
		if(!mask[minim.first][minim.second]){
			char ch = dfs(l, minim.first, minim.second, h, w);
			res[i][j] = ch;
			mask[i][j] = true;
			return ch;
		}else{
			res[i][j] = res[minim.first][minim.second];
			return res[minim.first][minim.second];
		}
	}else{
		res[i][j] = l;
		mask[i][j] = true;
		return l;
	}
}

void solve(int h, int w){
	for(int i=0; i<h; i++){
		for(int j=0; j<w; j++){
			mask[i][j] = false;
		}
	}

	char letter = 'a';
	for(int i=0; i<h; i++){
		for(int j=0; j<w; j++){
			if(!mask[i][j]){
				char ch = dfs(letter, i, j, h, w);
				res[i][j] = ch;
				mask[i][j] = true;
				if(ch == letter){
					letter++;
				}
			}
		}
	}
	
	for(int i=0; i<h; i++){
		for(int j=0; j<w; j++){
			if(j == w-1){
				printf("%c\n", res[i][j]);
				continue;
			}
			printf("%c ", res[i][j]);
		}
		
	}
}

int main(){

	freopen("B-large.in", "rt", stdin);
	freopen("outLarge.txt", "wt", stdout);

	int t;
	scanf("%i", &t);	
	for(int i=0; i<t; i++){
		int h, w;
		scanf("%i%i", &h, &w);
		for(int i=0; i<h; i++){
			for(int j=0; j<w; j++){
				cin >> mas[i][j];
			}
		}
		printf("Case #%i:\n", i+1);
		solve(h, w);
	}

	return 0;
}