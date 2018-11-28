#include <cstdio>
#include <vector>

using namespace std;

void Open() {
	freopen ("Magicka.in", "r", stdin);
	freopen ("Magicka.out", "w", stdout);
}

void Close() {
	fclose(stdin);
	fclose(stdout);
}

void GetRelation(int comb[][26], bool oppo[][26]) {
	int C, D;
	for (int i = 0; i < 26; i++)
		for (int j = 0; j < 26; j++)
			comb[i][j] = -1, oppo[i][j] = 0;
	
	scanf ("%d ", &C);
	for (int i = 0; i < C; i++) {	
		char ta, tb, tc;
		int na, nb, nc;
		scanf ("%c%c%c ", &ta, &tb, &tc);
		na = (int)ta - 65, nb = (int)tb - 65, nc = (int)tc - 65;
//		printf ("%d %d %d\n", na, nb, nc);
		comb[na][nb] = nc;
		comb[nb][na] = nc;
	}

	scanf ("%d ", &D);
	for (int i = 0; i < D; i++) {
		char ta, tb;
		int na, nb;
		scanf ("%c%c ", &ta, &tb);
		na = (int)ta - 65, nb = (int)tb - 65;
		oppo[na][nb] = 1;
		oppo[nb][na] = 1;
	}
/*
	for (int i = 0; i < 26; i++) {
		for (int j = 0; j < 26; j++) 
			printf ("%d ", (int)oppo[i][j]);
		printf ("\n");
	}
*/
}

void Action(int comb[][26], bool oppo[][26], vector<int> &answer) {
	int N;
	answer.clear();
	scanf ("%d ", &N);

	int *oppoCount = new int[26];

	for (int i = 0; i < 26; i++) oppoCount[i] = 0;

	for (int i = 0; i < N; i++) {
		char tmp;
		int tn;
		scanf ("%c", &tmp);
		tn = (int)tmp - 65;

		while(1) {
			if (answer.empty()) break;
			int tb = answer.back();
			if (comb[tn][tb] < 0) break;
			answer.pop_back();
			for (int j = 0; j < 26; j++)
				if (oppo[tb][j]) oppoCount[j]--;
			tn = comb[tn][tb];
		}

		if (oppoCount[tn] > 0) {
			answer.clear();
			for (int j = 0; j < 26; j++) oppoCount[j] = 0;
		} else {
			answer.push_back(tn);
			for (int j = 0; j < 26; j++) 
				if (oppo[tn][j]) oppoCount[j]++;
		}

		//for (int i = 0; i < 26; i++) printf ("%d ", oppoCount[i]);
		//printf ("\n");
	}

	delete[] oppoCount;
}

void Output(int caseNo, vector<int> &answer) {
	printf ("Case #%d: [", caseNo);
	for (int i = 0; i < answer.size(); i++) {
		char tmp = (char)(answer[i] + 65);
		printf ("%c", tmp);
		if (i != (answer.size() - 1)) printf (", ");
	}
	printf ("]\n");
}

void Work() {
	int T;
	int (*comb)[26] = new int[26][26];
	bool (*oppo)[26] = new bool[26][26];
	vector<int> answer;
	scanf ("%d", &T);

	for (int caseNo = 1; caseNo <= T; caseNo++) {
		GetRelation(comb, oppo);
		Action(comb, oppo, answer);
		Output(caseNo, answer);
	}

	delete[] comb;
	delete[] oppo;
}

int main() {
	Open();
	Work();
	Close();
}
