#include <iostream>
#include <string>

using namespace std;

void magicka(int C, char c[40][3], int D, char d[40][2], int N, char *invoke) {
	int lettercount[26];
	int len;
	memset(lettercount, 0, sizeof(lettercount));
	string incant;
	for (int i=0; i < N; ++i) {
		incant += invoke[i];
		len = incant.length();
		++lettercount[incant[len-1]-'A'];
		if (len > 1) {
			char c1 = incant[len-2];
			char c2 = incant[len-1];
			if (c1 > c2) {
				char temp = c1; c1 = c2; c2 = temp;
			}
			for (int j = 0; j < C; ++j) {
				if (c1 == c[j][0] && c2 == c[j][1]) {
					incant = incant.substr(0, len-2);
					--lettercount[c1-'A'];
					--lettercount[c2-'A'];
					++lettercount[c[j][2]-'A'];
					incant += c[j][2];
				}
			}
			for (int j = 0; j < D; ++j) {
				if (lettercount[d[j][0]-'A'] > 0 && lettercount[d[j][1]-'A'] > 0) {
					incant = "";
					memset(lettercount, 0, sizeof(lettercount));
				}
			}
		}
	}
			
	cout << "[";
	len = incant.length();
	for (int j = 0; j < len; ++j) {
		if (j > 0)
			cout << ", ";
		cout << incant[j];
	}
	cout << "]\n";
#if 0
	for (int j = 0; j < C; ++j) {
		for (int k = 0; k < 3; ++k) {
  			cout << c[j][k];
		}
		cout << " ";
	}
#endif
}

int main() {

  int T, C, D, N;
  cin >> T;
  char c[40][3], d[40][2], invoke[101];
  char temp;
  for (int cs=0; cs < T; ++cs) {
	cin >> C;
	for (int j = 0; j < C; ++j) {
		cin >> c[j][0];
		cin >> c[j][1];
		cin >> c[j][2];
		if (c[j][0] > c[j][1]) {
			temp = c[j][0]; c[j][0] = c[j][1]; c[j][1] = temp;
		}
	}
	cin >> D;
	for (int j = 0; j < D; ++j) {
		cin >> d[j][0];
		cin >> d[j][1];
		if (d[j][0] > d[j][1]) {
			temp = d[j][0]; d[j][0] = d[j][1]; d[j][1] = temp;
		}
	}
	cin >> N;
	for (int j = 0; j < N; ++j) {
		cin >> invoke[j];
	}
	cout << "Case #" << cs+1 << ": ";
	magicka(C, c, D, d, N, invoke);
  }

}
