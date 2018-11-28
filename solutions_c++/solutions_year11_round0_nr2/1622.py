#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
#include <string>
#include <cstring>
using namespace std;

int comb[26][26];
int oppo[26][26];
	
string calc()
{
	memset(comb, -1, sizeof(comb));
	memset(oppo, 0, sizeof(oppo));

	int i, j, k;

	//string line;
	//getline(cin, line);

	int C;
	string str;
	cin >> C;
	for (i=0; i<C; ++i) {
		cin >> str;
		int a = str[0]-'A';
		int b = str[1]-'A';
		int c = str[2]-'A';
		comb[a][b] = comb[b][a] = c;
	}

	int D;
	cin >> D;
	for (i=0; i<D; ++i) {
		cin >> str;
		int a = str[0]-'A';
		int b = str[1]-'A';
		oppo[a][b] = oppo[b][a] = 1;
	}

	int N;
	cin >> N;
	cin >> str;

	i = 0;
	j = 1;
	for (j=1; j<N; ++j) {
		if (i < 0) {
			str[0] = str[j];
			i = 0;
			continue;
		}

		int a = str[i]-'A';
		int b = str[j]-'A';
		if (comb[a][b] != -1) {
			str[i] = 'A' + comb[a][b];
			continue;
		}

		for (k=0; k<=i; ++k) {
			int a = str[k]-'A';
			if (oppo[a][b] == 1) {
				break;
			}
		}
		if (k <= i) {
			i = -1;
			continue;
		}

		str[++i] = str[j];
	}

	stringstream S;
	S << "[";
	if (i >= 0) {
		S << str[0];

		for (j=1; j<=i; ++j) {
			S << ", " << str[j];
		}
	}
	S << "]";

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

