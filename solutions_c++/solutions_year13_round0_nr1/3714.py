#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <fstream>

#include <algorithm>
#include <stdio.h>
using namespace std;

char a[4][4] = {0};
bool notDraw = false;


bool hasDot(char *b) {
	for(int i = 0; i < 4; i++) {
		if(b[i] == '.')
			return true;
	}
	return false;
}
int hasT(char *b) {
	for(int i = 0; i < 4; i++) {
		if(b[i] == 'T')
			return i;
	}
	return -1;
}

int countX(char *b) {
	int counter = 0;
	for(int i = 0; i < 4; i++) {
		if(b[i] == 'X'){
			counter++;
		}
	}
	return counter;
}


int checkArr(char *arr) {
	if(!hasDot(arr)) {
		int xAmount = countX(arr);
		if(hasT(arr) >= 0) {
			if(xAmount == 3) {
				return 2; //xwin
			}
			if(xAmount == 0) {
				return 1; //ywin
			} 
			return 0; //draw
		} else {
			if(xAmount == 4) {
				return 2; //xwin
			} if (xAmount == 0) {
				return 1; //ywin
			}
			return 0; // draw
		}
	} else {
		notDraw = true;
	}
	// draw
	return 0;
}

char* prepareRowArr(int i)
{
	char *arr = new char[4];
	for(int j = 0; j < 4; j++) {
		arr[j] = a[i][j];
	}
	return arr;
}

char* prepareColArr(int j)
{
	char *arr = new char[4];
	for(int i = 0; i < 4; i++) {
		arr[i] = a[i][j];
	}
	return arr;
}

char* prepareDiag(bool isMain)
{
	char *arr = new char[4];
	if(isMain) {
		for(int i = 0; i < 4; i++) {
			arr[i] = a[i][i];
		}
	} else{
		for(int i = 0; i < 4; i++) {
			arr[i] = a[i][4-i-1];
		}
	}
	return arr;
}

int checkMatrix()
{
	int result = 0;
	for(int i = 0; i < 4; i++) {
		result = checkArr(prepareRowArr(i));
		if(result > 0){
			return result;
		}
		result = checkArr(prepareColArr(i));
		if(result > 0) {
			return result;
		}
	}

	result = checkArr(prepareDiag(true));
	if(result > 0) {
		return result;
	}

	result = checkArr(prepareDiag(false));
	if(result > 0) {
		return result;
	}

}

int main()
{

	freopen("D://Source//C++//GCJa1//Debug//A-large.in", "rt", stdin);
	freopen("D://Source//C++//GCJa1//Debug//output.txt", "wt", stdout);

	int testCases = 0;
	
	cin>>testCases;

	for (int t = 0; t < testCases; t++) {
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				cin>>a[i][j];
			}
		}

		notDraw = false;
		int result = checkMatrix();
		if(result == 2) {
			cout<<"Case #"<<(t+1)<<": X won"<<endl;
		} else if(result == 1) {
			cout<<"Case #"<<(t+1)<<": O won"<<endl;
		} else if(!notDraw){
			cout<<"Case #"<<(t+1)<<": Draw"<<endl;
		} else {
			cout<<"Case #"<<(t+1)<<": Game has not completed"<<endl;
		}
		
	}


	return 0;
}