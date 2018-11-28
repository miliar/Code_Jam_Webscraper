#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

const int maxn = 128;

int games[maxn][maxn];
double wpCache[maxn];
double wp2Cache[maxn][maxn];
double owpCache[maxn];
double oowpCache[maxn];
int n;

void input() {
	cin >> n;
	string line;
	memset(games, -1, sizeof(games));
	getline(cin, line);
	for (int i=0;i<n;i++) {
		wpCache[i] = owpCache[i] = oowpCache[i] = -1;
		getline(cin, line);
		for (int j=0;j<n;j++) {
			wp2Cache[i][j] = -1;
			if (line[j] == '0') games[i][j] = 0;
			else if (line[j] == '1') games[i][j] = 1;
			else games[i][j] = -1;
		}
	}
}

double winPercentage(int x) {
	if (wpCache[x] < 0) {
		int gamesWon = 0, gamesTotal = 0;
		for (int i=0;i<n;i++) {
			if (games[x][i] == -1) continue;
			gamesTotal++;
			if (games[x][i] == 1) gamesWon++;
		}
		wpCache[x] = ((double)gamesWon / (double)gamesTotal);
	}
	return wpCache[x];
}

double wpWithOut(int x, int withOut) {
	if (wp2Cache[x][withOut] < 0) {
		int gamesWon = 0, gamesTotal = 0;
		for (int i=0;i<n;i++) {
			if (withOut == i) continue;
			if (games[x][i] == -1) continue;
			gamesTotal++;
			if (games[x][i] == 1) gamesWon++;
		}
		wp2Cache[x][withOut] = ((double)gamesWon / (double)gamesTotal);
	}
	return wp2Cache[x][withOut];
}

double opponentsWinPercentage(int x) {
	if (owpCache[x] < 0) {
		double wpTotal = 0;
		int wpCount = 0;
		for (int i=0;i<n;i++) {
			if (games[x][i] == -1) continue;
			wpCount++;
			wpTotal = wpTotal + wpWithOut(i,x);
		}
		owpCache[x] = wpTotal / (double)wpCount;
	} 
	return owpCache[x];
}

double opponentsOpponentsWinPercentage(int x) {
	if (oowpCache[x] < 0) {
		double wpTotal = 0;
		int wpCount = 0;
		for (int i=0;i<n;i++) {
			if (games[x][i] == -1) continue;
			wpCount++;
			wpTotal = wpTotal + opponentsWinPercentage(i);
		}
		oowpCache[x] = wpTotal / (double)wpCount;
	} 
	return oowpCache[x];
}

void output() {
	for (int i=0;i<n;i++) {
		cout << fixed << setprecision(12) << 0.25 * winPercentage(i) + 0.5 * opponentsWinPercentage(i) + 0.25 * opponentsOpponentsWinPercentage(i) << "\n";
	}
	/*
	for (int i=0;i<n;i++) {
		cerr << winPercentage(i,127) << " " << opponentsWinPercentage(i) << " " << opponentsOpponentsWinPercentage(i) << "\n";
	}
	*/
}

int main() {

	int T,t;

	cin >> T;
	
	for (t=1;t<=T;++t) {
		input();
		//solve();
		cout << "Case #" << t << ":\n";
		output();
	}

	return 0;

}