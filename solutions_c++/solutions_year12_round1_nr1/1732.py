#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <vector>
#include <cmath>
using namespace std;

int T, A, B;
double probRightA[100000];
double probWrong, probRight, probWrongA[100000];
int first, second;
double sumProbs, thisKeys, minKeys;

void printWrong() {
	for(int i=0; i<=A; ++i) {
		cout << probWrongA[i] << "  ";
	}
	cout << endl;
}

int main() {
	cin >> T;
	for(int t=1; t<=T; ++t) {
		cout << "Case #" << t << ": ";
		cin >> A >> B;
		minKeys = B+2;
		probWrong = 1;
		for(int a=0; a<A; ++a) {
			cin >> probRightA[a];
			probWrong *= probRightA[a];
		}
		probWrongA[0] = probWrong;
		for(int w=1; w<=A; ++w) {
			probRight = probRightA[A-w];
			probWrong *= (1-probRight)/probRight;
			probWrongA[w] = probWrong;
		}
		for(int backspace=0; backspace<=A; ++backspace) {
			thisKeys = 0;
			sumProbs = 0;
			first = B-A+1+2*backspace;
			second = 2*backspace + 2*B - A + 2;
			for(int j=0; j<=backspace; ++j) {
				sumProbs += probWrongA[j];
			}
			thisKeys = first*sumProbs + second*(1-sumProbs);
			if(thisKeys < minKeys) minKeys = thisKeys;
		}
		//printWrong();
		printf("%.6f\n", minKeys);
	}
	return 0;
}