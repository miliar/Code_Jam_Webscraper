#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
#include<string.h>
#include<string>
#include<math.h>
using namespace std;
char s[4][5];

bool check(char ch)
{
	for(int i = 0; i < 4; i++) {
		bool flag = true;
		for(int j = 0; j < 4; j++) {
			if(!(s[i][j] == ch || s[i][j] == 'T')) {
				flag = false;
				break;
			}
		}
		if(flag == true) return true;
		flag = true;
		for(int j = 0; j < 4; j++) {
			if(!(s[j][i] == ch || s[j][i] == 'T')) {
				flag = false;
				break;
			}
		}
		if(flag == true) return true;
	}
	bool flag = true;
	for(int i = 0; i < 4; i++) {
		if(!(s[i][i] == ch || s[i][i] == 'T')) {
			flag = false;
			break;
		}
	}
	if(flag == true) return true;
	flag = true;
	for(int i = 0; i < 4; i++) {
		if(!(s[i][3 - i] == ch || s[i][3 - i] == 'T')) {
			flag = false;
			break;
		}
	}
	if(flag == true) return true;
	return false;
}

bool full()
{
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			if(s[i][j] == '.') return false;
		}
	}
	return true;
}


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out.large", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++) {
		for(int j = 0; j < 4; j++) {
			scanf("%s", &s[j]);
		}
		printf("Case #%d: ", i);
		if(check('X') == true) {
			printf("X won\n");
		}
		else if(check('O') == true) {
			printf("O won\n");
		}
		else if(full() == true) {
			printf("Draw\n");
		}
		else {
			printf("Game has not completed\n");
		}
	}
	return 0;
}

