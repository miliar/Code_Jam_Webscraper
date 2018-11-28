#include<iostream>
#include<sstream>
#include<cstdio>
#include<stack>
#include<queue>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<vector>
#define MAX 5
#define TAMANIO 4
using namespace std;

void clearStack(stack <char> &s){
	while(!s.empty()){
		s.pop();
	}
}

int compareStack(stack <char> &s){
	//char rightV;
	//char leftV;
	
	int countT = 0;
	int countX = 0;
	int countO = 0;
	int countEmpty = 0;
	while (!s.empty()){
		if (s.top() == 'X')
			countX++;
		else if (s.top() == 'T')
			countT++;
		else if (s.top() == 'O')
			countO++;
		else if (s.top() == '.')
			countEmpty++;
		s.pop();
	}
	//clearStack(s);
	if (countX == 4)
		return 1;
	else if (countO == 4)
		return 2;
	else if (countO == 3 && countT == 1)
		return 2;
	else if (countX == 3 && countT == 1)
		return 1;
	else if (countEmpty > 0)
		return 4;
	return 3;
}
int main(){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int eval;
	char board[MAX][MAX];
	stack <char> letterStack;
	int T;
	int numberOfCases = 0;
	int I;
	int J;
	string line;
	char arreglo[MAX];
	scanf("%d", &T);
	cin.ignore();
	while (numberOfCases < T){
		for (I = 0; I < TAMANIO; I++){
			getline(cin, line);
			for (int it = 0; it < (int)line.size(); it++){
				arreglo[it] = line[it];
			}
			for (J = 0; J < TAMANIO; J++){
				board[I][J] = arreglo[J];
			}
			//cin.ignore();
		}
		getline(cin, line);
	
		// check rows
		for (I = 0; I < TAMANIO; I++){
			for (J = 0; J < TAMANIO; J++){
				letterStack.push(board[I][J]);
			}
			eval = compareStack(letterStack);
			if (eval == 1 || eval == 2){
				break;
			}
		}
		if (!(eval == 1 || eval == 2)){
		// check columns
		for (J = 0; J < TAMANIO; J++){
			for (I = 0; I < TAMANIO; I++){
				letterStack.push(board[I][J]);
			}
			eval = compareStack(letterStack);
			if (eval == 1 || eval == 2){
				break;
			}
		}
		}

		if ((!(eval == 1 || eval == 2))){
			// check for diagonals
			for (I = 0; I < TAMANIO; I++){
				letterStack.push(board[I][I]);
			}
				eval = compareStack(letterStack);
		}

		if ((!(eval == 1 || eval == 2))){
			// check for diagonals
			for (I = 0; I < TAMANIO; I++)
				letterStack.push(board[I][TAMANIO - (1 + I)]);
				eval = compareStack(letterStack);
		}
		
		if ((!(eval == 1 || eval == 2))){
		for (I = 0; I < TAMANIO; I++){
			for (J = 0; J < TAMANIO; J++){
				letterStack.push(board[I][J]);
			}
			eval = compareStack(letterStack);
			if (eval == 4)
				break;
		}
		}
		/*for (I = 0; I < TAMANIO; I++){
			for (J = 0; J < TAMANIO; J++){
				printf("%c", board[I][J]);
			}
			printf("\n");
		}
		printf("\n");*/
	numberOfCases++;
	printf("Case #%d: ", numberOfCases);

	if (eval == 1){
		printf("X won\n");
	}
	else if (eval == 2){
		printf("O won\n");
	}
	else if (eval == 4){
		printf("Game has not completed\n");
	}
	else if (eval == 3){
		printf("Draw\n");
	}
	}
		return 0;
}