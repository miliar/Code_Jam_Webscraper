#include <cstdio>
#include <cstdlib>

inline int abs(int a) {return a < 0 ? -a : a;}

struct Button {
	int color;
	int position;
};

struct Pos {
	int space;
	int time;
};

void Open() {
	freopen ("BotTrust.in", "r", stdin);
	freopen ("BotTrust.out", "w", stdout);
}

void Close() {
	fclose(stdin);
	fclose(stdout);
}

void Input(int &N, Button *seq) {
	scanf ("%d ", &N);
	for (int i = 0; i < N; i++) {
		char tcol;
		scanf ("%c %d ", &tcol, &seq[i].position);
		if (tcol == 'O') 
			seq[i].color = 0;
		else 
			seq[i].color = 1;
	}
}

void Output(int caseNo, int answer) {
	printf ("Case #%d: %d\n", caseNo, answer);
}

int Calc(int &N, Button *seq) {
	//printf ("---------debug-----------\n");
	int answer = 0, adjacent = 0;
	Pos recent[2];
	recent[0].time = recent[1].time = 0;
	recent[0].space = recent[1].space = 1;
	for (int i = 0; i < N; i++) {
		Pos tmp;
		if (seq[i].color == adjacent) {
			tmp.time = recent[adjacent].time + abs(recent[adjacent].space - seq[i].position) + 1;
			tmp.space = seq[i].position;
			recent[adjacent] = tmp;
			if (tmp.time > answer) answer = tmp.time;
		} else {
			int col = seq[i].color;
			tmp.time = recent[col].time + abs(recent[col].space - seq[i].position) + 1;
			tmp.space = seq[i].position;
			if (recent[adjacent].time + 1 > tmp.time) tmp.time = recent[adjacent].time + 1;
			recent[col] = tmp;
			adjacent = col;
			if (tmp.time > answer) answer = tmp.time;
		}
		//printf ("%d\n", tmp.time);
	}
	//printf ("-------------end-----------\n");
	return answer;
}

void Work() {
	int T, N, answer;
	Button *seq = new Button[1000];
	scanf ("%d", &T);
	for (int caseNo = 1; caseNo <= T; caseNo++) {
		Input(N, seq);
		answer = Calc(N, seq);
		Output(caseNo, answer);
	}
	delete[] seq;
}

int main() {
	Open();
	Work();
	Close();
	return 0;
}
