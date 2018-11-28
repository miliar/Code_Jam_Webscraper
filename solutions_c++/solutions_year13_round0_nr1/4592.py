#include <string>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

bool isnotcomp(const string &S)
{
	return ((S[0] == '.') || (S[1] == '.') || (S[2] == '.') || (S[3] == '.'));
}

bool iswinner(const char P, const string &S)
{
	string S2 = S;
	for (int i = 0; i < 4; i++) if (S2[i] == 'T') S2[i] = P;
	return ((S2[0] == P) && (S2[1] == P) && (S2[2] == P) && (S2[3] == P)); 
}

vector<string> rows(char B[5][5])
{
	vector<string> V; V.clear();
	for (int i = 0; i < 4; i++) V.push_back(&B[i][0]);

	for (int j = 0; j < 4; j++) {
		string s = "";
		for (int i = 0; i < 4; i++) s += B[i][j];
		V.push_back(s);
	}

	string sd = "";
	for (int i = 0; i < 4; i++) {
		sd += B[i][i];
	}
	V.push_back(sd);

	string sod = "";
	for (int i = 0; i < 4; i++) {
		sod += B[3-i][i];
	}
	V.push_back(sod);

//	for (int i = 0; i < V.size(); i++) cout << V[i] << endl;
	return V;
}

int main(int argc, char *argv[])
{
	char B[5][5];
	int T;
	typedef enum { DRAWN, X_WON, O_WON, INCOMPLETE } flag_t;
	scanf("%d\n",&T);
	for (int t = 0; t < T; t++) {

		flag_t flag = DRAWN;
		for (int i = 0; i < 4; i++) {
			scanf("%s", &B[i][0]);
			//cout << B[i] << endl;
		}

		vector<string> V = rows(B);
		//cout << endl;
		int sz = V.size();
		for (int i = 0; i < sz; i++) {

			if (iswinner('X', V[i])) {
				//cout << V[i] << endl;
				flag = X_WON;
				break;
			}

			if (iswinner('O', V[i])) {
				//cout << V[i] << endl;
				flag = O_WON;
				break;
			}
		}

		if ((flag != X_WON) && (flag != O_WON)) { 
			for (int i = 0; i < sz; i++) {
				if (isnotcomp(V[i])) {
					// cout << V[i] << endl;
					flag = INCOMPLETE;
					break;
				}

			}
		}
		string msg = "";
		switch (flag) {
			case DRAWN: 
				msg = "Draw";
				break;
			case X_WON: 
				msg = "X won";
				break;
			case O_WON:
				msg = "O won";
				break;
			case INCOMPLETE:
				msg = "Game has not completed";
				break;
			default:
				msg = "Draw";
		}

		printf("Case #%d: %s\n", t+1, msg.c_str());
	}

	return 0;
}
