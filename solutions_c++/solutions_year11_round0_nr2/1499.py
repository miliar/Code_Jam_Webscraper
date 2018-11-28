#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <stack>

using namespace std;

int vv(char c) {
	switch (c) {
		case 'Q': return 0;
		case 'W': return 1;
		case 'E': return 2;
		case 'R': return 3;
		case 'A': return 4;
		case 'S': return 5;
		case 'D': return 6;
		case 'F': return 7;
		default: return 8;
	}
}

char rv(int n) {
	switch (n) {
		case 0: return 'Q';
		case 1: return 'W';
		case 2: return 'E';
		case 3: return 'R';
		case 4: return 'A';
		case 5: return 'S';
		case 6: return 'D';
		case 7: return 'F';
		default: return '-';
	}
}

bool opposesSomeone(vector <int> exists, vector <vector <bool> > oppose, char c) {
	int n = vv(c);

	for (int i = 0; i < 8; i++) {
		if (exists[i] && oppose[n][i])
			return true;
	}

	return false;
}


int main() {
	int T;
	scanf("%d", &T);

	for (int cs = 1; cs <= T; cs++) {
		int C, D, N;
		vector <vector <char> > combine(30, vector <char> (9, '-'));
		vector <vector <bool> > oppose(30, vector <bool> (9, false));
		vector <int> exists (9, 0);
		stack <char> P;

		scanf("%d", &C);
		for (int j = 0; j < C; j++) {
			char aux[5];
			scanf("%s", aux);
			combine[vv(aux[0])][vv(aux[1])] = combine[vv(aux[1])][vv(aux[0])] = aux[2];
		}

		scanf("%d", &D);
		for (int j = 0; j < D; j++) {
			char aux[5];
			scanf("%s", aux);
			oppose[vv(aux[0])][vv(aux[1])] = oppose[vv(aux[1])][vv(aux[0])] = true;
		}

		scanf("%d", &N);
		char str[N+5];
		scanf("%s", str);

		for (int i = 0; i < N; i++) {
			if (!P.empty() && combine[vv(str[i])][vv(P.top())] != '-') {
				int aux = vv(P.top());
				P.pop();
				P.push(combine[vv(str[i])][aux]);
				exists[aux]--;
			}
			else if (opposesSomeone(exists, oppose, str[i])) {
				while (!P.empty())
					P.pop();
				for (int j = 0; j < 9; j++)
					exists[j] = 0;
			}
			else {
				P.push(str[i]);
				exists[vv(str[i])]++;
			}
		}

		int size = P.size();
		char res[size];
		for (int i = P.size()-1; i >= 0; i--) {
			res[i] = P.top();
			P.pop();
		}

		printf ("Case #%d: [", cs);
		if (size > 0) {
			printf("%c", res[0]);
			for (int i = 1; i < size; i++)
				printf(", %c", res[i]);
		}
		printf("]\n");
	}

	return 0;
}
