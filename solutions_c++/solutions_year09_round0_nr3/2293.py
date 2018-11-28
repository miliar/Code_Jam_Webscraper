#include <cstdio>
#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

int C = 0;
bool Q[20][505];
int  V[20][505];
const int W = 19;
char wel[W+1] = "welcome to code jam";

int fillQ()
{
	memset(Q, false, sizeof(Q));
	string line;
	getline(cin, line);
	int lineLen = line.length();

	for(int i = 0; i < lineLen; ++i)
	{
		char ch = line.at(i);
		for(int j = 0; j < W; j++) {
			if (wel[j] == ch)
				Q[j][i] = true;
		}
	}

	/*
	for(int i = 0; i < W; ++i) {
		for(int j = 0; j < lineLen; j++) {
			cout << Q[i][j];
		}
		cout << endl;
	}
	*/

	return lineLen;
}

int play()
{
	int lineLen = fillQ();
	int matchNum = 0;
	memset(V, 0, sizeof(V));

	for(int i = 0; i < lineLen; i++) {
		if(Q[0][i])
			V[0][i] = 1;
	}
	for(int i = 1; i < W; ++i) {
		for(int j = 0; j < lineLen; j++) {
			if(Q[i][j]) {
				for(int k = 0; k < j; k++) {
					if(Q[i-1][k]) {
						V[i][j] += V[i-1][k];
						V[i][j] %= 10000;
					}
				}
			}
		}
	}

	for(int j = 0; j < lineLen; j++)
		matchNum += V[W-1][j];

	/*
	cerr << endl;
	for(int i = 0; i < W; ++i) {
		for(int j = 0; j < lineLen; j++) {
			cerr << V[i][j];
		}
		cerr << endl;
	}
	*/

	return (matchNum % 10000);
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	cin >> C;

	string line;
	getline(cin, line);
	for(int i = 1; i <= C; i++)
		cout << "Case #" << i << ": " << setfill ('0') << setw (4) << play() << endl;

	return 0;
}

