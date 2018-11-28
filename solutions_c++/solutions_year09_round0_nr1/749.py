
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
using namespace std;


#define L0 20
#define D0 5010
#define N0 510

string words[D0];
string keys[L0];
int L, D, N;

void change(string &st, int n){
	int i, j = 0;

	for (i = 0; i < L; i++){
		keys[i] = "";
		if (st[j] == '('){
			while (st[j] != ')'){
				j++; keys[i] += st[j];
			}
		}
		else {
			keys[i] += st[j];
		}
		j++;
	}
}

bool yes(string &w){
	int i, j;

	for (i = 0; i < L; i++){
		for (j = 0; j < (int)keys[i].length(); j++){
			if (keys[i][j] == w[i]) break;
		}

		if (j >= (int)keys[i].length()) return(false);
	}

	return(true);
}

void solve(int n){
	int i, r = 0;

	cout << "Case #" << n + 1 << ": ";

	for (i = 0; i < D; i++){
		if (yes(words[i])){
			r++;
		}
	}

	cout << r << endl;
}

void calc(){
	int i;
	string st;

	cin >> L >> D >> N;
	for (i = 0; i < D; i++)
		cin >> words[i];

	for (i = 0; i < N; i++){
		cin >> st;
		change(st, i);
		solve(i);
	}
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	calc();

	return 0;
}