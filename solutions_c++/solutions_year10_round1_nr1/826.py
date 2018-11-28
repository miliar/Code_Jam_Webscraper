#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

char bboard[60][60];
char board[60][60];

string checkwin(int N, int K) {
	int i, j, k;
	int Rwins = false;
	int Bwins = false;
	int Rlen, Blen;

	REP(i,N) {
		Rlen = 0;
		Blen = 0;
		char prev = 0;
		REP(j, N) {
			if (board[i][j] == 'R' && prev == 'R') {
				++Rlen;
			}
			if (board[i][j] == 'B' && prev == 'B') {
				++Blen;
			}
			if (board[i][j] == 'R' && prev != 'R') {
				Blen = 0;
				Rlen = 1;
			}
			if (board[i][j] == 'B' && prev != 'B') {
				Blen = 1;
				Rlen = 0;
			}

			prev = board[i][j];

			if (Blen >= K)
				Bwins = true;
			if (Rlen >= K)
				Rwins = true;
		}
	}

	REP(j,N) {
		Rlen = 0;
		Blen = 0;
		char prev = 0;
		REP(i, N) {
			if (board[i][j] == 'R' && prev == 'R') {
				++Rlen;
			}
			if (board[i][j] == 'B' && prev == 'B') {
				++Blen;
			}
			if (board[i][j] == 'R' && prev != 'R') {
				Blen = 0;
				Rlen = 1;
			}
			if (board[i][j] == 'B' && prev != 'B') {
				Blen = 1;
				Rlen = 0;
			}

			prev = board[i][j];

			if (Blen >= K)
				Bwins = true;
			if (Rlen >= K)
				Rwins = true;
		}
	}

	REP(k,N) {
		Rlen = 0;
		Blen = 0;
		char prev = 0;
		i = 0;
		j = k;
		while(i < N && j < N) {
			if (board[i][j] == 'R' && prev == 'R') {
				++Rlen;
			}
			if (board[i][j] == 'B' && prev == 'B') {
				++Blen;
			}
			if (board[i][j] == 'R' && prev != 'R') {
				Blen = 0;
				Rlen = 1;
			}
			if (board[i][j] == 'B' && prev != 'B') {
				Blen = 1;
				Rlen = 0;
			}

			prev = board[i][j];
			++i;
			++j;

			if (Blen >= K)
				Bwins = true;
			if (Rlen >= K)
				Rwins = true;
		}
	}

	REP(k,N) {
		Rlen = 0;
		Blen = 0;
		char prev = 0;
		i = k;
		j = 0;
		while(i < N && j < N) {
			if (board[i][j] == 'R' && prev == 'R') {
				++Rlen;
			}
			if (board[i][j] == 'B' && prev == 'B') {
				++Blen;
			}
			if (board[i][j] == 'R' && prev != 'R') {
				Blen = 0;
				Rlen = 1;
			}
			if (board[i][j] == 'B' && prev != 'B') {
				Blen = 1;
				Rlen = 0;
			}

			prev = board[i][j];
			++i;
			++j;

			if (Blen >= K)
				Bwins = true;
			if (Rlen >= K)
				Rwins = true;
		}
	}

	REP(k,N) {
		Rlen = 0;
		Blen = 0;
		char prev = 0;
		i = k;
		j = 0;
		while(i >= 0 && j < N) {
			if (board[i][j] == 'R' && prev == 'R') {
				++Rlen;
			}
			if (board[i][j] == 'B' && prev == 'B') {
				++Blen;
			}
			if (board[i][j] == 'R' && prev != 'R') {
				Blen = 0;
				Rlen = 1;
			}
			if (board[i][j] == 'B' && prev != 'B') {
				Blen = 1;
				Rlen = 0;
			}

			prev = board[i][j];
			--i;
			++j;

			if (Blen >= K)
				Bwins = true;
			if (Rlen >= K)
				Rwins = true;
		}
	}

	REP(k,N) {
		Rlen = 0;
		Blen = 0;
		char prev = 0;
		i = N - 1;
		j = k;
		while(i >= 0 && j < N) {
			if (board[i][j] == 'R' && prev == 'R') {
				++Rlen;
			}
			if (board[i][j] == 'B' && prev == 'B') {
				++Blen;
			}
			if (board[i][j] == 'R' && prev != 'R') {
				Blen = 0;
				Rlen = 1;
			}
			if (board[i][j] == 'B' && prev != 'B') {
				Blen = 1;
				Rlen = 0;
			}

			prev = board[i][j];
			--i;
			++j;

			if (Blen >= K)
				Bwins = true;
			if (Rlen >= K)
				Rwins = true;
		}
	}

	if (!Rwins && !Bwins)
		return "Neither";
	if (Rwins && Bwins)
		return "Both";
	if (Rwins)
		return "Red";
	return "Blue";
}

void main() {
	int T,K,N;
	char buf[100];

	gets(buf);
	sscanf(buf, "%d", &T);

	int i,j,k;

	REP(i,T) {
		gets(buf);
		sscanf(buf, "%d %d\n", &N, &K);
		memset(bboard, 0, sizeof(bboard));
		memset(board, 0, sizeof(board));
		REP(j,N) {
			gets(buf);
			REP(k, N) {
				if (buf[k] != '.')
					bboard[N - j - 1][k] = buf[k];
			}
		}

		/*
		printf("zero %d\n", K);
		REP(j,N) {
			REP(k,N) {
				if (bboard[N - j - 1][k] == 0)
					printf(".");
				else
					printf("%c", bboard[N - j - 1][k]);
			}
			printf("\n");
		}*/

		REP(j,N) {
			REP(k, N) {
				board[N - k - 1][j] = bboard[j][k];
			}
		}

		/*
		printf("\none\n");
		REP(j,N) {
			REP(k,N) {
				if (board[N - j - 1][k] == 0)
					printf(".");
				else
					printf("%c", board[N - j - 1][k]);
			}
			printf("\n");
		}*/

		REP(k,N) {
			int em = 0;
			while (board[em][k] != 0)
				++em;

			FOR(j,em+1,N-1) {
				if (board[j][k] != 0) {
					board[em][k] = board[j][k];
					board[j][k] = 0;
					while (board[em][k] != 0)
						++em;
				}
			}
		}

		/*
		printf("\ntwo\n");
		REP(j,N) {
			REP(k,N) {
				if (board[N - j - 1][k] == 0)
					printf(".");
				else
					printf("%c", board[N - j - 1][k]);
			}
			printf("\n");
		}*/

		cout << "Case #" << (i+1) << ": " << checkwin(N,K) << endl;
	}
}