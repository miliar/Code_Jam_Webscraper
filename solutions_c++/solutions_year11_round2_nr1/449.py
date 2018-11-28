#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
#include <string>
#include <cstring>
using namespace std;

vector<string> result(100);
int ones[100];
int zeros[100];

double wp[100];
double owp[100];
double oowp[100];

string calc()
{
	stringstream S;
	int i, j;

	int N;
	cin >> N;

	for (i=0; i<N; ++i) {
		cin >> result[i];
	}

	for (i=0; i<N; ++i) {
		ones[i] = zeros[i] = 0;
		for (j=0; j<N; ++j) {
			if (result[i][j] == '1') ones[i]++;
			else if (result[i][j] == '0') zeros[i]++;
		}
	}

	for (i=0; i<N; ++i) {
		wp[i] = double(ones[i]) / (ones[i]+zeros[i]);
	}

	for (i=0; i<N; ++i) {
		owp[i] = 0;
		int num = 0;
		for (j=0; j<N; ++j) if (j!=i && result[i][j]!='.') {
			num++;
			if (result[j][i] == '1') {
				owp[i] += double(ones[j]-1)/(ones[j]+zeros[j]-1);
			} else {
				owp[i] += double(ones[j])/(ones[j]+zeros[j]-1);
			}
		}

		owp[i] /= num;
	}

	for (i=0; i<N; ++i) {
		oowp[i] = 0;
		for (j=0; j<N; ++j) if (result[i][j] != '.') {
			oowp[i] += owp[j];
		}
		oowp[i] /= (ones[i]+zeros[i]);
	}

	for (i=0; i<N; ++i) {
		S << endl << 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
	}

	return S.str();
}

int main(void)
{
	int caseNum;
	cin >> caseNum;
	//string line;
	//getline(cin, line);
	for (int c=1; c<=caseNum; ++c) {
		cout << "Case #" << c << ": " << calc() << endl;
	}

	return 0;
}

