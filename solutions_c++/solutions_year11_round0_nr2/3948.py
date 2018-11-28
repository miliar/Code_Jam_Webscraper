#include <iostream>
#include <stdio.h>
using namespace std;

#define MAXN 200
int combineMenu[26][26] = {-1};
bool clearMenu[26][26] = {false};
char invokeStack[MAXN];
int stackPtr = 0;
void input(){
	for (int i = 0; i < 26; i++)
		for (int j = 0; j < 26; j++){
			combineMenu[i][j] = -1;
			clearMenu[i][j] = false;
		}
	
	char a, b, c;
	int num;
	scanf("%d", &num);
	for (int i = 0; i < num; i++){
		scanf("%*c%c%c%c", &a, &b, &c);
		combineMenu[a - 65][b - 65] = c - 65;
		combineMenu[b - 65][a - 65] = c - 65;
	}

	scanf("%d", &num);
	for (int i = 0; i < num; i++){
		scanf("%*c%c%c", &a, &b);
		clearMenu[a - 65][b - 65] = true;
		clearMenu[b - 65][a - 65] = true;
	}

}
void solveProblem(){
	stackPtr = 0;
	int n;
	scanf("%d", &n);
	char c;
	scanf("%*c");
	for (int i = 0; i < n; i++){
		scanf("%c", &c);
		invokeStack[stackPtr++] = c;
		//combination
		while (stackPtr >= 2){
			char pre = invokeStack[stackPtr - 2];
			char now = invokeStack[stackPtr - 1];
			int num = combineMenu[pre - 65][now - 65];
			if (num != -1){
				invokeStack[stackPtr - 2] = char(num + 65);
				stackPtr--;
			}else
				break;
		}
		//clear
		char now = invokeStack[stackPtr - 1];
		for (int i = stackPtr - 2; i >= 0; i--){
			char temp = invokeStack[i];
			if (clearMenu[temp - 65][now - 65]){
				stackPtr = 0;
				break;
			}
		}
	}
	scanf("%*c");
}
void output(int t){
	printf("Case #%d: [", t);
	for (int i = 0; i < stackPtr; i++){
		if (i != 0)
			printf(", ");
		printf("%c", invokeStack[i]);
	}
	printf("]\n");
}
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		input();
		solveProblem();
		output(i);
	}
	return 0;
}